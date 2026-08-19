// fastlio_tf_bridge: 把 FAST-LIO 的 /Odometry (camera_init->body) 转成
// Nav2 需要的 TF 树: map -> odom -> base_link
//
// 阶段1: map->odom 为静态恒等(FAST-LIO 即定位,无全局定位器)
//        odom->base_link = FAST-LIO 位姿
// 阶段2: 接入全局定位后,map->odom 由定位漂移估计更新(本节点只发 odom->base_link)

#include <memory>
#include <string>

#include <rclcpp/rclcpp.hpp>
#include <nav_msgs/msg/odometry.hpp>
#include <geometry_msgs/msg/transform_stamped.hpp>
#include <tf2_ros/transform_broadcaster.h>
#include <tf2_ros/static_transform_broadcaster.h>

class TfBridgeNode : public rclcpp::Node
{
public:
  TfBridgeNode() : Node("fastlio_tf_bridge")
  {
    declare_parameter<std::string>("odom_topic", "/Odometry");
    declare_parameter<std::string>("odom_frame", "odom");
    declare_parameter<std::string>("base_frame", "base_link");
    declare_parameter<std::string>("map_frame", "map");
    declare_parameter<bool>("publish_map_odom_static", true);

    odom_topic_ = get_parameter("odom_topic").as_string();
    odom_frame_ = get_parameter("odom_frame").as_string();
    base_frame_ = get_parameter("base_frame").as_string();
    map_frame_ = get_parameter("map_frame").as_string();

    tf_broadcaster_ = std::make_unique<tf2_ros::TransformBroadcaster>(this);

    // 静态 map->odom 恒等(阶段1)
    if (get_parameter("publish_map_odom_static").as_bool()) {
      static_broadcaster_ = std::make_unique<tf2_ros::StaticTransformBroadcaster>(this);
      geometry_msgs::msg::TransformStamped ts;
      ts.header.stamp = now();
      ts.header.frame_id = map_frame_;
      ts.child_frame_id = odom_frame_;
      ts.transform.rotation.w = 1.0;
      static_broadcaster_->sendTransform(ts);
      RCLCPP_INFO(get_logger(), "Static TF: %s -> %s (identity)", map_frame_.c_str(), odom_frame_.c_str());
    }

    sub_ = create_subscription<nav_msgs::msg::Odometry>(
      odom_topic_, 10,
      [this](const nav_msgs::msg::Odometry::SharedPtr msg) { odomCallback(msg); });

    RCLCPP_INFO(get_logger(), "Subscribing %s, publishing %s -> %s",
                odom_topic_.c_str(), odom_frame_.c_str(), base_frame_.c_str());
  }

private:
  void odomCallback(const nav_msgs::msg::Odometry::SharedPtr msg)
  {
    geometry_msgs::msg::TransformStamped ts;
    ts.header.stamp = msg->header.stamp;
    ts.header.frame_id = odom_frame_;
    ts.child_frame_id = base_frame_;
    ts.transform.translation.x = msg->pose.pose.position.x;
    ts.transform.translation.y = msg->pose.pose.position.y;
    ts.transform.translation.z = msg->pose.pose.position.z;
    ts.transform.rotation = msg->pose.pose.orientation;
    tf_broadcaster_->sendTransform(ts);
  }

  std::string odom_topic_;
  std::string odom_frame_;
  std::string base_frame_;
  std::string map_frame_;
  std::unique_ptr<tf2_ros::TransformBroadcaster> tf_broadcaster_;
  std::unique_ptr<tf2_ros::StaticTransformBroadcaster> static_broadcaster_;
  rclcpp::Subscription<nav_msgs::msg::Odometry>::SharedPtr sub_;
};

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<TfBridgeNode>());
  rclcpp::shutdown();
  return 0;
}
