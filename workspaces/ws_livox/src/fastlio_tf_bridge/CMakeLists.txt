cmake_minimum_required(VERSION 3.8)
project(fastlio_tf_bridge)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2 REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(tf_bridge_node src/tf_bridge_node.cpp)
target_compile_features(tf_bridge_node PUBLIC cxx_std_17)
target_include_directories(tf_bridge_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_link_libraries(tf_bridge_node
  rclcpp::rclcpp
  nav_msgs::nav_msgs__rosidl_typesupport_cpp
  tf2_ros::tf2_ros
  geometry_msgs::geometry_msgs__rosidl_typesupport_cpp)

install(TARGETS tf_bridge_node
  DESTINATION lib/${PROJECT_NAME})

ament_package()
