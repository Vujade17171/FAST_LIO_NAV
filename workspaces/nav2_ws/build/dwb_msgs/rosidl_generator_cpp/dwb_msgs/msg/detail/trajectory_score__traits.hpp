// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dwb_msgs:msg/TrajectoryScore.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "dwb_msgs/msg/trajectory_score.hpp"


#ifndef DWB_MSGS__MSG__DETAIL__TRAJECTORY_SCORE__TRAITS_HPP_
#define DWB_MSGS__MSG__DETAIL__TRAJECTORY_SCORE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "dwb_msgs/msg/detail/trajectory_score__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'traj'
#include "dwb_msgs/msg/detail/trajectory2_d__traits.hpp"
// Member 'scores'
#include "dwb_msgs/msg/detail/critic_score__traits.hpp"

namespace dwb_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const TrajectoryScore & msg,
  std::ostream & out)
{
  out << "{";
  // member: traj
  {
    out << "traj: ";
    to_flow_style_yaml(msg.traj, out);
    out << ", ";
  }

  // member: scores
  {
    if (msg.scores.size() == 0) {
      out << "scores: []";
    } else {
      out << "scores: [";
      size_t pending_items = msg.scores.size();
      for (auto item : msg.scores) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: total
  {
    out << "total: ";
    rosidl_generator_traits::value_to_yaml(msg.total, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const TrajectoryScore & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: traj
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "traj:\n";
    to_block_style_yaml(msg.traj, out, indentation + 2);
  }

  // member: scores
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.scores.size() == 0) {
      out << "scores: []\n";
    } else {
      out << "scores:\n";
      for (auto item : msg.scores) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: total
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "total: ";
    rosidl_generator_traits::value_to_yaml(msg.total, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const TrajectoryScore & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, dwb_msgs::msg::TrajectoryScore>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).traj,
    std::forward<T>(msg).scores,
    std::forward<T>(msg).total);
}

}  // namespace msg

}  // namespace dwb_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<dwb_msgs::msg::TrajectoryScore>()
{
  return "dwb_msgs::msg::TrajectoryScore";
}

template<>
constexpr const char * name<dwb_msgs::msg::TrajectoryScore>()
{
  return "dwb_msgs/msg/TrajectoryScore";
}

template<>
struct has_fixed_size<dwb_msgs::msg::TrajectoryScore>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dwb_msgs::msg::TrajectoryScore>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dwb_msgs::msg::TrajectoryScore>
  : std::true_type {};

template<>
struct MessageTraits<dwb_msgs::msg::TrajectoryScore>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "traj",
    "scores",
    "total",
  };
};

}  // namespace rosidl_generator_traits

#endif  // DWB_MSGS__MSG__DETAIL__TRAJECTORY_SCORE__TRAITS_HPP_
