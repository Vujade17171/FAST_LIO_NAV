// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:action/ComputeAndTrackRoute.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/action/compute_and_track_route.hpp"


#ifndef NAV2_MSGS__ACTION__DETAIL__COMPUTE_AND_TRACK_ROUTE__TRAITS_HPP_
#define NAV2_MSGS__ACTION__DETAIL__COMPUTE_AND_TRACK_ROUTE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/action/detail/compute_and_track_route__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'start'
// Member 'goal'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const ComputeAndTrackRoute_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: start_id
  {
    out << "start_id: ";
    rosidl_generator_traits::value_to_yaml(msg.start_id, out);
    out << ", ";
  }

  // member: start
  {
    out << "start: ";
    to_flow_style_yaml(msg.start, out);
    out << ", ";
  }

  // member: goal_id
  {
    out << "goal_id: ";
    rosidl_generator_traits::value_to_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
    out << ", ";
  }

  // member: use_start
  {
    out << "use_start: ";
    rosidl_generator_traits::value_to_yaml(msg.use_start, out);
    out << ", ";
  }

  // member: use_poses
  {
    out << "use_poses: ";
    rosidl_generator_traits::value_to_yaml(msg.use_poses, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ComputeAndTrackRoute_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: start_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "start_id: ";
    rosidl_generator_traits::value_to_yaml(msg.start_id, out);
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

  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id: ";
    rosidl_generator_traits::value_to_yaml(msg.goal_id, out);
    out << "\n";
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }

  // member: use_start
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "use_start: ";
    rosidl_generator_traits::value_to_yaml(msg.use_start, out);
    out << "\n";
  }

  // member: use_poses
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "use_poses: ";
    rosidl_generator_traits::value_to_yaml(msg.use_poses, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ComputeAndTrackRoute_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_Goal>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).start_id,
    std::forward<T>(msg).start,
    std::forward<T>(msg).goal_id,
    std::forward<T>(msg).goal,
    std::forward<T>(msg).use_start,
    std::forward<T>(msg).use_poses);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_Goal>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_Goal";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_Goal>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_Goal";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_Goal>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::PoseStamped>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_Goal>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::PoseStamped>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_Goal>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_Goal>
{
  static constexpr std::size_t member_count = 6;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "start_id",
    "start",
    "goal_id",
    "goal",
    "use_start",
    "use_poses",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'execution_duration'
#include "builtin_interfaces/msg/detail/duration__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const ComputeAndTrackRoute_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: execution_duration
  {
    out << "execution_duration: ";
    to_flow_style_yaml(msg.execution_duration, out);
    out << ", ";
  }

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
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ComputeAndTrackRoute_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: execution_duration
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "execution_duration:\n";
    to_block_style_yaml(msg.execution_duration, out, indentation + 2);
  }

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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ComputeAndTrackRoute_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_Result>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).execution_duration,
    std::forward<T>(msg).error_code,
    std::forward<T>(msg).error_msg);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_Result>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_Result";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_Result>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_Result";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_Result>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_Result>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "execution_duration",
    "error_code",
    "error_msg",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'route'
