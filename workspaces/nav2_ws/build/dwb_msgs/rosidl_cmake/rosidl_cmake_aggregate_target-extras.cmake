# generated from rosidl_cmake/cmake/rosidl_cmake_aggregate_target-extras.cmake.in

# Create a convenience aggregate target dwb_msgs::dwb_msgs
# that links all generated interface targets, so downstream packages can use
# a single modern CMake target name instead of ${dwb_msgs_TARGETS}.
if(dwb_msgs_TARGETS AND NOT TARGET dwb_msgs::dwb_msgs)
  add_library(dwb_msgs::dwb_msgs INTERFACE IMPORTED)
  set_target_properties(dwb_msgs::dwb_msgs PROPERTIES
    INTERFACE_LINK_LIBRARIES "${dwb_msgs_TARGETS}")
endif()
