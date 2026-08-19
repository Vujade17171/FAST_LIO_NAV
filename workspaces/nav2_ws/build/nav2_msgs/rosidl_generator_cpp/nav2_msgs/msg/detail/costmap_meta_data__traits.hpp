// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/CostmapMetaData.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/costmap_meta_data.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__COSTMAP_META_DATA__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__COSTMAP_META_DATA__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/costmap_meta_data__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'map_load_time'
// Member 'update_time'
#include "builtin_interfaces/msg/detail/time__traits.hpp"
// Member 'origin'
#include "geometry_msgs/msg/detail/pose__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CostmapMetaData & msg,
  std::ostream & out)
{
  out << "{";
  // member: map_load_time
  {
    out << "map_load_time: ";
    to_flow_style_yaml(msg.map_load_time, out);
    out << ", ";
  }

  // member: update_time
  {
    out << "update_time: ";
    to_flow_style_yaml(msg.update_time, out);
    out << ", ";
  }

  // member: layer
  {
    out << "layer: ";
    rosidl_generator_traits::value_to_yaml(msg.layer, out);
    out << ", ";
  }

  // member: resolution
  {
    out << "resolution: ";
    rosidl_generator_traits::value_to_yaml(msg.resolution, out);
    out << ", ";
  }

  // member: size_x
  {
    out << "size_x: ";
    rosidl_generator_traits::value_to_yaml(msg.size_x, out);
    out << ", ";
  }

  // member: size_y
  {
    out << "size_y: ";
    rosidl_generator_traits::value_to_yaml(msg.size_y, out);
    out << ", ";
  }

  // member: origin
  {
    out << "origin: ";
    to_flow_style_yaml(msg.origin, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CostmapMetaData & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: map_load_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "map_load_time:\n";
    to_block_style_yaml(msg.map_load_time, out, indentation + 2);
  }

  // member: update_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "update_time:\n";
    to_block_style_yaml(msg.update_time, out, indentation + 2);
  }

  // member: layer
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "layer: ";
    rosidl_generator_traits::value_to_yaml(msg.layer, out);
    out << "\n";
  }

  // member: resolution
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "resolution: ";
    rosidl_generator_traits::value_to_yaml(msg.resolution, out);
    out << "\n";
  }

  // member: size_x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "size_x: ";
    rosidl_generator_traits::value_to_yaml(msg.size_x, out);
    out << "\n";
  }

  // member: size_y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "size_y: ";
    rosidl_generator_traits::value_to_yaml(msg.size_y, out);
    out << "\n";
  }

  // member: origin
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "origin:\n";
    to_block_style_yaml(msg.origin, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CostmapMetaData & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::CostmapMetaData>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).map_load_time,
    std::forward<T>(msg).update_time,
    std::forward<T>(msg).layer,
    std::forward<T>(msg).resolution,
    std::forward<T>(msg).size_x,
    std::forward<T>(msg).size_y,
    std::forward<T>(msg).origin);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::CostmapMetaData>()
{
  return "nav2_msgs::msg::CostmapMetaData";
}

template<>
constexpr const char * name<nav2_msgs::msg::CostmapMetaData>()
{
  return "nav2_msgs/msg/CostmapMetaData";
}

template<>
struct has_fixed_size<nav2_msgs::msg::CostmapMetaData>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::msg::CostmapMetaData>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::msg::CostmapMetaData>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::CostmapMetaData>
{
  static constexpr std::size_t member_count = 7;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "map_load_time",
    "update_time",
    "layer",
    "resolution",
    "size_x",
    "size_y",
    "origin",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__COSTMAP_META_DATA__TRAITS_HPP_
