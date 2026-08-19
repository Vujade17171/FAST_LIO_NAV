// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/CollisionMonitorState.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/collision_monitor_state.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__COLLISION_MONITOR_STATE__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__COLLISION_MONITOR_STATE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/collision_monitor_state__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CollisionMonitorState & msg,
  std::ostream & out)
{
  out << "{";
  // member: action_type
  {
    out << "action_type: ";
    rosidl_generator_traits::value_to_yaml(msg.action_type, out);
    out << ", ";
  }

  // member: polygon_name
  {
    out << "polygon_name: ";
    rosidl_generator_traits::value_to_yaml(msg.polygon_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CollisionMonitorState & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: action_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "action_type: ";
    rosidl_generator_traits::value_to_yaml(msg.action_type, out);
    out << "\n";
  }

  // member: polygon_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "polygon_name: ";
    rosidl_generator_traits::value_to_yaml(msg.polygon_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CollisionMonitorState & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::CollisionMonitorState>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).action_type,
    std::forward<T>(msg).polygon_name);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::CollisionMonitorState>()
{
  return "nav2_msgs::msg::CollisionMonitorState";
}

template<>
constexpr const char * name<nav2_msgs::msg::CollisionMonitorState>()
{
  return "nav2_msgs/msg/CollisionMonitorState";
}

template<>
struct has_fixed_size<nav2_msgs::msg::CollisionMonitorState>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::msg::CollisionMonitorState>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::msg::CollisionMonitorState>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::CollisionMonitorState>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "action_type",
    "polygon_name",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__COLLISION_MONITOR_STATE__TRAITS_HPP_
