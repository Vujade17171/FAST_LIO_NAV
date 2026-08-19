// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/RouteEdge.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/route_edge.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__ROUTE_EDGE__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__ROUTE_EDGE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/route_edge__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'start'
// Member 'end'
#include "geometry_msgs/msg/detail/point__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const RouteEdge & msg,
  std::ostream & out)
{
  out << "{";
  // member: edgeid
  {
    out << "edgeid: ";
    rosidl_generator_traits::value_to_yaml(msg.edgeid, out);
    out << ", ";
  }

  // member: start
  {
    out << "start: ";
    to_flow_style_yaml(msg.start, out);
    out << ", ";
  }

  // member: end
  {
    out << "end: ";
    to_flow_style_yaml(msg.end, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const RouteEdge & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: edgeid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "edgeid: ";
    rosidl_generator_traits::value_to_yaml(msg.edgeid, out);
    out << "\n";
  }

  // member: start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start:\n";
    to_block_style_yaml(msg.start, out, indentation + 2);
  }

  // member: end
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "end:\n";
    to_block_style_yaml(msg.end, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const RouteEdge & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::RouteEdge>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).edgeid,
    std::forward<T>(msg).start,
    std::forward<T>(msg).end);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::RouteEdge>()
{
  return "nav2_msgs::msg::RouteEdge";
}

template<>
constexpr const char * name<nav2_msgs::msg::RouteEdge>()
{
  return "nav2_msgs/msg/RouteEdge";
}

template<>
struct has_fixed_size<nav2_msgs::msg::RouteEdge>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::Point>::value> {};

template<>
struct has_bounded_size<nav2_msgs::msg::RouteEdge>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::Point>::value> {};

template<>
struct is_message<nav2_msgs::msg::RouteEdge>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::RouteEdge>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "edgeid",
    "start",
    "end",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__ROUTE_EDGE__TRAITS_HPP_
