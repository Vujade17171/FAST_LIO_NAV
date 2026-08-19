cmake_minimum_required(VERSION 3.8)
project(robot_base_node)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(robot_base_node src/robot_base_node.cpp)
target_compile_features(robot_base_node PUBLIC cxx_std_17)
target_link_libraries(robot_base_node
  rclcpp::rclcpp
  geometry_msgs::geometry_msgs__rosidl_typesupport_cpp)

install(TARGETS robot_base_node
  DESTINATION lib/${PROJECT_NAME})

ament_package()
