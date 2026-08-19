# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target nav_2d_msgs::nav_2d_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${nav_2d_msgs_TARGETS}.
if(nav_2d_msgs_TARGETS AND NOT TARGET nav_2d_msgs::nav_2d_msgs)
  add_library(nav_2d_msgs::nav_2d_msgs INTERFACE IMPORTED)
  set_target_properties(nav_2d_msgs::nav_2d_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${nav_2d_msgs_TARGETS}")
endif()
