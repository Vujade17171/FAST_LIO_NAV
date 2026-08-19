// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dwb_msgs:msg/CriticScore.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "dwb_msgs/msg/critic_score.hpp"


#ifndef DWB_MSGS__MSG__DETAIL__CRITIC_SCORE__TRAITS_HPP_
#define DWB_MSGS__MSG__DETAIL__CRITIC_SCORE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "dwb_msgs/msg/detail/critic_score__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace dwb_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const CriticScore & msg,
  std::ostream & out)
{
  out << "{";
  // member: name
  {
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << ", ";
  }

  // member: raw_score
  {
    out << "raw_score: ";
    rosidl_generator_traits::value_to_yaml(msg.raw_score, out);
    out << ", ";
  }

  // member: scale
  {
    out << "scale: ";
    rosidl_generator_traits::value_to_yaml(msg.scale, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const CriticScore & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "name: ";
    rosidl_generator_traits::value_to_yaml(msg.name, out);
    out << "\n";
  }

  // member: raw_score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "raw_score: ";
    rosidl_generator_traits::value_to_yaml(msg.raw_score, out);
    out << "\n";
  }

  // member: scale
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "scale: ";
    rosidl_generator_traits::value_to_yaml(msg.scale, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const CriticScore & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, dwb_msgs::msg::CriticScore>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).name,
    std::forward<T>(msg).raw_score,
    std::forward<T>(msg).scale);
}

}  // namespace msg

}  // namespace dwb_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<dwb_msgs::msg::CriticScore>()
{
  return "dwb_msgs::msg::CriticScore";
}

template<>
constexpr const char * name<dwb_msgs::msg::CriticScore>()
{
  return "dwb_msgs/msg/CriticScore";
}

template<>
struct has_fixed_size<dwb_msgs::msg::CriticScore>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dwb_msgs::msg::CriticScore>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dwb_msgs::msg::CriticScore>
  : std::true_type {};

template<>
struct MessageTraits<dwb_msgs::msg::CriticScore>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "name",
    "raw_score",
    "scale",
  };
};

}  // namespace rosidl_generator_traits

#endif  // DWB_MSGS__MSG__DETAIL__CRITIC_SCORE__TRAITS_HPP_
