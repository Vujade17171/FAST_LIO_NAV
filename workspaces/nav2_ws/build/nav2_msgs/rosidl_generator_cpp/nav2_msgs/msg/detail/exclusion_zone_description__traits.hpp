// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/ExclusionZoneDescription.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/exclusion_zone_description.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/exclusion_zone_description__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'points'
#include "geometry_msgs/msg/detail/point32__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const ExclusionZoneDescription & msg,
  std::ostream & out)
{
  out << "{";
  // member: zone_name
  {
    out << "zone_name: ";
    rosidl_generator_traits::value_to_yaml(msg.zone_name, out);
    out << ", ";
  }

  // member: type
  {
    out << "type: ";
    rosidl_generator_traits::value_to_yaml(msg.type, out);
    out << ", ";
  }

  // member: frame_id
  {
    out << "frame_id: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_id, out);
    out << ", ";
  }

  // member: points
  {
    if (msg.points.size() == 0) {
      out << "points: []";
    } else {
      out << "points: [";
      size_t pending_items = msg.points.size();
      for (auto item : msg.points) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: radius
  {
    out << "radius: ";
    rosidl_generator_traits::value_to_yaml(msg.radius, out);
    out << ", ";
  }

  // member: min_height
  {
    out << "min_height: ";
    rosidl_generator_traits::value_to_yaml(msg.min_height, out);
    out << ", ";
  }

  // member: max_height
  {
    out << "max_height: ";
    rosidl_generator_traits::value_to_yaml(msg.max_height, out);
    out << ", ";
  }

  // member: enabled
  {
    out << "enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.enabled, out);
    out << ", ";
  }

  // member: visualize
  {
    out << "visualize: ";
    rosidl_generator_traits::value_to_yaml(msg.visualize, out);
    out << ", ";
  }

  // member: frame_hold_timeout
  {
    out << "frame_hold_timeout: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_hold_timeout, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ExclusionZoneDescription & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: zone_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "zone_name: ";
    rosidl_generator_traits::value_to_yaml(msg.zone_name, out);
    out << "\n";
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

  // member: frame_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "frame_id: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_id, out);
    out << "\n";
  }

  // member: points
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.points.size() == 0) {
      out << "points: []\n";
    } else {
      out << "points:\n";
      for (auto item : msg.points) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: radius
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "radius: ";
    rosidl_generator_traits::value_to_yaml(msg.radius, out);
    out << "\n";
  }

  // member: min_height
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "min_height: ";
    rosidl_generator_traits::value_to_yaml(msg.min_height, out);
    out << "\n";
  }

  // member: max_height
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_height: ";
    rosidl_generator_traits::value_to_yaml(msg.max_height, out);
    out << "\n";
  }

  // member: enabled
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "enabled: ";
    rosidl_generator_traits::value_to_yaml(msg.enabled, out);
    out << "\n";
  }

  // member: visualize
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "visualize: ";
    rosidl_generator_traits::value_to_yaml(msg.visualize, out);
    out << "\n";
  }

  // member: frame_hold_timeout
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "frame_hold_timeout: ";
    rosidl_generator_traits::value_to_yaml(msg.frame_hold_timeout, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ExclusionZoneDescription & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::ExclusionZoneDescription>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).zone_name,
    std::forward<T>(msg).type,
    std::forward<T>(msg).frame_id,
    std::forward<T>(msg).points,
    std::forward<T>(msg).radius,
    std::forward<T>(msg).min_height,
    std::forward<T>(msg).max_height,
    std::forward<T>(msg).enabled,
    std::forward<T>(msg).visualize,
    std::forward<T>(msg).frame_hold_timeout);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::ExclusionZoneDescription>()
{
  return "nav2_msgs::msg::ExclusionZoneDescription";
}

template<>
constexpr const char * name<nav2_msgs::msg::ExclusionZoneDescription>()
{
  return "nav2_msgs/msg/ExclusionZoneDescription";
}

template<>
struct has_fixed_size<nav2_msgs::msg::ExclusionZoneDescription>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::msg::ExclusionZoneDescription>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::msg::ExclusionZoneDescription>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::ExclusionZoneDescription>
{
  static constexpr std::size_t member_count = 10;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "zone_name",
    "type",
    "frame_id",
    "points",
    "radius",
    "min_height",
    "max_height",
    "enabled",
    "visualize",
    "frame_hold_timeout",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__TRAITS_HPP_
