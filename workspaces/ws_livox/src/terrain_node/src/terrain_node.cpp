// terrain_node: 2.5D 坡度分析
// 输入:  /cloud_registered (FAST-LIO 全局点云, map 系)
// 输出:  /traversability   可通行性图 OccupancyGrid
//          0=可通行(坡度<=max_slope), 100=障碍(陡坡/高台阶/凸起)
//        /obstacle_cloud   过滤后点云(地面/坡面剔除, 只留凸起障碍) → local costmap
//        /heightmap        调试: 高度图(可选)
//
// 原理: 点云投影到 2.5D 栅格, 每格记录最高点 z; 计算格与邻域的高度差 /
//       水平距离得到坡度; 按 max_slope_deg 分类。同时把"高于局部地面
//       z_ground + obstacle_min_height"的点作为障碍点输出。

#include <cmath>
#include <limits>
#include <string>
#include <vector>

#include <rclcpp/rclcpp.hpp>
#include <sensor_msgs/msg/point_cloud2.hpp>
#include <nav_msgs/msg/occupancy_grid.hpp>
#include <visualization_msgs/msg/marker.hpp>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <tf2_ros/buffer.h>
#include <tf2_ros/transform_listener.h>
#include <tf2_sensor_msgs/tf2_sensor_msgs.hpp>
class TerrainNode : public rclcpp::Node
{
public:
  TerrainNode() : Node("terrain_node"), tf_buffer_(get_clock()), tf_listener_(tf_buffer_)
  {
    declare_parameter<std::string>("cloud_topic", "/cloud_registered");
    declare_parameter<std::string>("map_frame", "map");
    declare_parameter<double>("resolution", 0.1);
    declare_parameter<double>("map_width", 40.0);
    declare_parameter<double>("map_height", 40.0);
    declare_parameter<double>("max_range", 30.0);
    declare_parameter<double>("max_slope_deg", 10.0);
    declare_parameter<double>("obstacle_min_height", 0.12);
    declare_parameter<double>("z_ground_offset", 0.05);
    declare_parameter<double>("publish_rate", 5.0);

    cloud_topic_ = get_parameter("cloud_topic").as_string();
    map_frame_ = get_parameter("map_frame").as_string();
    resolution_ = get_parameter("resolution").as_double();
    map_width_ = get_parameter("map_width").as_double();
    map_height_ = get_parameter("map_height").as_double();
    max_range_ = get_parameter("max_range").as_double();
    max_slope_ = std::tan(get_parameter("max_slope_deg").as_double() * M_PI / 180.0);
    obstacle_min_height_ = get_parameter("obstacle_min_height").as_double();
    z_ground_offset_ = get_parameter("z_ground_offset").as_double();

    cols_ = static_cast<int>(map_width_ / resolution_);
    rows_ = static_cast<int>(map_height_ / resolution_);
    heightmap_.assign(cols_ * rows_, std::numeric_limits<float>::lowest());
    obstacle_count_.assign(cols_ * rows_, 0);

    sub_ = create_subscription<sensor_msgs::msg::PointCloud2>(
      cloud_topic_, rclcpp::SensorDataQoS(),
      [this](const sensor_msgs::msg::PointCloud2::SharedPtr msg) { cloudCb(msg); });

    pub_trav_ = create_publisher<nav_msgs::msg::OccupancyGrid>("/traversability", 1);
    pub_obs_ = create_publisher<sensor_msgs::msg::PointCloud2>("/obstacle_cloud", 1);

    auto period = std::chrono::milliseconds(
      static_cast<int64_t>(1000.0 / get_parameter("publish_rate").as_double()));
    timer_ = create_wall_timer(period, [this]() { publishMaps(); });

    RCLCPP_INFO(get_logger(), "terrain_node: %s, res=%.2f, slope<=%.1fdeg, obs_min_h=%.2f",
                cloud_topic_.c_str(), resolution_,
                get_parameter("max_slope_deg").as_double(), obstacle_min_height_);
  }

private:
  void cloudCb(const sensor_msgs::msg::PointCloud2::SharedPtr msg)
  {
    // 转换到 map 系(若点云已在 map 系, lookup 失败则直接用)
    sensor_msgs::msg::PointCloud2 cloud_map = *msg;
    try {
      if (tf_buffer_.canTransform(map_frame_, msg->header.frame_id, msg->header.stamp,
                                  tf2::durationFromSec(0.1))) {
        tf2::doTransform(*msg, cloud_map,
          tf_buffer_.lookupTransform(map_frame_, msg->header.frame_id,
                                     msg->header.stamp));
      }
    } catch (const tf2::TransformException & e) {
      RCLCPP_WARN_THROTTLE(get_logger(), *get_clock(), 2000,
                           "TF 转换失败, 使用原始坐标系: %s", e.what());
    }

    pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>());
    pcl::fromROSMsg(cloud_map, *cloud);

    // 清空高度图
    std::fill(heightmap_.begin(), heightmap_.end(), std::numeric_limits<float>::lowest());

    // 投影到栅格
    for (const auto & p : cloud->points) {
      if (std::isnan(p.x) || std::isnan(p.y) || std::isnan(p.z)) continue;
      float dx = p.x - map_center_x_;
      float dy = p.y - map_center_y_;
      if (std::hypot(dx, dy) > max_range_) continue;
      int c = static_cast<int>((p.x - map_origin_x_) / resolution_);
      int r = static_cast<int>((p.y - map_origin_y_) / resolution_);
      if (c < 0 || c >= cols_ || r < 0 || r >= rows_) continue;
      int idx = r * cols_ + c;
      if (p.z > heightmap_[idx]) heightmap_[idx] = p.z;
    }

