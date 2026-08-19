// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/CostmapFilterInfo.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/costmap_filter_info.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__COSTMAP_FILTER_INFO__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__COSTMAP_FILTER_INFO__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/costmap_filter_info__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CostmapFilterInfo & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: type
  {
    out << "type: ";
    rosidl_generator_traits::value_to_yaml(msg.type, out);
    out << ", ";
  }

  // member: filter_mask_topic
  {
    out << "filter_mask_topic: ";
    rosidl_generator_traits::value_to_yaml(msg.filter_mask_topic, out);
    out << ", ";
  }

  // member: base
  {
    out << "base: ";
    rosidl_generator_traits::value_to_yaml(msg.base, out);
    out << ", ";
  }

  // member: multiplier
  {
    out << "multiplier: ";
    rosidl_generator_traits::value_to_yaml(msg.multiplier, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CostmapFilterInfo & msg,
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

  // member: type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "type: ";
    rosidl_generator_traits::value_to_yaml(msg.type, out);
    out << "\n";
  }

  // member: filter_mask_topic
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "filter_mask_topic: ";
    rosidl_generator_traits::value_to_yaml(msg.filter_mask_topic, out);
    out << "\n";
  }

  // member: base
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "base: ";
    rosidl_generator_traits::value_to_yaml(msg.base, out);
    out << "\n";
  }

  // member: multiplier
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "multiplier: ";
    rosidl_generator_traits::value_to_yaml(msg.multiplier, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CostmapFilterInfo & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::CostmapFilterInfo>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).type,
    std::forward<T>(msg).filter_mask_topic,
    std::forward<T>(msg).base,
    std::forward<T>(msg).multiplier);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::CostmapFilterInfo>()
{
  return "nav2_msgs::msg::CostmapFilterInfo";
}

template<>
constexpr const char * name<nav2_msgs::msg::CostmapFilterInfo>()
{
  return "nav2_msgs/msg/CostmapFilterInfo";
}

template<>
struct has_fixed_size<nav2_msgs::msg::CostmapFilterInfo>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::msg::CostmapFilterInfo>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::msg::CostmapFilterInfo>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::CostmapFilterInfo>
{
  static constexpr std::size_t member_count = 5;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "type",
    "filter_mask_topic",
    "base",
    "multiplier",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__COSTMAP_FILTER_INFO__TRAITS_HPP_
