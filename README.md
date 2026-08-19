# FAST_LIO_NAV 工程汇总

> 小车 3D 导航完整工程: FAST-LIO 定位 + 地形感知(斜坡) + Nav2 导航 + 下位机串口对接
> 整理日期: 2026-08-19

---

## 一、工程结构

```
FAST_LIO_NAV/
├── README.md                    # 总说明
├── USAGE.md                     # 快速使用说明(启动/测试/参数)
├── my24th_robo_1/               # STM32 下位机工程(Keil)
├── workspaces/
│   ├── nav2_ws/                 # Nav2 源码编译工作区
│   └── ws_livox/                # FAST-LIO + 4 自定义包工作区
└── scripts/                     # 一键脚本
    ├── build_all.sh            # 编译所有包
    ├── run_navigation.sh       # 7 终端一键启动导航
    └── test_serial_frame.sh    # 串口联调: 手动发一帧速度指令
```

---

## 二、涉及的工作区(实际工程位置,勿移动)

| 路径 | 内容 | 说明 |
|---|---|---|
| `/home/vujade17171/prj/FAST_LIO_NAV/workspaces/ws_livox` | FAST-LIO + livox 驱动 + 4 自定义包 | 主工作区(路径被 CMake 硬编码) |
| `/home/vujade17171/prj/FAST_LIO_NAV/workspaces/nav2_ws` | Nav2 源码编译结果(lyrical 分支) | 源码在 `src/navigation2` |
| `/home/vujade17171/Livox-SDK2` | Livox SDK2 源码 | 用于编译静态 SDK |
| `/home/vujade17171/livox_sdk_install` | 编译好的 PIC 静态 SDK | 被 livox 驱动链接 |
| `/home/vujade17171/prj/FAST_LIO_NAV/my24th_robo_1` | STM32 下位机工程 | 已加入 Nav/ 目录的串口接收代码 |

**重要**: 工作区路径被 CMakeLists / yaml 硬编码, **不要移动**, 否则需同步改这些文件:
- `ws_livox/src/livox_ros_driver2/CMakeLists.txt` → `/home/vujade17171/livox_sdk_install/lib`
- `ws_livox/src/nav2_config/config/nav2_params.yaml` → `bt_search_directories` 绝对路径

---

## 三、系统架构

```
MID360雷达 → livox_ros_driver2 → /livox/lidar, /livox/imu
                                    ↓
FAST-LIO (fastlio_mapping) → /Odometry, /cloud_registered
                                    ↓
fastlio_tf_bridge → TF: map→odom→base_link (阶段1: map=odom 恒等)
                                    ↓
terrain_node → /traversability(可通行性图) + /obstacle_cloud(滤坡面障碍点云)
                                    ↓
Nav2 (controller DWB全向 + planner NavFn + bt_navigator)
                                    ↓ /cmd_vel
robot_base_node → 串口 18字节帧 → 下位机 USART1
                                    ↓
nav_receiver.c → speed_cmd → Chassis_task → 运动学 → PID → CAN → 电机
```

**斜坡处理**: 坡度≤10° → terrain_node 标可通行, 路径直接穿过; 坡度>10° → 障碍绕行。
**关键**: local costmap 用 `/obstacle_cloud`(已滤掉坡面点), 避免坡面被当成墙。

---

## 四、编译与运行

### 1. 环境(一次)
```bash
source /opt/ros/lyrical/setup.bash
source /home/vujade17171/prj/FAST_LIO_NAV/workspaces/ws_livox/install/setup.bash
source /home/vujade17171/prj/FAST_LIO_NAV/workspaces/nav2_ws/install/setup.bash   # 顺序: ws_livox 先, nav2_ws 后
```

### 2. 编译
```bash
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/build_all.sh
```

### 3. 下位机(Keil)
- 新建 `Nav/` 组, 加入 `Nav/nav_receiver.c`
- Include Paths 加 `../Nav`
- 编译烧录 STM32

### 4. 启动导航
```bash
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/run_navigation.sh
# 或手动分终端启动, 见 USAGE.md 第 2 节
```

### 5. 串口联调(不启动 Nav2, 直接测下位机)
```bash
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/test_serial_frame.sh /dev/ttyUSB0 0.5 0 0
# 车应前进 0.5 m/s; 200ms 不发帧则自动急停
```

---

## 五、Nav2 源码编译背景(Lyrical 源缺失)

ROS 官方 Lyrical 源未发布 nav2 核心二进制包(只有 11 个基础包),
因此从源码编译了官方 `navigation2` 仓库的 **lyrical 分支**:

```bash
git clone -b lyrical https://github.com/ros-navigation/navigation2.git
# 依赖: apt 安装(behaviortree-cpp/rviz2/pcl 等, 已在系统装好)
# 编译: nav2_ws 内 colcon build (跳过测试)
```

**排除的包**: nav2_waypoint_follower(用了 Lyrical 已移除的 ament_target_dependencies 宏)、
nav2_rviz_plugins(依赖未编译的 nav2_route)。均非导航必需。

---

## 六、当前状态

| 项目 | 状态 |
|---|---|
| FAST-LIO 编译运行 | ✅ 已跑通(可出 PCD) |
| 下位机串口接收(nav_receiver) | ✅ 已写入工程(待 Keil 编译烧录) |
| 上位机 4 包编译 | ✅ 全部编译通过 |
| Nav2 源码编译(lyrical) | ✅ 21+14 包编译通过 |
| Nav2 全节点激活 | ✅ "Managed nodes are active" 验证通过 |
| 实车联调 | ⏳ 待插 USB-TTL 串口验证 |

---

## 七、待办(实车阶段)

- [ ] 插 USB-TTL, `ls /dev/ttyUSB*` 确认设备名
- [ ] `test_serial_frame.sh` 验证下位机响应
- [ ] 调 `nav2_params.yaml`: 车体半径/速度上限按实际
- [ ] terrain.yaml: max_slope_deg 按实测爬坡能力
- [ ] (可选)后续加抬升机构: 下位机加指令帧分支 + 上位机 step_lift_node

---

## 关键调试记录(2026-08-19 踩坑总结)

| 问题 | 根因 | 解决 |
|---|---|---|
| Nav2 "no map received" | static_layer 参数名是 `map_topic` 不是 `topic` | yaml 里用 `map_topic: /traversability` |
| 地图白底黑块(平地误判) | 坡度用最高点算, 噪点误判 | 放宽 max_slope_deg/obstacle_min_height |
| RViz 滚轮缩放无效 | TopDownOrtho 视图滚轮行为异常 | 改用 Orbit 视图 + Distance 30 |
| 地图闪烁 | terrain 5Hz 发布, Map 层频繁重绘 | publish_rate 降到 1Hz |
| gnome-terminal 不存在 | 纯命令行/远程环境 | 改用 screen 会话 |
| screen 无法启动 | /run/screen 只读 | SCREENDIR 指向 ~/.screen(已写 .bashrc) |
| Nav2 官方源缺包 | Lyrical 二进制未发布核心包 | 源码编译 lyrical 分支 |

## 一键启动

```bash
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/run_navigation.sh   # 启动
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/stop_navigation.sh  # 停止
screen -r 6-nav2                                                     # 看 Nav2 日志
```
