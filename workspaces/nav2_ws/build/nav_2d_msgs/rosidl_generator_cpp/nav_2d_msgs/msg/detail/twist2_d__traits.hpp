// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav_2d_msgs:msg/Twist2D.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav_2d_msgs/msg/twist2_d.hpp"


#ifndef NAV_2D_MSGS__MSG__DETAIL__TWIST2_D__TRAITS_HPP_
#define NAV_2D_MSGS__MSG__DETAIL__TWIST2_D__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav_2d_msgs/msg/detail/twist2_d__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace nav_2d_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Twist2D & msg,
  std::ostream & out)
{
  out << "{";
  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: theta
  {
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Twist2D & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: theta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Twist2D & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav_2d_msgs::msg::Twist2D>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).x,
    std::forward<T>(msg).y,
    std::forward<T>(msg).theta);
}

}  // namespace msg

}  // namespace nav_2d_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav_2d_msgs::msg::Twist2D>()
{
  return "nav_2d_msgs::msg::Twist2D";
}

template<>
constexpr const char * name<nav_2d_msgs::msg::Twist2D>()
{
  return "nav_2d_msgs/msg/Twist2D";
}

template<>
struct has_fixed_size<nav_2d_msgs::msg::Twist2D>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<nav_2d_msgs::msg::Twist2D>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<nav_2d_msgs::msg::Twist2D>
  : std::true_type {};

template<>
struct MessageTraits<nav_2d_msgs::msg::Twist2D>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "x",
    "y",
    "theta",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV_2D_MSGS__MSG__DETAIL__TWIST2_D__TRAITS_HPP_