    // 计算可通行性 + 提取障碍点
    traversability_.assign(cols_ * rows_, 0);
    obstacle_cloud_.clear();
    const float hres = static_cast<float>(resolution_);

    for (int r = 0; r < rows_; ++r) {
      for (int c = 0; c < cols_; ++c) {
        int idx = r * cols_ + c;
        float z = heightmap_[idx];
        if (z == std::numeric_limits<float>::lowest()) continue;  // 无数据, 保持 0(可通行)

        // 与 8 邻域的最大坡度
        float max_slope = 0.0f;
        for (int dr = -1; dr <= 1; ++dr) {
          for (int dc = -1; dc <= 1; ++dc) {
            if (dr == 0 && dc == 0) continue;
            int rr = r + dr, cc = c + dc;
            if (rr < 0 || rr >= rows_ || cc < 0 || cc >= cols_) continue;
            float zn = heightmap_[rr * cols_ + cc];
            if (zn == std::numeric_limits<float>::lowest()) continue;
            float dist = std::hypot(dr * hres, dc * hres);
            if (dist < 1e-3f) continue;
            float slope = std::fabs(zn - z) / dist;
            if (slope > max_slope) max_slope = slope;
          }
        }

        // 平滑滤波: 连续多帧都是障碍才输出障碍, 单帧抖动忽略
        if (max_slope > max_slope_) {
          obstacle_count_[idx] += 1;      // 本帧判定为障碍, 计数+1
        } else {
          obstacle_count_[idx] = 0;       // 本帧可通行, 清零
        }
        // 连续 3 帧都是障碍才真正标记(约 3 个点云周期)
        if (obstacle_count_[idx] >= 3) {
          traversability_[idx] = 100;  // 陡坡/台阶 → 障碍
        } else {
          traversability_[idx] = 0;    // 平地/缓坡/瞬时抖动 → 可通行
        }
      }
    }

    // 提取障碍点: 高于局部地面(z 基准 + obstacle_min_height)的凸起
    // 坡面点属于"地面", 不会高于局部地面太多, 因此被滤掉
    for (const auto & p : cloud->points) {
      if (std::isnan(p.x) || std::isnan(p.y) || std::isnan(p.z)) continue;
      int c = static_cast<int>((p.x - map_origin_x_) / resolution_);
      int r = static_cast<int>((p.y - map_origin_y_) / resolution_);
      if (c < 0 || c >= cols_ || r < 0 || r >= rows_) continue;
      int idx = r * cols_ + c;
      float z = heightmap_[idx];
      if (z == std::numeric_limits<float>::lowest()) continue;
      // 局部地面高度 ≈ 该格最低点; 简化为: 高度图中的低分位
      // 这里用"低于邻域中位数的点"作为地面基准的近似
      float ground_z = localGroundZ(r, c);
      if (p.z - ground_z > obstacle_min_height_) {
        obstacle_cloud_.push_back(p);
      }
    }

    map_ready_ = true;
  }

  // 局部地面高度: 取该格及其 3x3 邻域的最低 z
  float localGroundZ(int r, int c) const
  {
    float min_z = std::numeric_limits<float>::max();
    for (int dr = -1; dr <= 1; ++dr) {
      for (int dc = -1; dc <= 1; ++dc) {
        int rr = r + dr, cc = c + dc;
        if (rr < 0 || rr >= rows_ || cc < 0 || cc >= cols_) continue;
        float zn = heightmap_[rr * cols_ + cc];
        if (zn != std::numeric_limits<float>::lowest() && zn < min_z) min_z = zn;
      }
    }
    return (min_z == std::numeric_limits<float>::max()) ? 0.0f : min_z;
  }

  void publishMaps()
  {
    if (!map_ready_) return;

    // 可通行性图
    nav_msgs::msg::OccupancyGrid trav;
    trav.header.stamp = now();
    trav.header.frame_id = map_frame_;
    trav.info.resolution = resolution_;
    trav.info.width = cols_;
    trav.info.height = rows_;
    trav.info.origin.position.x = map_origin_x_;
    trav.info.origin.position.y = map_origin_y_;
    trav.data = traversability_;
    pub_trav_->publish(trav);

    // 障碍点云
    sensor_msgs::msg::PointCloud2 obs_msg;
    pcl::toROSMsg(obstacle_cloud_, obs_msg);
    obs_msg.header.stamp = now();
    obs_msg.header.frame_id = map_frame_;
    pub_obs_->publish(obs_msg);
  }

  std::string cloud_topic_;
  std::string map_frame_;
  double resolution_;
  double map_width_, map_height_;
  double max_range_;
  double max_slope_;
  double obstacle_min_height_;
  double z_ground_offset_;
  int cols_, rows_;
  double map_origin_x_ = -20.0;   // 地图原点(固定, 以车初始位置附近为中心)
  double map_origin_y_ = -20.0;
  double map_center_x_ = 0.0;
  double map_center_y_ = 0.0;

  std::vector<float> heightmap_;
  std::vector<int8_t> traversability_;
  std::vector<int> obstacle_count_;     // 连续障碍计数(平滑滤波, 防闪烁)
  pcl::PointCloud<pcl::PointXYZ> obstacle_cloud_;
  bool map_ready_ = false;

  tf2_ros::Buffer tf_buffer_;
  tf2_ros::TransformListener tf_listener_;
  rclcpp::Subscription<sensor_msgs::msg::PointCloud2>::SharedPtr sub_;
  rclcpp::Publisher<nav_msgs::msg::OccupancyGrid>::SharedPtr pub_trav_;
  rclcpp::Publisher<sensor_msgs::msg::PointCloud2>::SharedPtr pub_obs_;
  rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TerrainNode>());
  rclcpp::shutdown();
  return 0;
}