#include "nav2_msgs/msg/detail/route__traits.hpp"
// Member 'path'
#include "nav_msgs/msg/detail/path__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const ComputeAndTrackRoute_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: last_node_id
  {
    out << "last_node_id: ";
    rosidl_generator_traits::value_to_yaml(msg.last_node_id, out);
    out << ", ";
  }

  // member: next_node_id
  {
    out << "next_node_id: ";
    rosidl_generator_traits::value_to_yaml(msg.next_node_id, out);
    out << ", ";
  }

  // member: current_edge_id
  {
    out << "current_edge_id: ";
    rosidl_generator_traits::value_to_yaml(msg.current_edge_id, out);
    out << ", ";
  }

  // member: route
  {
    out << "route: ";
    to_flow_style_yaml(msg.route, out);
    out << ", ";
  }

  // member: path
  {
    out << "path: ";
    to_flow_style_yaml(msg.path, out);
    out << ", ";
  }

  // member: operations_triggered
  {
    if (msg.operations_triggered.size() == 0) {
      out << "operations_triggered: []";
    } else {
      out << "operations_triggered: [";
      size_t pending_items = msg.operations_triggered.size();
      for (auto item : msg.operations_triggered) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: rerouted
  {
    out << "rerouted: ";
    rosidl_generator_traits::value_to_yaml(msg.rerouted, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ComputeAndTrackRoute_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: last_node_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "last_node_id: ";
    rosidl_generator_traits::value_to_yaml(msg.last_node_id, out);
    out << "\n";
  }

  // member: next_node_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "next_node_id: ";
    rosidl_generator_traits::value_to_yaml(msg.next_node_id, out);
    out << "\n";
  }

  // member: current_edge_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_edge_id: ";
    rosidl_generator_traits::value_to_yaml(msg.current_edge_id, out);
    out << "\n";
  }

  // member: route
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "route:\n";
    to_block_style_yaml(msg.route, out, indentation + 2);
  }

  // member: path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "path:\n";
    to_block_style_yaml(msg.path, out, indentation + 2);
  }

  // member: operations_triggered
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.operations_triggered.size() == 0) {
      out << "operations_triggered: []\n";
    } else {
      out << "operations_triggered:\n";
      for (auto item : msg.operations_triggered) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: rerouted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "rerouted: ";
    rosidl_generator_traits::value_to_yaml(msg.rerouted, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ComputeAndTrackRoute_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_Feedback>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).last_node_id,
    std::forward<T>(msg).next_node_id,
    std::forward<T>(msg).current_edge_id,
    std::forward<T>(msg).route,
    std::forward<T>(msg).path,
    std::forward<T>(msg).operations_triggered,
    std::forward<T>(msg).rerouted);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_Feedback>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_Feedback";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_Feedback>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_Feedback";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_Feedback>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_Feedback>
{
  static constexpr std::size_t member_count = 7;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "last_node_id",
    "next_node_id",
    "current_edge_id",
    "route",
    "path",
    "operations_triggered",
    "rerouted",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "nav2_msgs/action/detail/compute_and_track_route__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const ComputeAndTrackRoute_SendGoal_Request & msg,
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
  const ComputeAndTrackRoute_SendGoal_Request & msg,
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

inline std::string to_yaml(const ComputeAndTrackRoute_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_SendGoal_Request";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>
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
  const ComputeAndTrackRoute_SendGoal_Response & msg,
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
  const ComputeAndTrackRoute_SendGoal_Response & msg,
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

inline std::string to_yaml(const ComputeAndTrackRoute_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_SendGoal_Response";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>
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
  const ComputeAndTrackRoute_SendGoal_Event & msg,
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
  const ComputeAndTrackRoute_SendGoal_Event & msg,
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

inline std::string to_yaml(const ComputeAndTrackRoute_SendGoal_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_SendGoal_Event";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>::value && has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Event>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_SendGoal>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_SendGoal";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_SendGoal>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_SendGoal";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>::value &&
    has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>::value &&
    has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::action::ComputeAndTrackRoute_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::action::ComputeAndTrackRoute_SendGoal_Response>
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
  const ComputeAndTrackRoute_GetResult_Request & msg,
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
  const ComputeAndTrackRoute_GetResult_Request & msg,
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

inline std::string to_yaml(const ComputeAndTrackRoute_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).goal_id);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_GetResult_Request";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>
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
// #include "nav2_msgs/action/detail/compute_and_track_route__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const ComputeAndTrackRoute_GetResult_Response & msg,
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
  const ComputeAndTrackRoute_GetResult_Response & msg,
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

inline std::string to_yaml(const ComputeAndTrackRoute_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_GetResult_Response";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_Result>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_Result>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>
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
  const ComputeAndTrackRoute_GetResult_Event & msg,
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
  const ComputeAndTrackRoute_GetResult_Event & msg,
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

inline std::string to_yaml(const ComputeAndTrackRoute_GetResult_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_GetResult_Event";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>::value && has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Event>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_GetResult>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_GetResult";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_GetResult>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_GetResult";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>::value &&
    has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>::value &&
    has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::action::ComputeAndTrackRoute_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::action::ComputeAndTrackRoute_GetResult_Response>
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
// #include "nav2_msgs/action/detail/compute_and_track_route__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const ComputeAndTrackRoute_FeedbackMessage & msg,
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
  const ComputeAndTrackRoute_FeedbackMessage & msg,
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

inline std::string to_yaml(const ComputeAndTrackRoute_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute_FeedbackMessage";
}

template<>
struct has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::ComputeAndTrackRoute_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::ComputeAndTrackRoute_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::ComputeAndTrackRoute_FeedbackMessage>
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
constexpr const char * data_type<nav2_msgs::action::ComputeAndTrackRoute>()
{
  return "nav2_msgs::action::ComputeAndTrackRoute";
}

template<>
constexpr const char * name<nav2_msgs::action::ComputeAndTrackRoute>()
{
  return "nav2_msgs/action/ComputeAndTrackRoute";
}

template<>
struct is_action<nav2_msgs::action::ComputeAndTrackRoute>
  : std::true_type
{
};

template<>
struct is_action_goal<nav2_msgs::action::ComputeAndTrackRoute_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<nav2_msgs::action::ComputeAndTrackRoute_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<nav2_msgs::action::ComputeAndTrackRoute_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // NAV2_MSGS__ACTION__DETAIL__COMPUTE_AND_TRACK_ROUTE__TRAITS_HPP_
