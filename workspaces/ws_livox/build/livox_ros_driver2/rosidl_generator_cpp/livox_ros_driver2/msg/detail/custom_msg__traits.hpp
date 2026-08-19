// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from livox_ros_driver2:msg/CustomMsg.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "livox_ros_driver2/msg/custom_msg.hpp"


#ifndef LIVOX_ROS_DRIVER2__MSG__DETAIL__CUSTOM_MSG__TRAITS_HPP_
#define LIVOX_ROS_DRIVER2__MSG__DETAIL__CUSTOM_MSG__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "livox_ros_driver2/msg/detail/custom_msg__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'points'
#include "livox_ros_driver2/msg/detail/custom_point__traits.hpp"

namespace livox_ros_driver2
{

namespace msg
{

inline void to_flow_style_yaml(
  const CustomMsg & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: timebase
  {
    out << "timebase: ";
    rosidl_generator_traits::value_to_yaml(msg.timebase, out);
    out << ", ";
  }

  // member: point_num
  {
    out << "point_num: ";
    rosidl_generator_traits::value_to_yaml(msg.point_num, out);
    out << ", ";
  }

  // member: lidar_id
  {
    out << "lidar_id: ";
    rosidl_generator_traits::value_to_yaml(msg.lidar_id, out);
    out << ", ";
  }

  // member: rsvd
  {
    if (msg.rsvd.size() == 0) {
      out << "rsvd: []";
    } else {
      out << "rsvd: [";
      size_t pending_items = msg.rsvd.size();
      for (auto item : msg.rsvd) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
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
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CustomMsg & msg,
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

  // member: timebase
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timebase: ";
    rosidl_generator_traits::value_to_yaml(msg.timebase, out);
    out << "\n";
  }

  // member: point_num
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "point_num: ";
    rosidl_generator_traits::value_to_yaml(msg.point_num, out);
    out << "\n";
  }

  // member: lidar_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "lidar_id: ";
    rosidl_generator_traits::value_to_yaml(msg.lidar_id, out);
    out << "\n";
  }

  // member: rsvd
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.rsvd.size() == 0) {
      out << "rsvd: []\n";
    } else {
      out << "rsvd:\n";
      for (auto item : msg.rsvd) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CustomMsg & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, livox_ros_driver2::msg::CustomMsg>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).timebase,
    std::forward<T>(msg).point_num,
    std::forward<T>(msg).lidar_id,
    std::forward<T>(msg).rsvd,
    std::forward<T>(msg).points);
}

}  // namespace msg

}  // namespace livox_ros_driver2

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<livox_ros_driver2::msg::CustomMsg>()
{
  return "livox_ros_driver2::msg::CustomMsg";
}

template<>
constexpr const char * name<livox_ros_driver2::msg::CustomMsg>()
{
  return "livox_ros_driver2/msg/CustomMsg";
}

template<>
struct has_fixed_size<livox_ros_driver2::msg::CustomMsg>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<livox_ros_driver2::msg::CustomMsg>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<livox_ros_driver2::msg::CustomMsg>
  : std::true_type {};

template<>
struct MessageTraits<livox_ros_driver2::msg::CustomMsg>
{
  static constexpr std::size_t member_count = 6;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "timebase",
    "point_num",
    "lidar_id",
    "rsvd",
    "points",
  };
};

}  // namespace rosidl_generator_traits

#endif  // LIVOX_ROS_DRIVER2__MSG__DETAIL__CUSTOM_MSG__TRAITS_HPP_
