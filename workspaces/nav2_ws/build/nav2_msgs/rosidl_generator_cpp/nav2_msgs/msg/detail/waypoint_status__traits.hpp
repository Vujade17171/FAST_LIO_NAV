// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/WaypointStatus.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/waypoint_status.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__WAYPOINT_STATUS__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__WAYPOINT_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/waypoint_status__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'waypoint_pose'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const WaypointStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: waypoint_status
  {
    out << "waypoint_status: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_status, out);
    out << ", ";
  }

  // member: waypoint_index
  {
    out << "waypoint_index: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_index, out);
    out << ", ";
  }

  // member: waypoint_pose
  {
    out << "waypoint_pose: ";
    to_flow_style_yaml(msg.waypoint_pose, out);
    out << ", ";
  }

  // member: error_code
  {
    out << "error_code: ";
    rosidl_generator_traits::value_to_yaml(msg.error_code, out);
    out << ", ";
  }

  // member: error_msg
  {
    out << "error_msg: ";
    rosidl_generator_traits::value_to_yaml(msg.error_msg, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const WaypointStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: waypoint_status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoint_status: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_status, out);
    out << "\n";
  }

  // member: waypoint_index
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoint_index: ";
    rosidl_generator_traits::value_to_yaml(msg.waypoint_index, out);
    out << "\n";
  }

  // member: waypoint_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "waypoint_pose:\n";
    to_block_style_yaml(msg.waypoint_pose, out, indentation + 2);
  }

  // member: error_code
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error_code: ";
    rosidl_generator_traits::value_to_yaml(msg.error_code, out);
    out << "\n";
  }

  // member: error_msg
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "error_msg: ";
    rosidl_generator_traits::value_to_yaml(msg.error_msg, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const WaypointStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::WaypointStatus>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).waypoint_status,
    std::forward<T>(msg).waypoint_index,
    std::forward<T>(msg).waypoint_pose,
    std::forward<T>(msg).error_code,
    std::forward<T>(msg).error_msg);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::WaypointStatus>()
{
  return "nav2_msgs::msg::WaypointStatus";
}

template<>
constexpr const char * name<nav2_msgs::msg::WaypointStatus>()
{
  return "nav2_msgs/msg/WaypointStatus";
}

template<>
struct has_fixed_size<nav2_msgs::msg::WaypointStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::msg::WaypointStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::msg::WaypointStatus>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::WaypointStatus>
{
  static constexpr std::size_t member_count = 5;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "waypoint_status",
    "waypoint_index",
    "waypoint_pose",
    "error_code",
    "error_msg",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__WAYPOINT_STATUS__TRAITS_HPP_
