#!/bin/bash
# ============================================================
# FAST_LIO_NAV 一键停止脚本
# 用法: bash stop_navigation.sh
# ============================================================
export SCREENDIR=$HOME/.screen
mkdir -p "$SCREENDIR" && chmod 700 "$SCREENDIR"

echo "正在停止所有导航会话..."
for s in 1-livox 2-fastlio 3-tfbridge 4-terrain 5-base 6-nav2 7-rviz; do
  screen -S "$s" -X quit 2>/dev/null && echo "  已停止 $s"
done
sleep 1

echo "清理残留进程..."
pkill -f "livox_ros_driver2_node" 2>/dev/null
pkill -f "fastlio_mapping" 2>/dev/null
pkill -f "tf_bridge_node" 2>/dev/null
pkill -f "terrain_node" 2>/dev/null
pkill -f "robot_base_node" 2>/dev/null
pkill -f "navigation.launch.py" 2>/dev/null
pkill -f "rviz2" 2>/dev/null
sleep 1

echo "✅ 全部停止"
