# FAST_LIO_NAV 快速使用说明

> 小车自动导航(FAST-LIO + 静态地图 + Nav2)。环境已配好(.bashrc 自动 source),开终端即用。

---

## 0. 建图与地图转换(首次使用必做)

导航需要一张静态地图。流程:推车建图 → 保存 PCD → 转成地图。

### 第1步:推车建图

启动雷达 + FAST-LIO(两个终端):

```bash
# 终端1: 雷达
ros2 launch livox_ros_driver2 msg_MID360_launch.py

# 终端2: FAST-LIO
ros2 launch fast_lio mapping.launch.py rviz:=false config_file:=mid360.yaml
```

然后**推着车走遍整个场地**(墙、障碍物、要走的坡都扫到)。走完后在终端2 按 **Ctrl+C** 停止 FAST-LIO,它会自动保存点云地图到:
```
/home/vujade17171/prj/FAST_LIO_NAV/test.pcd
```

### 第2步:PCD 转静态地图

```bash
python3 /home/vujade17171/prj/FAST_LIO_NAV/scripts/pcd_to_map.py \
  /home/vujade17171/prj/FAST_LIO_NAV/test.pcd \
  /home/vujade17171/prj/FAST_LIO_NAV/maps \
  0.1 10.0
```

参数说明:
- 第1个:输入的 PCD 文件路径
- 第2个:输出目录(生成 map.pgm + map.yaml)
- 第3个 `0.1`:分辨率(米/格),越小越精细
- 第4个 `10.0`:坡度阈值(度),**超过此角度的坡标记为障碍绕行,≤此值可通行**。按你车实际爬坡能力设(你确认过 ≤10°)

转换成功会输出:
```
maps/map.pgm     # 地图图像(白=可通行, 黑=障碍, 灰=未知)
maps/map.yaml    # 地图描述文件(Nav2 加载用)
```

### 第3步:启动导航

转换完成后,才执行第 1 节的一键启动。

---

## 1. 一键启动

```bash
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/run_navigation.sh
```

自动按顺序启动 5 个 screen 会话:
```
雷达 → FAST-LIO → TF桥 → Nav2(加载静态地图) → RViz
```

**查看状态**:
```bash
screen -ls                          # 看所有会话
screen -r 6-nav2                    # 进 Nav2 会话看日志(Ctrl+A 再按 D 退出)
```

**停止全部**:
```bash
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/stop_navigation.sh
```

**发目标点**:RViz 窗口顶部选 **Goal(2D Goal Pose)** 工具 → 地图上点目标位置 → 拖动设朝向 → 松开。

---

## 2. 逐个终端启动(备选,排障时用)

| 终端 | 命令 |
|---|---|
| 1 | `ros2 launch livox_ros_driver2 msg_MID360_launch.py` |
| 2 | `ros2 launch fast_lio mapping.launch.py rviz:=false config_file:=mid360.yaml` |
| 3 | `ros2 run fastlio_tf_bridge tf_bridge_node` |
| 4 | `ros2 launch nav2_config navigation.launch.py` |
| 5 | `ros2 run rviz2 rviz2 -d ~/prj/FAST_LIO_NAV/workspaces/ws_livox/src/nav2_config/rviz/nav2.rviz` |

> 每个终端先 source 环境(已在 .bashrc,新终端自动有)。启动顺序:1→2(等点云)→3→4→5。

---

## 3. 底盘串口(让车真动)

**接线**:上位机 USB → USB-TTL → 下位机 USART1(PA9/PA10,共地)

**启动底盘节点**(串口名按实际):
```bash
ls /dev/ttyUSB*                    # 确认设备名
ros2 run robot_base_node robot_base_node --ros-args -p serial_port:=/dev/ttyUSB0
```

**测试底盘**(不启动导航, 发一帧速度):
```bash
bash /home/vujade17171/prj/FAST_LIO_NAV/scripts/test_serial_frame.sh /dev/ttyUSB0 0.5 0 0
# 车应前进 0.5 m/s(发一帧后 200ms 急停属正常)
```

---

## 4. 修改参数方法

### 4.1 改什么、在哪改

| 要改 | 文件 |
|---|---|
| 车的半径/速度/膨胀 | `~/prj/FAST_LIO_NAV/workspaces/ws_livox/src/nav2_config/config/nav2_params.yaml` |
| 坡度阈值/障碍高度 | `~/prj/FAST_LIO_NAV/workspaces/ws_livox/src/terrain_node/config/terrain.yaml` |
| 串口设备名 | 启动底盘节点时用 `-p serial_port:=...` 指定 |

### 4.2 修改步骤

```bash
nano ~/prj/FAST_LIO_NAV/workspaces/ws_livox/src/nav2_config/config/nav2_params.yaml
# 保存: Ctrl+O 回车, 退出: Ctrl+X
```

**改完只需重启对应节点,不用重新编译**(symlink-install 已生效)。

| 改的文件 | 重启命令 |
|---|---|
| nav2_params.yaml | `ros2 launch nav2_config navigation.launch.py` |
| terrain.yaml | `ros2 run terrain_node terrain_node --ros-args --params-file ~/prj/FAST_LIO_NAV/workspaces/ws_livox/src/terrain_node/config/terrain.yaml` |

> 只有改 C++ 源码 / CMakeLists / package.xml 才需 `colcon build`。

### 4.3 最常改的参数

```yaml
# nav2_params.yaml
robot_radius: 0.35        # ★车半径m, 量车长L宽W, 填√((L/2)²+(W/2)²)再留余量(两处!)
max_vel_x: 1.0            # 最大速度 m/s
inflation_radius: 0.4     # 障碍膨胀 ≈车半径+0.1~0.2

# terrain.yaml
max_slope_deg: 25.0       # ★最大爬坡角(度), 超过绕行。当前25°是放宽值, 实测爬坡后调回10°左右
obstacle_min_height: 0.25 # 高于地面多少算障碍(当前0.25放宽值, 平地测试用)
publish_rate: 1.0         # 地图发布频率, 调低减少闪烁
```

---

## 5. 常见问题速查

| 现象 | 解决 |
|---|---|
| 串口打开失败 | `ls /dev/ttyUSB*` 确认设备名; `sudo usermod -aG dialout $USER` 后重登 |
| 车不动 | 用第 3 节 test_serial_frame.sh 单独测底盘 |
| 地图白底黑块 | 黑块=障碍(真实墙/桌椅正常); 平地误判就重新转换时把坡度阈值调大 |
| 地图为空 | 没建图/没转换; 先做第 0 节"建图与地图转换" |
| RViz 画面小 | 滚轮缩放; 按 R 键重置视角 |
| 导航起不来 | `ros2 run tf2_tools view_frames` 查 TF 树; 看各 screen 会话日志; 先 `stop_navigation.sh` 停干净再启 |
| "no map received" | 地图没生成或 map_server 没加载; 确认 `maps/map.yaml` 存在 |

---

## 6. 完整链路

```
MID360雷达 → livox驱动 → /livox/lidar+/livox/imu
                            ↓
                      FAST-LIO → /Odometry + /cloud_registered(建图)
                            ↓
                   TF桥 → map→odom→base_link
                            ↓
                  map_server → 加载静态地图 /map (由 PCD 离线转换)
                            ↓
                   Nav2 → 规划 + /cmd_vel
                            ↓
                   robot_base → 串口帧 → 下位机 → 电机
```
