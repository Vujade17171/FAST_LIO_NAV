#!/bin/bash
# ============================================================
# FAST_LIO_NAV 一键编译脚本
# 编译: ws_livox 4 个自定义包 + nav2_ws 源码 Nav2
# 用法: bash build_all.sh
# ============================================================
set -e

source /opt/ros/lyrical/setup.bash

echo "===== [1/2] 编译自定义包 (ws_livox) ====="
cd /home/vujade17171/prj/FAST_LIO_NAV/workspaces/ws_livox
colcon build --packages-select \
  fastlio_tf_bridge robot_base_node terrain_node nav2_config \
  --symlink-install

echo "===== [2/2] 编译 Nav2 源码包 (nav2_ws, 若已编译会跳过) ====="
cd /home/vujade17171/prj/FAST_LIO_NAV/workspaces/nav2_ws
colcon build --packages-select \
  nav2_msgs nav2_common nav2_util nav2_voxel_grid nav2_ros_common nav2_core \
  nav2_costmap_2d nav2_navfn_planner nav2_planner nav2_controller \
  nav2_dwb_controller nav2_behavior_tree nav2_behaviors nav2_bt_navigator \
  nav2_smoother nav2_velocity_smoother nav2_collision_monitor \
  nav2_amcl nav2_map_server nav2_lifecycle_manager \
  --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF

echo ""
echo "✅ 全部编译完成!"
echo "运行导航请使用: bash run_navigation.sh"
