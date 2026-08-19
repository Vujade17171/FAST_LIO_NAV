// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from dwb_msgs:srv/GetCriticScore.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "dwb_msgs/srv/get_critic_score.hpp"


#ifndef DWB_MSGS__SRV__DETAIL__GET_CRITIC_SCORE__TRAITS_HPP_
#define DWB_MSGS__SRV__DETAIL__GET_CRITIC_SCORE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "dwb_msgs/srv/detail/get_critic_score__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'pose'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"
// Member 'velocity'
#include "nav_2d_msgs/msg/detail/twist2_d__traits.hpp"
// Member 'global_plan'
#include "nav_msgs/msg/detail/path__traits.hpp"
// Member 'traj'
#include "dwb_msgs/msg/detail/trajectory2_d__traits.hpp"

namespace dwb_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetCriticScore_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: pose
  {
    out << "pose: ";
    to_flow_style_yaml(msg.pose, out);
    out << ", ";
  }

  // member: velocity
  {
    out << "velocity: ";
    to_flow_style_yaml(msg.velocity, out);
    out << ", ";
  }

  // member: global_plan
  {
    out << "global_plan: ";
    to_flow_style_yaml(msg.global_plan, out);
    out << ", ";
  }

  // member: traj
  {
    out << "traj: ";
    to_flow_style_yaml(msg.traj, out);
    out << ", ";
  }

  // member: critic_name
  {
    out << "critic_name: ";
    rosidl_generator_traits::value_to_yaml(msg.critic_name, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetCriticScore_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: pose
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "pose:\n";
    to_block_style_yaml(msg.pose, out, indentation + 2);
  }

  // member: velocity
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "velocity:\n";
    to_block_style_yaml(msg.velocity, out, indentation + 2);
  }

  // member: global_plan
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "global_plan:\n";
    to_block_style_yaml(msg.global_plan, out, indentation + 2);
  }

  // member: traj
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "traj:\n";
    to_block_style_yaml(msg.traj, out, indentation + 2);
  }

  // member: critic_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "critic_name: ";
    rosidl_generator_traits::value_to_yaml(msg.critic_name, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetCriticScore_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, dwb_msgs::srv::GetCriticScore_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).pose,
    std::forward<T>(msg).velocity,
    std::forward<T>(msg).global_plan,
    std::forward<T>(msg).traj,
    std::forward<T>(msg).critic_name);
}

}  // namespace srv

}  // namespace dwb_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<dwb_msgs::srv::GetCriticScore_Request>()
{
  return "dwb_msgs::srv::GetCriticScore_Request";
}

template<>
constexpr const char * name<dwb_msgs::srv::GetCriticScore_Request>()
{
  return "dwb_msgs/srv/GetCriticScore_Request";
}

template<>
struct has_fixed_size<dwb_msgs::srv::GetCriticScore_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dwb_msgs::srv::GetCriticScore_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<dwb_msgs::srv::GetCriticScore_Request>
  : std::true_type {};

template<>
struct MessageTraits<dwb_msgs::srv::GetCriticScore_Request>
{
  static constexpr std::size_t member_count = 5;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "pose",
    "velocity",
    "global_plan",
    "traj",
    "critic_name",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'score'
#include "dwb_msgs/msg/detail/critic_score__traits.hpp"

namespace dwb_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetCriticScore_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: score
  {
    out << "score: ";
    to_flow_style_yaml(msg.score, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetCriticScore_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: score
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "score:\n";
    to_block_style_yaml(msg.score, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetCriticScore_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, dwb_msgs::srv::GetCriticScore_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).score);
}

}  // namespace srv

}  // namespace dwb_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<dwb_msgs::srv::GetCriticScore_Response>()
{
  return "dwb_msgs::srv::GetCriticScore_Response";
}

template<>
constexpr const char * name<dwb_msgs::srv::GetCriticScore_Response>()
{
  return "dwb_msgs/srv/GetCriticScore_Response";
}

template<>
struct has_fixed_size<dwb_msgs::srv::GetCriticScore_Response>
  : std::integral_constant<bool, has_fixed_size<dwb_msgs::msg::CriticScore>::value> {};

template<>
struct has_bounded_size<dwb_msgs::srv::GetCriticScore_Response>
  : std::integral_constant<bool, has_bounded_size<dwb_msgs::msg::CriticScore>::value> {};

template<>
struct is_message<dwb_msgs::srv::GetCriticScore_Response>
  : std::true_type {};

template<>
struct MessageTraits<dwb_msgs::srv::GetCriticScore_Response>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "score",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace dwb_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetCriticScore_Event & msg,
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
  const GetCriticScore_Event & msg,
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

inline std::string to_yaml(const GetCriticScore_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, dwb_msgs::srv::GetCriticScore_Event>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).info,
    std::forward<T>(msg).request,
    std::forward<T>(msg).response);
}

}  // namespace srv

}  // namespace dwb_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<dwb_msgs::srv::GetCriticScore_Event>()
{
  return "dwb_msgs::srv::GetCriticScore_Event";
}

template<>
constexpr const char * name<dwb_msgs::srv::GetCriticScore_Event>()
{
  return "dwb_msgs/srv/GetCriticScore_Event";
}

template<>
struct has_fixed_size<dwb_msgs::srv::GetCriticScore_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<dwb_msgs::srv::GetCriticScore_Event>
  : std::integral_constant<bool, has_bounded_size<dwb_msgs::srv::GetCriticScore_Request>::value && has_bounded_size<dwb_msgs::srv::GetCriticScore_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<dwb_msgs::srv::GetCriticScore_Event>
  : std::true_type {};

template<>
struct MessageTraits<dwb_msgs::srv::GetCriticScore_Event>
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
constexpr const char * data_type<dwb_msgs::srv::GetCriticScore>()
{
  return "dwb_msgs::srv::GetCriticScore";
}

template<>
constexpr const char * name<dwb_msgs::srv::GetCriticScore>()
{
  return "dwb_msgs/srv/GetCriticScore";
}

template<>
struct has_fixed_size<dwb_msgs::srv::GetCriticScore>
  : std::integral_constant<
    bool,
    has_fixed_size<dwb_msgs::srv::GetCriticScore_Request>::value &&
    has_fixed_size<dwb_msgs::srv::GetCriticScore_Response>::value
  >
{
};

template<>
struct has_bounded_size<dwb_msgs::srv::GetCriticScore>
  : std::integral_constant<
    bool,
    has_bounded_size<dwb_msgs::srv::GetCriticScore_Request>::value &&
    has_bounded_size<dwb_msgs::srv::GetCriticScore_Response>::value
  >
{
};

template<>
struct is_service<dwb_msgs::srv::GetCriticScore>
  : std::true_type
{
};

template<>
struct is_service_request<dwb_msgs::srv::GetCriticScore_Request>
  : std::true_type
{
};

template<>
struct is_service_response<dwb_msgs::srv::GetCriticScore_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // DWB_MSGS__SRV__DETAIL__GET_CRITIC_SCORE__TRAITS_HPP_
