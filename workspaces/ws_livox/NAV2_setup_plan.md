# 小车 Nav2 自动导航接入方案(3D 定位 + 地形感知,含斜坡/台阶/抬升)

> 目标:小车(单片机下位机:Vx/Vy/角速度 + 抬升指令)自动导航到目标点。
> 定位:**lidar_localization_ros2(NDT/GICP 匹配 .pcd 地图)为主,FAST-LIO 里程计为高频预测**。
> 地形:缓坡(≤10°)可通行;台阶 ≤10cm 用抬升机构(停车→抬升→越过→放下);更高台阶判为障碍绕行。
> ROS 版本:Lyrical。

---

## 0. 方案选型结论(已调研 jie_3d_nav 与 lidar_localization_ros2)

| | jie_3d_nav | lidar_localization_ros2(选用) |
|---|---|---|
| 本质 | OctoMap 3D 规划+控制完整框架 | 纯 3D 定位(NDT/GICP 匹配 .pcd 地图) |
| 定位 | 强依赖 Odin 1 模组 | 独立,输出 map→base_link |
| 平台 | 面向 Humble + D1 机器狗 | Jazzy 为主,Humble 兼容,含 MID-360 launch |
| 你的场景 | 3D 绕行规划用不上,抬升/坡度逻辑还得自加 | 定位层替换干净,其余复用 Nav2+自写节点 |
| 结论 | 不选(包袱重、适配成本高) | ✅ 选它做定位层 |

**演进路径**:阶段1 可先用 FAST-LIO 位姿跑通整条链路(不装 lidar_localization),
阶段2 再加 lidar_localization_ros2 做全局定位消除漂移。

---

## 1. 总体架构

```
┌─────────────┐ /livox/lidar, /livox/imu  ┌──────────────────┐
│ MID360 雷达  │ ───────────────────────▶ │ livox_ros_driver2│
└─────────────┘                           └──────────────────┘
                                                │ /livox/lidar, /livox/imu
                                                ▼
┌──────────────────┐ /Odometry(camera_init→body)  ┌────────────────────────┐
│ fastlio_mapping  │ ───────────────────────────▶ │ pose_fusion_node (自定义E)│
│ (FAST-LIO,里程计) │  TF: camera_init→body        │ 高频里程计 + 全局定位融合 │
└────────┬─────────┘                               │ → 发布 odom→base_link    │
         │ /cloud_registered(实时)                └───────────┬────────────┘
         ▼                                                     │ TF: map→odom→base_link
┌─────────────────────────┐  /traversability(可通行性图)       ▼
│ terrain_node (自定义B)   │ ────────────────────────┐  ┌──────────────────────────────┐
│ 实时点云→2.5D坡度→分类    │                         │  │ Nav2 (nav2_bringup)          │
│ 缓坡✓/可越台阶◎/障碍✗    │ /step_markers           │  │ global: terrain+obstacle     │
└────────┬────────────────┘                         │  │ local: voxel 层              │
         │                                          │  │ planner: NavFn/Smac          │
         ▼                                          │  │ controller: DWB(全向)        │
┌─────────────────────────┐  ┌────────────────────┐ │  └──────────────┬───────────────┘
│ lidar_localization_ros2 │  │ step_lift_node (C) │ │                 │ /cmd_vel
│ NDT/GICP 匹配 .pcd 地图  │  │ 台阶检测→抬升时序   │ │                 ▼
│ 输出 map→base_link       │  │ 停车→抬升→越过→放下│ │  ┌──────────────────────────────┐
└───────────┬─────────────┘  └────────────────────┘ │  │ robot_base_node (自定义D)     │
            │ map→base_link(低频,全局校准)           │  │ /cmd_vel + 抬升指令→串口→单片机 │
            └───────────────▶ pose_fusion_node ─────┘  └──────────────────────────────┘
```

### 角色分工

