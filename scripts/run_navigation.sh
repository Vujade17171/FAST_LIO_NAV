#!/bin/bash
# ============================================================
# FAST_LIO_NAV 一键启动脚本
# 按依赖顺序启动: 雷达 → FAST-LIO → TF桥 → 地形 → Nav2 → RViz
# 每个节点一个独立 screen 会话, 可用 screen -r 查看
# 用法: bash run_navigation.sh
# ============================================================

WS=/home/vujade17171/prj/FAST_LIO_NAV/workspaces/ws_livox
NAV2_WS=/home/vujade17171/prj/FAST_LIO_NAV/workspaces/nav2_ws
SETUP="source /opt/ros/lyrical/setup.bash && source $WS/install/setup.bash && source $NAV2_WS/install/setup.bash"

# screen 会话目录(系统 /run/screen 只读)
export SCREENDIR=$HOME/.screen
mkdir -p "$SCREENDIR" && chmod 700 "$SCREENDIR"

# 串口设备名(插上 USB-TTL 后改这里, 或运行时传参)
SERIAL_PORT=${1:-/dev/ttyUSB0}

echo "=== 停止旧会话 ==="
for s in 1-livox 2-fastlio 3-tfbridge 4-terrain 5-base 6-nav2 7-rviz; do
  screen -S "$s" -X quit 2>/dev/null
done
sleep 2

echo "=== [1/6] 启动雷达驱动 ==="
screen -dmS 1-livox bash -c "$SETUP && ros2 launch livox_ros_driver2 msg_MID360_launch.py; exec bash"
echo "  等待 8 秒让雷达出数据..."
sleep 8

echo "=== [2/6] 启动 FAST-LIO(定位) ==="
screen -dmS 2-fastlio bash -c "$SETUP && ros2 launch fast_lio mapping.launch.py rviz:=false config_file:=mid360.yaml; exec bash"
echo "  等待 10 秒让 FAST-LIO 初始化..."
sleep 10

echo "=== [3/6] 启动 TF 桥 ==="
screen -dmS 3-tfbridge bash -c "$SETUP && ros2 run fastlio_tf_bridge tf_bridge_node; exec bash"
sleep 2

echo "=== [4/6] 跳过地形感知(静态地图模式, 不需要实时算图) ==="
sleep 1

echo "=== [5/6] 启动 Nav2(含 map_server 加载静态地图) ==="
screen -dmS 6-nav2 bash -c "$SETUP && ros2 launch nav2_config navigation.launch.py; exec bash"
echo "  等待 15 秒让 Nav2 全部激活..."
sleep 15

echo "=== [6/6] 启动 RViz(发目标点) ==="
screen -dmS 7-rviz bash -c "$SETUP && ros2 run rviz2 rviz2 -d $WS/src/nav2_config/rviz/nav2.rviz; exec bash"
sleep 3

echo ""
echo "=========================================="
echo "✅ 全部启动完成! 共 6 个 screen 会话:"
screen -ls | grep -E "1-livox|2-fastlio|3-tfbridge|4-terrain|6-nav2|7-rviz"
echo ""
echo "查看某节点日志:  screen -r 6-nav2   (退出: Ctrl+A 再按 D)"
echo "发目标点:        RViz 窗口选 Goal 工具, 地图上点目标点"
echo "停止全部:        bash $WS/../../scripts/stop_navigation.sh"
echo ""
echo "⚠️ 底盘串口未启动(未插 USB-TTL)。插上后执行:"
echo "   ros2 run robot_base_node robot_base_node --ros-args -p serial_port:=$SERIAL_PORT"
echo "=========================================="
