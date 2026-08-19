// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/BehaviorTreeLog.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/behavior_tree_log.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__BEHAVIOR_TREE_LOG__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__BEHAVIOR_TREE_LOG__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/behavior_tree_log__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"
// Member 'event_log'
#include "nav2_msgs/msg/detail/behavior_tree_status_change__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const BehaviorTreeLog & msg,
  std::ostream & out)
{
  out << "{";
  // member: timestamp
  {
    out << "timestamp: ";
    to_flow_style_yaml(msg.timestamp, out);
    out << ", ";
  }

  // member: event_log
  {
    if (msg.event_log.size() == 0) {
      out << "event_log: []";
    } else {
      out << "event_log: [";
      size_t pending_items = msg.event_log.size();
      for (auto item : msg.event_log) {
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
  const BehaviorTreeLog & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: timestamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "timestamp:\n";
    to_block_style_yaml(msg.timestamp, out, indentation + 2);
  }

  // member: event_log
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.event_log.size() == 0) {
      out << "event_log: []\n";
    } else {
      out << "event_log:\n";
      for (auto item : msg.event_log) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const BehaviorTreeLog & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::BehaviorTreeLog>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).timestamp,
    std::forward<T>(msg).event_log);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::BehaviorTreeLog>()
{
  return "nav2_msgs::msg::BehaviorTreeLog";
}

template<>
constexpr const char * name<nav2_msgs::msg::BehaviorTreeLog>()
{
  return "nav2_msgs/msg/BehaviorTreeLog";
}

template<>
struct has_fixed_size<nav2_msgs::msg::BehaviorTreeLog>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::msg::BehaviorTreeLog>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::msg::BehaviorTreeLog>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::BehaviorTreeLog>
{
  static constexpr std::size_t member_count = 2;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "timestamp",
    "event_log",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__BEHAVIOR_TREE_LOG__TRAITS_HPP_
