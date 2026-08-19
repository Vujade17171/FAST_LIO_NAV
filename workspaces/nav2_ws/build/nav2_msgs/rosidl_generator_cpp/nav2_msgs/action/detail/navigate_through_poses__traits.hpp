// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:action/NavigateThroughPoses.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/action/navigate_through_poses.hpp"


#ifndef NAV2_MSGS__ACTION__DETAIL__NAVIGATE_THROUGH_POSES__TRAITS_HPP_
#define NAV2_MSGS__ACTION__DETAIL__NAVIGATE_THROUGH_POSES__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/action/detail/navigate_through_poses__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'poses'
#include "nav_msgs/msg/detail/goals__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: poses
  {
    out << "poses: ";
    to_flow_style_yaml(msg.poses, out);
    out << ", ";
  }

  // member: behavior_tree
  {
    out << "behavior_tree: ";
    rosidl_generator_traits::value_to_yaml(msg.behavior_tree, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NavigateThroughPoses_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: poses
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "poses:\n";
    to_block_style_yaml(msg.poses, out, indentation + 2);
  }

  // member: behavior_tree
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "behavior_tree: ";
    rosidl_generator_traits::value_to_yaml(msg.behavior_tree, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_Goal>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).poses,
    std::forward<T>(msg).behavior_tree);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_Goal>()
{
  return "nav2_msgs::action::NavigateThroughPoses_Goal";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_Goal>()
{
  return "nav2_msgs/action/NavigateThroughPoses_Goal";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_Goal>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_Goal>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_Goal>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_Goal>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "poses",
    "behavior_tree",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'waypoint_statuses'
#include "nav2_msgs/msg/detail/waypoint_status__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_Result & msg,
  std::ostream & out)
{
  out << "{";
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
    out << ", ";
  }

  // member: waypoint_statuses
  {
    if (msg.waypoint_statuses.size() == 0) {
      out << "waypoint_statuses: []";
    } else {
      out << "waypoint_statuses: [";
      size_t pending_items = msg.waypoint_statuses.size();
      for (auto item : msg.waypoint_statuses) {
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
  const NavigateThroughPoses_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
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

  // member: waypoint_statuses
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoint_statuses.size() == 0) {
      out << "waypoint_statuses: []\n";
    } else {
      out << "waypoint_statuses:\n";
      for (auto item : msg.waypoint_statuses) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_Result>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).error_code,
    std::forward<T>(msg).error_msg,
    std::forward<T>(msg).waypoint_statuses);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_Result>()
{
  return "nav2_msgs::action::NavigateThroughPoses_Result";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_Result>()
{
  return "nav2_msgs/action/NavigateThroughPoses_Result";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_Result>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_Result>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "error_code",
    "error_msg",
    "waypoint_statuses",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'current_pose'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"
// Member 'navigation_time'
// Member 'estimated_time_remaining'
#include "builtin_interfaces/msg/detail/duration__traits.hpp"
// Member 'waypoint_statuses'
// already included above
// #include "nav2_msgs/msg/detail/waypoint_status__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: current_pose
  {
    out << "current_pose: ";
    to_flow_style_yaml(msg.current_pose, out);
    out << ", ";
  }

  // member: navigation_time
  {
    out << "navigation_time: ";
    to_flow_style_yaml(msg.navigation_time, out);
    out << ", ";
  }

  // member: estimated_time_remaining
  {
    out << "estimated_time_remaining: ";
    to_flow_style_yaml(msg.estimated_time_remaining, out);
    out << ", ";
  }

  // member: number_of_recoveries
  {
    out << "number_of_recoveries: ";
    rosidl_generator_traits::value_to_yaml(msg.number_of_recoveries, out);
    out << ", ";
  }

  // member: distance_remaining
  {
    out << "distance_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_remaining, out);
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

  // member: number_of_poses_remaining
  {
    out << "number_of_poses_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.number_of_poses_remaining, out);
    out << ", ";
  }

  // member: waypoint_statuses
  {
    if (msg.waypoint_statuses.size() == 0) {
      out << "waypoint_statuses: []";
    } else {
      out << "waypoint_statuses: [";
      size_t pending_items = msg.waypoint_statuses.size();
      for (auto item : msg.waypoint_statuses) {
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
  const NavigateThroughPoses_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: current_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_pose:\n";
    to_block_style_yaml(msg.current_pose, out, indentation + 2);
  }

  // member: navigation_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "navigation_time:\n";
    to_block_style_yaml(msg.navigation_time, out, indentation + 2);
  }

  // member: estimated_time_remaining
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "estimated_time_remaining:\n";
    to_block_style_yaml(msg.estimated_time_remaining, out, indentation + 2);
  }

  // member: number_of_recoveries
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "number_of_recoveries: ";
    rosidl_generator_traits::value_to_yaml(msg.number_of_recoveries, out);
    out << "\n";
  }

  // member: distance_remaining
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "distance_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.distance_remaining, out);
    out << "\n";
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

  // member: number_of_poses_remaining
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "number_of_poses_remaining: ";
    rosidl_generator_traits::value_to_yaml(msg.number_of_poses_remaining, out);
    out << "\n";
  }

  // member: waypoint_statuses
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.waypoint_statuses.size() == 0) {
      out << "waypoint_statuses: []\n";
    } else {
      out << "waypoint_statuses:\n";
      for (auto item : msg.waypoint_statuses) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_Feedback>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).current_pose,
    std::forward<T>(msg).navigation_time,
    std::forward<T>(msg).estimated_time_remaining,
    std::forward<T>(msg).number_of_recoveries,
    std::forward<T>(msg).distance_remaining,
    std::forward<T>(msg).position_tracking_error,
    std::forward<T>(msg).heading_tracking_error,
    std::forward<T>(msg).number_of_poses_remaining,
    std::forward<T>(msg).waypoint_statuses);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_Feedback>()
{
  return "nav2_msgs::action::NavigateThroughPoses_Feedback";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_Feedback>()
{
  return "nav2_msgs/action/NavigateThroughPoses_Feedback";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_Feedback>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_Feedback>
{
  static constexpr std::size_t member_count = 9;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "current_pose",
    "navigation_time",
    "estimated_time_remaining",
    "number_of_recoveries",
    "distance_remaining",
    "position_tracking_error",
    "heading_tracking_error",
    "number_of_poses_remaining",
    "waypoint_statuses",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "nav2_msgs/action/detail/navigate_through_poses__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_SendGoal_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NavigateThroughPoses_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).goal_id,
    std::forward<T>(msg).goal);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>()
{
  return "nav2_msgs::action::NavigateThroughPoses_SendGoal_Request";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>()
{
  return "nav2_msgs/action/NavigateThroughPoses_SendGoal_Request";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::NavigateThroughPoses_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::NavigateThroughPoses_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "goal_id",
    "goal",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_SendGoal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NavigateThroughPoses_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << "\n";
  }

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).accepted,
    std::forward<T>(msg).stamp);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>()
{
  return "nav2_msgs::action::NavigateThroughPoses_SendGoal_Response";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>()
{
  return "nav2_msgs/action/NavigateThroughPoses_SendGoal_Response";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "accepted",
    "stamp",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_SendGoal_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
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
  const NavigateThroughPoses_SendGoal_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_SendGoal_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_SendGoal_Event>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).info,
    std::forward<T>(msg).request,
    std::forward<T>(msg).response);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_SendGoal_Event>()
{
  return "nav2_msgs::action::NavigateThroughPoses_SendGoal_Event";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_SendGoal_Event>()
{
  return "nav2_msgs/action/NavigateThroughPoses_SendGoal_Event";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>::value && has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_SendGoal_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_SendGoal_Event>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "info",
    "request",
    "response",
  };
};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_SendGoal>()
{
  return "nav2_msgs::action::NavigateThroughPoses_SendGoal";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_SendGoal>()
{
  return "nav2_msgs/action/NavigateThroughPoses_SendGoal";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>::value &&
    has_fixed_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>::value &&
    has_bounded_size<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::action::NavigateThroughPoses_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::action::NavigateThroughPoses_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::action::NavigateThroughPoses_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_GetResult_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NavigateThroughPoses_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_GetResult_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).goal_id);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>()
{
  return "nav2_msgs::action::NavigateThroughPoses_GetResult_Request";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>()
{
  return "nav2_msgs/action/NavigateThroughPoses_GetResult_Request";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "goal_id",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "nav2_msgs/action/detail/navigate_through_poses__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_GetResult_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: result
  {
    out << "result: ";
    to_flow_style_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NavigateThroughPoses_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_block_style_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_GetResult_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).status,
    std::forward<T>(msg).result);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>()
{
  return "nav2_msgs::action::NavigateThroughPoses_GetResult_Response";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>()
{
  return "nav2_msgs/action/NavigateThroughPoses_GetResult_Response";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::NavigateThroughPoses_Result>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::NavigateThroughPoses_Result>::value> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "status",
    "result",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
// already included above
// #include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_GetResult_Event & msg,
  std::ostream & out)
{
  out << "{";
  // member: info
  {
    out << "info: ";
    to_flow_style_yaml(msg.info, out);
    out << ", ";
  }

  // member: request
  {
    if (msg.request.size() == 0) {
      out << "request: []";
    } else {
      out << "request: [";
      size_t pending_items = msg.request.size();
      for (auto item : msg.request) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: response
  {
    if (msg.response.size() == 0) {
      out << "response: []";
    } else {
      out << "response: [";
      size_t pending_items = msg.response.size();
      for (auto item : msg.response) {
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
  const NavigateThroughPoses_GetResult_Event & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: info
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "info:\n";
    to_block_style_yaml(msg.info, out, indentation + 2);
  }

  // member: request
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.request.size() == 0) {
      out << "request: []\n";
    } else {
      out << "request:\n";
      for (auto item : msg.request) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: response
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.response.size() == 0) {
      out << "response: []\n";
    } else {
      out << "response:\n";
      for (auto item : msg.response) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_GetResult_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_GetResult_Event>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).info,
    std::forward<T>(msg).request,
    std::forward<T>(msg).response);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_GetResult_Event>()
{
  return "nav2_msgs::action::NavigateThroughPoses_GetResult_Event";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_GetResult_Event>()
{
  return "nav2_msgs/action/NavigateThroughPoses_GetResult_Event";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>::value && has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_GetResult_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_GetResult_Event>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "info",
    "request",
    "response",
  };
};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_GetResult>()
{
  return "nav2_msgs::action::NavigateThroughPoses_GetResult";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_GetResult>()
{
  return "nav2_msgs/action/NavigateThroughPoses_GetResult";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>::value &&
    has_fixed_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>::value &&
    has_bounded_size<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::action::NavigateThroughPoses_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::action::NavigateThroughPoses_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::action::NavigateThroughPoses_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "nav2_msgs/action/detail/navigate_through_poses__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const NavigateThroughPoses_FeedbackMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: feedback
  {
    out << "feedback: ";
    to_flow_style_yaml(msg.feedback, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const NavigateThroughPoses_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_block_style_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const NavigateThroughPoses_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::NavigateThroughPoses_FeedbackMessage>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).goal_id,
    std::forward<T>(msg).feedback);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses_FeedbackMessage>()
{
  return "nav2_msgs::action::NavigateThroughPoses_FeedbackMessage";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses_FeedbackMessage>()
{
  return "nav2_msgs/action/NavigateThroughPoses_FeedbackMessage";
}

template<>
struct has_fixed_size<nav2_msgs::action::NavigateThroughPoses_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::NavigateThroughPoses_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::NavigateThroughPoses_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::NavigateThroughPoses_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::NavigateThroughPoses_FeedbackMessage>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::NavigateThroughPoses_FeedbackMessage>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "goal_id",
    "feedback",
  };
};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::NavigateThroughPoses>()
{
  return "nav2_msgs::action::NavigateThroughPoses";
}

template<>
constexpr const char * name<nav2_msgs::action::NavigateThroughPoses>()
{
  return "nav2_msgs/action/NavigateThroughPoses";
}

template<>
struct is_action<nav2_msgs::action::NavigateThroughPoses>
  : std::true_type
{
};

template<>
struct is_action_goal<nav2_msgs::action::NavigateThroughPoses_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<nav2_msgs::action::NavigateThroughPoses_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<nav2_msgs::action::NavigateThroughPoses_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // NAV2_MSGS__ACTION__DETAIL__NAVIGATE_THROUGH_POSES__TRAITS_HPP_
