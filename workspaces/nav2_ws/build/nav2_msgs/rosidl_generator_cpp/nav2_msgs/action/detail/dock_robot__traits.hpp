// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:action/DockRobot.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/action/dock_robot.hpp"


#ifndef NAV2_MSGS__ACTION__DETAIL__DOCK_ROBOT__TRAITS_HPP_
#define NAV2_MSGS__ACTION__DETAIL__DOCK_ROBOT__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/action/detail/dock_robot__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'dock_pose'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const DockRobot_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: use_dock_id
  {
    out << "use_dock_id: ";
    rosidl_generator_traits::value_to_yaml(msg.use_dock_id, out);
    out << ", ";
  }

  // member: dock_id
  {
    out << "dock_id: ";
    rosidl_generator_traits::value_to_yaml(msg.dock_id, out);
    out << ", ";
  }

  // member: dock_pose
  {
    out << "dock_pose: ";
    to_flow_style_yaml(msg.dock_pose, out);
    out << ", ";
  }

  // member: dock_type
  {
    out << "dock_type: ";
    rosidl_generator_traits::value_to_yaml(msg.dock_type, out);
    out << ", ";
  }

  // member: max_staging_time
  {
    out << "max_staging_time: ";
    rosidl_generator_traits::value_to_yaml(msg.max_staging_time, out);
    out << ", ";
  }

  // member: navigate_to_staging_pose
  {
    out << "navigate_to_staging_pose: ";
    rosidl_generator_traits::value_to_yaml(msg.navigate_to_staging_pose, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DockRobot_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: use_dock_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "use_dock_id: ";
    rosidl_generator_traits::value_to_yaml(msg.use_dock_id, out);
    out << "\n";
  }

  // member: dock_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dock_id: ";
    rosidl_generator_traits::value_to_yaml(msg.dock_id, out);
    out << "\n";
  }

  // member: dock_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dock_pose:\n";
    to_block_style_yaml(msg.dock_pose, out, indentation + 2);
  }

  // member: dock_type
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "dock_type: ";
    rosidl_generator_traits::value_to_yaml(msg.dock_type, out);
    out << "\n";
  }

  // member: max_staging_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_staging_time: ";
    rosidl_generator_traits::value_to_yaml(msg.max_staging_time, out);
    out << "\n";
  }

  // member: navigate_to_staging_pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "navigate_to_staging_pose: ";
    rosidl_generator_traits::value_to_yaml(msg.navigate_to_staging_pose, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DockRobot_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_Goal>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).use_dock_id,
    std::forward<T>(msg).dock_id,
    std::forward<T>(msg).dock_pose,
    std::forward<T>(msg).dock_type,
    std::forward<T>(msg).max_staging_time,
    std::forward<T>(msg).navigate_to_staging_pose);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::DockRobot_Goal>()
{
  return "nav2_msgs::action::DockRobot_Goal";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_Goal>()
{
  return "nav2_msgs/action/DockRobot_Goal";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_Goal>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_Goal>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_Goal>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_Goal>
{
  static constexpr std::size_t member_count = 6;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "use_dock_id",
    "dock_id",
    "dock_pose",
    "dock_type",
    "max_staging_time",
    "navigate_to_staging_pose",
  };
};

}  // namespace rosidl_generator_traits

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const DockRobot_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: error_code
  {
    out << "error_code: ";
    rosidl_generator_traits::value_to_yaml(msg.error_code, out);
    out << ", ";
  }

  // member: num_retries
  {
    out << "num_retries: ";
    rosidl_generator_traits::value_to_yaml(msg.num_retries, out);
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
  const DockRobot_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
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

  // member: num_retries
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "num_retries: ";
    rosidl_generator_traits::value_to_yaml(msg.num_retries, out);
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

inline std::string to_yaml(const DockRobot_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_Result>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).success,
    std::forward<T>(msg).error_code,
    std::forward<T>(msg).num_retries,
    std::forward<T>(msg).error_msg);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::DockRobot_Result>()
{
  return "nav2_msgs::action::DockRobot_Result";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_Result>()
{
  return "nav2_msgs/action/DockRobot_Result";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_Result>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_Result>
{
  static constexpr std::size_t member_count = 4;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "success",
    "error_code",
    "num_retries",
    "error_msg",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'docking_time'
#include "builtin_interfaces/msg/detail/duration__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const DockRobot_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: docking_time
  {
    out << "docking_time: ";
    to_flow_style_yaml(msg.docking_time, out);
    out << ", ";
  }

  // member: num_retries
  {
    out << "num_retries: ";
    rosidl_generator_traits::value_to_yaml(msg.num_retries, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DockRobot_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
  }

  // member: docking_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "docking_time:\n";
    to_block_style_yaml(msg.docking_time, out, indentation + 2);
  }

  // member: num_retries
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "num_retries: ";
    rosidl_generator_traits::value_to_yaml(msg.num_retries, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DockRobot_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_Feedback>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).state,
    std::forward<T>(msg).docking_time,
    std::forward<T>(msg).num_retries);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::DockRobot_Feedback>()
{
  return "nav2_msgs::action::DockRobot_Feedback";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_Feedback>()
{
  return "nav2_msgs/action/DockRobot_Feedback";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_Feedback>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Duration>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_Feedback>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Duration>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_Feedback>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_Feedback>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "state",
    "docking_time",
    "num_retries",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "nav2_msgs/action/detail/dock_robot__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const DockRobot_SendGoal_Request & msg,
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
  const DockRobot_SendGoal_Request & msg,
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

inline std::string to_yaml(const DockRobot_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_SendGoal_Request>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_SendGoal_Request>()
{
  return "nav2_msgs::action::DockRobot_SendGoal_Request";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_SendGoal_Request>()
{
  return "nav2_msgs/action/DockRobot_SendGoal_Request";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::DockRobot_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::DockRobot_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_SendGoal_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_SendGoal_Request>
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
  const DockRobot_SendGoal_Response & msg,
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
  const DockRobot_SendGoal_Response & msg,
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

inline std::string to_yaml(const DockRobot_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_SendGoal_Response>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_SendGoal_Response>()
{
  return "nav2_msgs::action::DockRobot_SendGoal_Response";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_SendGoal_Response>()
{
  return "nav2_msgs/action/DockRobot_SendGoal_Response";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_SendGoal_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_SendGoal_Response>
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
  const DockRobot_SendGoal_Event & msg,
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
  const DockRobot_SendGoal_Event & msg,
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

inline std::string to_yaml(const DockRobot_SendGoal_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_SendGoal_Event>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_SendGoal_Event>()
{
  return "nav2_msgs::action::DockRobot_SendGoal_Event";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_SendGoal_Event>()
{
  return "nav2_msgs/action/DockRobot_SendGoal_Event";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_SendGoal_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_SendGoal_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::DockRobot_SendGoal_Request>::value && has_bounded_size<nav2_msgs::action::DockRobot_SendGoal_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_SendGoal_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_SendGoal_Event>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_SendGoal>()
{
  return "nav2_msgs::action::DockRobot_SendGoal";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_SendGoal>()
{
  return "nav2_msgs/action/DockRobot_SendGoal";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::action::DockRobot_SendGoal_Request>::value &&
    has_fixed_size<nav2_msgs::action::DockRobot_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::action::DockRobot_SendGoal_Request>::value &&
    has_bounded_size<nav2_msgs::action::DockRobot_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::action::DockRobot_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::action::DockRobot_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::action::DockRobot_SendGoal_Response>
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
  const DockRobot_GetResult_Request & msg,
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
  const DockRobot_GetResult_Request & msg,
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

inline std::string to_yaml(const DockRobot_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_GetResult_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).goal_id);
}

}  // namespace action

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::action::DockRobot_GetResult_Request>()
{
  return "nav2_msgs::action::DockRobot_GetResult_Request";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_GetResult_Request>()
{
  return "nav2_msgs/action/DockRobot_GetResult_Request";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_GetResult_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_GetResult_Request>
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
// #include "nav2_msgs/action/detail/dock_robot__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const DockRobot_GetResult_Response & msg,
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
  const DockRobot_GetResult_Response & msg,
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

inline std::string to_yaml(const DockRobot_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_GetResult_Response>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_GetResult_Response>()
{
  return "nav2_msgs::action::DockRobot_GetResult_Response";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_GetResult_Response>()
{
  return "nav2_msgs/action/DockRobot_GetResult_Response";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::DockRobot_Result>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::DockRobot_Result>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_GetResult_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_GetResult_Response>
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
  const DockRobot_GetResult_Event & msg,
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
  const DockRobot_GetResult_Event & msg,
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

inline std::string to_yaml(const DockRobot_GetResult_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_GetResult_Event>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_GetResult_Event>()
{
  return "nav2_msgs::action::DockRobot_GetResult_Event";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_GetResult_Event>()
{
  return "nav2_msgs/action/DockRobot_GetResult_Event";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_GetResult_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_GetResult_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::DockRobot_GetResult_Request>::value && has_bounded_size<nav2_msgs::action::DockRobot_GetResult_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_GetResult_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_GetResult_Event>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_GetResult>()
{
  return "nav2_msgs::action::DockRobot_GetResult";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_GetResult>()
{
  return "nav2_msgs/action/DockRobot_GetResult";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::action::DockRobot_GetResult_Request>::value &&
    has_fixed_size<nav2_msgs::action::DockRobot_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::action::DockRobot_GetResult_Request>::value &&
    has_bounded_size<nav2_msgs::action::DockRobot_GetResult_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::action::DockRobot_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::action::DockRobot_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::action::DockRobot_GetResult_Response>
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
// #include "nav2_msgs/action/detail/dock_robot__traits.hpp"

namespace nav2_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const DockRobot_FeedbackMessage & msg,
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
  const DockRobot_FeedbackMessage & msg,
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

inline std::string to_yaml(const DockRobot_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::action::DockRobot_FeedbackMessage>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot_FeedbackMessage>()
{
  return "nav2_msgs::action::DockRobot_FeedbackMessage";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot_FeedbackMessage>()
{
  return "nav2_msgs/action/DockRobot_FeedbackMessage";
}

template<>
struct has_fixed_size<nav2_msgs::action::DockRobot_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<nav2_msgs::action::DockRobot_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<nav2_msgs::action::DockRobot_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::action::DockRobot_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<nav2_msgs::action::DockRobot_FeedbackMessage>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::action::DockRobot_FeedbackMessage>
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
constexpr const char * data_type<nav2_msgs::action::DockRobot>()
{
  return "nav2_msgs::action::DockRobot";
}

template<>
constexpr const char * name<nav2_msgs::action::DockRobot>()
{
  return "nav2_msgs/action/DockRobot";
}

template<>
struct is_action<nav2_msgs::action::DockRobot>
  : std::true_type
{
};

template<>
struct is_action_goal<nav2_msgs::action::DockRobot_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<nav2_msgs::action::DockRobot_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<nav2_msgs::action::DockRobot_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // NAV2_MSGS__ACTION__DETAIL__DOCK_ROBOT__TRAITS_HPP_
