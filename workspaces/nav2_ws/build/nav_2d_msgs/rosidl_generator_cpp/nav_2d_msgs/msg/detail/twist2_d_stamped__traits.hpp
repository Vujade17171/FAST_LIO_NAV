// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav_2d_msgs:msg/Twist2DStamped.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav_2d_msgs/msg/twist2_d_stamped.hpp"


#ifndef NAV_2D_MSGS__MSG__DETAIL__TWIST2_D_STAMPED__TRAITS_HPP_
#define NAV_2D_MSGS__MSG__DETAIL__TWIST2_D_STAMPED__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav_2d_msgs/msg/detail/twist2_d_stamped__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'velocity'
#include "nav_2d_msgs/msg/detail/twist2_d__traits.hpp"

namespace nav_2d_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Twist2DStamped & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: velocity
  {
    out << "velocity: ";
    to_flow_style_yaml(msg.velocity, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Twist2DStamped & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity:\n";
    to_block_style_yaml(msg.velocity, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Twist2DStamped & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav_2d_msgs::msg::Twist2DStamped>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).velocity);
}

}  // namespace msg

}  // namespace nav_2d_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav_2d_msgs::msg::Twist2DStamped>()
{
  return "nav_2d_msgs::msg::Twist2DStamped";
}

template<>
constexpr const char * name<nav_2d_msgs::msg::Twist2DStamped>()
{
  return "nav_2d_msgs/msg/Twist2DStamped";
}

template<>
struct has_fixed_size<nav_2d_msgs::msg::Twist2DStamped>
  : std::integral_constant<bool, has_fixed_size<nav_2d_msgs::msg::Twist2D>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<nav_2d_msgs::msg::Twist2DStamped>
  : std::integral_constant<bool, has_bounded_size<nav_2d_msgs::msg::Twist2D>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<nav_2d_msgs::msg::Twist2DStamped>
  : std::true_type {};

template<>
struct MessageTraits<nav_2d_msgs::msg::Twist2DStamped>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "velocity",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV_2D_MSGS__MSG__DETAIL__TWIST2_D_STAMPED__TRAITS_HPP_