| 节点 | 来源 | 职责 |
|---|---|---|
| fastlio_mapping | 已有(已跑通) | LiDAR-惯性里程计,高频(100Hz+)位姿 + 全局点云 |
| **lidar_localization_ros2** | [rsasaki0109/lidar_localization_ros2](https://github.com/rsasaki0109/lidar_localization_ros2)(新装) | NDT/GICP 把实时点云匹配到 PCD 地图,输出全局 `map→base_link`(10~20Hz),消除 FAST-LIO 漂移 |
| **pose_fusion_node** | 自写(包E) | 高频 FAST-LIO odom→base_link 与低频全局定位融合(简单加权/EKF),发布 Nav2 需要的 TF |
| terrain_node | 自写(包B) | 点云→2.5D 高度图→坡度分类→可通行性图 + 台阶标记 |
| step_lift_node | 自写(包C) | 检测前方可越台阶,编排 停车→抬升→越过→放下→恢复 |
| robot_base_node | 自写(包D) | /cmd_vel + 抬升指令 → 串口 → 单片机 |
| Nav2 | apt 安装 | 全局/局部代价地图、规划、DWB 全向控制 |

### TF 树

```
map ←──(lidar_localization_ros2 + pose_fusion,低频全局)── odom ←──(pose_fusion,高频)── base_link
  └── FAST-LIO camera_init→body 作为高频预测输入(在 pose_fusion_node 内转换)
```

> 阶段1(不装 lidar_localization):`map→odom` 恒等、`odom→base_link` = FAST-LIO 位姿(桥接节点)。
> 阶段2:加入全局定位后 `map→odom` 由定位漂移估计更新,`odom→base_link` 保持高频。

---

## 2. 地形感知节点 terrain_node(核心,同前版)

- 输入:`/cloud_registered`(FAST-LIO 全局点云)
- 输出:`/traversability`(OccupancyGrid)+ `/step_markers`(台阶位置/高度)+ 调试话题
- 分类规则(参数可调):
  - 坡度 ≤ 10° → 可通行(缓坡直接放进路径)
  - 邻域高度突变 3~10cm → **可越台阶**(标记,交 step_lift_node)
  - 高度差 > 10cm 或坡度 > 10° → 障碍
- 建议先用已存的 PCD 离线调阈值。

```yaml
terrain_node:
  ros__parameters:
    cloud_topic: /cloud_registered
    map_frame: map
    resolution: 0.1
    max_range: 30.0
    robot_radius: 0.35
    max_slope_deg: 10.0
    step_lift_max: 0.10
    step_lift_min: 0.03
    height_diff_threshold: 0.12
```

---

## 3. 抬升协调节点 step_lift_node

时序(停车→抬升→前进→放下→恢复):
1. terrain_node 发布可越台阶标记(前方 ~1m、路径走廊内)
2. step_lift_node:通知 Nav2 暂停 → 等车停稳 → 串口发抬升 → 低速直行(按前进距离判定越过)→ 停车 → 串口发放下 → 恢复 Nav2
3. 高度 >10cm 的台阶已标障碍,Nav2 自动绕行,不触发抬升

需你提供:抬升/放下串口指令格式;车长(判定已越过);触发距离。

---

## 4. Nav2 配置(同前版)

- global_costmap:terrain 可通行性图(static 层)+ obstacle 层(动态障碍,`min_obstacle_height: 0.12` 排除地面/坡面)+ inflation
- local_costmap:voxel 层全高度实时避障
- planner:NavFn(全向)或 SmacPlannerHybrid(有转弯半径约束时)
- controller:DWB,全向(Vx/Vy/w)

---

## 5. 包与文件清单(ws_livox/src)

| 包 | 内容 | 必写? |
|---|---|---|
| **A. fastlio_tf_bridge**(阶段1用) | 阶段1:FAST-LIO 位姿→odom→base_link + 静态 map→odom | ✅ 1 cpp |
| **E. pose_fusion_node**(阶段2用) | 高频里程计 + 低频全局定位融合 → TF | ✅ 1 cpp(阶段2) |
| **B. terrain_node** | 点云→坡度→可通行性图+台阶标记 | ✅ 核心 |
| **C. step_lift_node** | 台阶→抬升时序编排 | ✅ 1 cpp |
| **D. robot_base** | /cmd_vel+抬升→串口→单片机 | ✅ 1 cpp |
| **F. nav2_config** | nav2_params.yaml + launch + rviz | ✅ 纯配置 |
| **G. robot_description** | 最小 URDF(以后加) | ⏸ 后续 |

需要安装/编译:
```bash
# 系统包
sudo apt install -y ros-lyrical-nav2-bringup ros-lyrical-pybind11-vendor
# lidar_localization_ros2 及其依赖(源码编译)
cd ~/lidarloc_ws/src
git clone https://github.com/rsasaki0109/ndt_omp_ros2.git
git clone https://github.com/rsasaki0109/lidar_localization_ros2.git
# 按仓库 scripts/bootstrap_colcon_workspace.sh 编译(需在 Lyrical 验证)
```

---

## 6. 实施顺序

1. `sudo apt install -y ros-lyrical-nav2-bringup ros-lyrical-pybind11-vendor`
2. **阶段1(不依赖 lidar_localization)**:包A(桥)+F(Nav2 配置),平地跑通规划+cmd_vel
3. 包B(terrain_node):用已存 PCD 离线验证坡度/台阶/障碍分类
4. 实车验证缓坡:车沿缓坡路径走,不被坡面挡住
5. 包C+D:手动测抬升串口 → 自动触发
6. **阶段2**:编译安装 lidar_localization_ros2 + ndt_omp_ros2(验证 Lyrical 兼容)
7. 包E(pose_fusion):接入全局定位,长距离验证无漂移
8. 全链路:发目标点 → 绕高台阶 → 遇可越台阶停车抬升越过 → 到达

---

## 7. 待你确认/提供

- [ ] 抬升/放下串口指令格式(字节序列)
- [ ] 台阶"已越过"判定:默认位姿前进距离;有超声波/IMU 冲击检测更准
- [ ] 车体半径、最大速度/加速度、车长
- [ ] (以后)实测抬升最大高度,替换 10cm 阈值
- [ ] (阶段2)PCD 地图文件路径(已存于 FAST-LIO PCD/ 目录)

---

## 附录: Lyrical 源 Nav2 缺失的解决记录(2026-08-19)

**问题**: ROS 官方 Lyrical 源只发布了 11 个 nav2 基础包(nav2-msgs/common/
costmap-2d/util/voxel-grid/ros-common/simple-commander/system-tests/minimal-tb3/tb4-sim),
缺少 nav2-bringup、planner、controller、bt_navigator、recoveries、amcl、map_server
等全部核心导航包, `apt install ros-lyrical-nav2-bringup` 报"无法定位软件包"。

**解决**: 源码编译官方 lyrical 分支
```bash
mkdir -p ~/nav2_ws/src && cd ~/nav2_ws/src
git clone -b lyrical https://github.com/ros-navigation/navigation2.git
# apt 装第三方依赖(用户 sudo 执行)
sudo apt install -y ros-lyrical-behaviortree-cpp ros-lyrical-backward-ros \
  ros-lyrical-bondcpp ros-lyrical-angles ros-lyrical-nav-msgs \
  ros-lyrical-pluginlib ros-lyrical-rviz2 ros-lyrical-rviz-common \
  ros-lyrical-rviz-ogre-vendor ros-lyrical-xacro ros-lyrical-tf2-ros \
  ros-lyrical-tf2-geometry-msgs ros-lyrical-tf2-sensor-msgs \
  ros-lyrical-pcl-ros ros-lyrical-pcl-conversions \
  ros-lyrical-robot-state-publisher ros-lyrical-launch-ros \
  ros-lyrical-rclcpp-action ros-lyrical-diagnostic-msgs ros-lyrical-std-srvs \
  ros-lyrical-geographic-msgs ros-lyrical-diagnostic-updater \
  ros-lyrical-robot-localization libgraphicsmagick++1-dev uuid-dev qt6-scxml-dev
# 编译核心包(跳过测试; 排除 waypoint_follower[用已移除的宏] 和 rviz_plugins[依赖route])
cd ~/nav2_ws && source /opt/ros/lyrical/setup.bash
colcon build --packages-select \
  nav2_msgs nav2_common nav2_util nav2_voxel_grid nav2_ros_common nav2_core \
  nav2_costmap_2d nav2_navfn_planner nav2_planner nav2_controller \
  nav2_dwb_controller nav2_behavior_tree nav2_behaviors nav2_bt_navigator \
  nav2_smoother nav2_velocity_smoother nav2_collision_monitor \
  nav2_amcl nav2_map_server nav2_lifecycle_manager \
  --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF
```
**注意**: nav2_dwb_controller 是元包, 需先编译其子包
(nav_2d_msgs/dwb_msgs/nav_2d_utils/costmap_queue/dwb_core/dwb_critics/dwb_plugins),
colcon 依赖解析会自动处理, 若手动指定需全部列出。

**运行前 source**: `source ~/nav2_ws/install/setup.bash`(在 ws_livox 的 install 之后或之前都行, 无冲突)。
