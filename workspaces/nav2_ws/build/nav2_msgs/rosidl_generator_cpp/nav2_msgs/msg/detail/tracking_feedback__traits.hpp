// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/TrackingFeedback.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/tracking_feedback.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__TRACKING_FEEDBACK__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__TRACKING_FEEDBACK__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/tracking_feedback__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'robot_pose'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const TrackingFeedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: position_tracking_error
  {
    out << "position_tracking_error: ";
    rosidl_generator_traits::value_to_yaml(msg.position_tracking_error, out);
    out << ", ";
  }

  // member: heading_tracking_error
  {
    out << "heading_tracking_error: ";
    rosidl_generator_traits::value_to_yaml(msg.heading_tracking_error, out);
    out << ", ";
  }

  // member: current_path_index
  {
    out << "current_path_index: ";
    rosidl_generator_traits::value_to_yaml(msg.current_path_index, out);
    out << ", ";
  }

  // member: robot_pose
  {
    out << "robot_pose: ";
    to_flow_style_yaml(msg.robot_pose, out);
    out << ", ";
  }

  // member: distance_to_goal
  {
    out << "distance_to_goal: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_to_goal, out);
    out << ", ";
  }

  // member: speed
  {
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
    out << ", ";
  }

  // member: remaining_path_length
  {
    out << "remaining_path_length: ";
    rosidl_generator_traits::value_to_yaml(msg.remaining_path_length, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TrackingFeedback & msg,
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

  // member: position_tracking_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position_tracking_error: ";
    rosidl_generator_traits::value_to_yaml(msg.position_tracking_error, out);
    out << "\n";
  }

  // member: heading_tracking_error
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "heading_tracking_error: ";
    rosidl_generator_traits::value_to_yaml(msg.heading_tracking_error, out);
    out << "\n";
  }

  // member: current_path_index
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_path_index: ";
    rosidl_generator_traits::value_to_yaml(msg.current_path_index, out);
    out << "\n";
  }

  // member: robot_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "robot_pose:\n";
    to_block_style_yaml(msg.robot_pose, out, indentation + 2);
  }

  // member: distance_to_goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance_to_goal: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_to_goal, out);
    out << "\n";
  }

  // member: speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "speed: ";
    rosidl_generator_traits::value_to_yaml(msg.speed, out);
    out << "\n";
  }

  // member: remaining_path_length
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "remaining_path_length: ";
    rosidl_generator_traits::value_to_yaml(msg.remaining_path_length, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TrackingFeedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::TrackingFeedback>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).position_tracking_error,
    std::forward<T>(msg).heading_tracking_error,
    std::forward<T>(msg).current_path_index,
    std::forward<T>(msg).robot_pose,
    std::forward<T>(msg).distance_to_goal,
    std::forward<T>(msg).speed,
    std::forward<T>(msg).remaining_path_length);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::TrackingFeedback>()
{
  return "nav2_msgs::msg::TrackingFeedback";
}

template<>
constexpr const char * name<nav2_msgs::msg::TrackingFeedback>()
{
  return "nav2_msgs/msg/TrackingFeedback";
}

template<>
struct has_fixed_size<nav2_msgs::msg::TrackingFeedback>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::PoseStamped>::value && has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<nav2_msgs::msg::TrackingFeedback>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::PoseStamped>::value && has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<nav2_msgs::msg::TrackingFeedback>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::TrackingFeedback>
{
  static constexpr std::size_t member_count = 8;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "position_tracking_error",
    "heading_tracking_error",
    "current_path_index",
    "robot_pose",
    "distance_to_goal",
    "speed",
    "remaining_path_length",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__TRACKING_FEEDBACK__TRAITS_HPP_
