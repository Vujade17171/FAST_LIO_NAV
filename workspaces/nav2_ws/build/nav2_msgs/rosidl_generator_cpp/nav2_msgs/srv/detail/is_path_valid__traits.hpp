// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:srv/IsPathValid.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/srv/is_path_valid.hpp"


#ifndef NAV2_MSGS__SRV__DETAIL__IS_PATH_VALID__TRAITS_HPP_
#define NAV2_MSGS__SRV__DETAIL__IS_PATH_VALID__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/srv/detail/is_path_valid__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'path'
#include "nav_msgs/msg/detail/path__traits.hpp"

namespace nav2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const IsPathValid_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: path
  {
    out << "path: ";
    to_flow_style_yaml(msg.path, out);
    out << ", ";
  }

  // member: max_cost
  {
    out << "max_cost: ";
    rosidl_generator_traits::value_to_yaml(msg.max_cost, out);
    out << ", ";
  }

  // member: consider_unknown_as_obstacle
  {
    out << "consider_unknown_as_obstacle: ";
    rosidl_generator_traits::value_to_yaml(msg.consider_unknown_as_obstacle, out);
    out << ", ";
  }

  // member: layer_name
  {
    out << "layer_name: ";
    rosidl_generator_traits::value_to_yaml(msg.layer_name, out);
    out << ", ";
  }

  // member: footprint
  {
    out << "footprint: ";
    rosidl_generator_traits::value_to_yaml(msg.footprint, out);
    out << ", ";
  }

  // member: stop_at_first_collision
  {
    out << "stop_at_first_collision: ";
    rosidl_generator_traits::value_to_yaml(msg.stop_at_first_collision, out);
    out << ", ";
  }

  // member: max_lookahead_distance
  {
    out << "max_lookahead_distance: ";
    rosidl_generator_traits::value_to_yaml(msg.max_lookahead_distance, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const IsPathValid_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: path
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "path:\n";
    to_block_style_yaml(msg.path, out, indentation + 2);
  }

  // member: max_cost
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_cost: ";
    rosidl_generator_traits::value_to_yaml(msg.max_cost, out);
    out << "\n";
  }

  // member: consider_unknown_as_obstacle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "consider_unknown_as_obstacle: ";
    rosidl_generator_traits::value_to_yaml(msg.consider_unknown_as_obstacle, out);
    out << "\n";
  }

  // member: layer_name
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "layer_name: ";
    rosidl_generator_traits::value_to_yaml(msg.layer_name, out);
    out << "\n";
  }

  // member: footprint
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "footprint: ";
    rosidl_generator_traits::value_to_yaml(msg.footprint, out);
    out << "\n";
  }

  // member: stop_at_first_collision
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stop_at_first_collision: ";
    rosidl_generator_traits::value_to_yaml(msg.stop_at_first_collision, out);
    out << "\n";
  }

  // member: max_lookahead_distance
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_lookahead_distance: ";
    rosidl_generator_traits::value_to_yaml(msg.max_lookahead_distance, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IsPathValid_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::IsPathValid_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).path,
    std::forward<T>(msg).max_cost,
    std::forward<T>(msg).consider_unknown_as_obstacle,
    std::forward<T>(msg).layer_name,
    std::forward<T>(msg).footprint,
    std::forward<T>(msg).stop_at_first_collision,
    std::forward<T>(msg).max_lookahead_distance);
}

}  // namespace srv

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::srv::IsPathValid_Request>()
{
  return "nav2_msgs::srv::IsPathValid_Request";
}

template<>
constexpr const char * name<nav2_msgs::srv::IsPathValid_Request>()
{
  return "nav2_msgs/srv/IsPathValid_Request";
}

template<>
struct has_fixed_size<nav2_msgs::srv::IsPathValid_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::srv::IsPathValid_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::srv::IsPathValid_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::IsPathValid_Request>
{
  static constexpr std::size_t member_count = 7;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "path",
    "max_cost",
    "consider_unknown_as_obstacle",
    "layer_name",
    "footprint",
    "stop_at_first_collision",
    "max_lookahead_distance",
  };
};

}  // namespace rosidl_generator_traits

namespace nav2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const IsPathValid_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: is_valid
  {
    out << "is_valid: ";
    rosidl_generator_traits::value_to_yaml(msg.is_valid, out);
    out << ", ";
  }

  // member: invalid_pose_indices
  {
    if (msg.invalid_pose_indices.size() == 0) {
      out << "invalid_pose_indices: []";
    } else {
      out << "invalid_pose_indices: [";
      size_t pending_items = msg.invalid_pose_indices.size();
      for (auto item : msg.invalid_pose_indices) {
        rosidl_generator_traits::value_to_yaml(item, out);
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
  const IsPathValid_Response & msg,
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

  // member: is_valid
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "is_valid: ";
    rosidl_generator_traits::value_to_yaml(msg.is_valid, out);
    out << "\n";
  }

  // member: invalid_pose_indices
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.invalid_pose_indices.size() == 0) {
      out << "invalid_pose_indices: []\n";
    } else {
      out << "invalid_pose_indices:\n";
      for (auto item : msg.invalid_pose_indices) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const IsPathValid_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::IsPathValid_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).success,
    std::forward<T>(msg).is_valid,
    std::forward<T>(msg).invalid_pose_indices);
}

}  // namespace srv

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::srv::IsPathValid_Response>()
{
  return "nav2_msgs::srv::IsPathValid_Response";
}

template<>
constexpr const char * name<nav2_msgs::srv::IsPathValid_Response>()
{
  return "nav2_msgs/srv/IsPathValid_Response";
}

template<>
struct has_fixed_size<nav2_msgs::srv::IsPathValid_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::srv::IsPathValid_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::srv::IsPathValid_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::IsPathValid_Response>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "success",
    "is_valid",
    "invalid_pose_indices",
  };
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__traits.hpp"

namespace nav2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const IsPathValid_Event & msg,
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
  const IsPathValid_Event & msg,
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

inline std::string to_yaml(const IsPathValid_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::IsPathValid_Event>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).info,
    std::forward<T>(msg).request,
    std::forward<T>(msg).response);
}

}  // namespace srv

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::srv::IsPathValid_Event>()
{
  return "nav2_msgs::srv::IsPathValid_Event";
}

template<>
constexpr const char * name<nav2_msgs::srv::IsPathValid_Event>()
{
  return "nav2_msgs/srv/IsPathValid_Event";
}

template<>
struct has_fixed_size<nav2_msgs::srv::IsPathValid_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::srv::IsPathValid_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::srv::IsPathValid_Request>::value && has_bounded_size<nav2_msgs::srv::IsPathValid_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::srv::IsPathValid_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::IsPathValid_Event>
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
constexpr const char * data_type<nav2_msgs::srv::IsPathValid>()
{
  return "nav2_msgs::srv::IsPathValid";
}

template<>
constexpr const char * name<nav2_msgs::srv::IsPathValid>()
{
  return "nav2_msgs/srv/IsPathValid";
}

template<>
struct has_fixed_size<nav2_msgs::srv::IsPathValid>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::srv::IsPathValid_Request>::value &&
    has_fixed_size<nav2_msgs::srv::IsPathValid_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::srv::IsPathValid>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::srv::IsPathValid_Request>::value &&
    has_bounded_size<nav2_msgs::srv::IsPathValid_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::srv::IsPathValid>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::srv::IsPathValid_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::srv::IsPathValid_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__SRV__DETAIL__IS_PATH_VALID__TRAITS_HPP_
