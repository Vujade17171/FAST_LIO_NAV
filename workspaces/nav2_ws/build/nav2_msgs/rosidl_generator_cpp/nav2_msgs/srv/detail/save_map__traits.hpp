// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:srv/SaveMap.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/srv/save_map.hpp"


#ifndef NAV2_MSGS__SRV__DETAIL__SAVE_MAP__TRAITS_HPP_
#define NAV2_MSGS__SRV__DETAIL__SAVE_MAP__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/srv/detail/save_map__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace nav2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SaveMap_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: map_topic
  {
    out << "map_topic: ";
    rosidl_generator_traits::value_to_yaml(msg.map_topic, out);
    out << ", ";
  }

  // member: map_url
  {
    out << "map_url: ";
    rosidl_generator_traits::value_to_yaml(msg.map_url, out);
    out << ", ";
  }

  // member: image_format
  {
    out << "image_format: ";
    rosidl_generator_traits::value_to_yaml(msg.image_format, out);
    out << ", ";
  }

  // member: map_mode
  {
    out << "map_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.map_mode, out);
    out << ", ";
  }

  // member: free_thresh
  {
    out << "free_thresh: ";
    rosidl_generator_traits::value_to_yaml(msg.free_thresh, out);
    out << ", ";
  }

  // member: occupied_thresh
  {
    out << "occupied_thresh: ";
    rosidl_generator_traits::value_to_yaml(msg.occupied_thresh, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SaveMap_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: map_topic
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "map_topic: ";
    rosidl_generator_traits::value_to_yaml(msg.map_topic, out);
    out << "\n";
  }

  // member: map_url
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "map_url: ";
    rosidl_generator_traits::value_to_yaml(msg.map_url, out);
    out << "\n";
  }

  // member: image_format
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "image_format: ";
    rosidl_generator_traits::value_to_yaml(msg.image_format, out);
    out << "\n";
  }

  // member: map_mode
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "map_mode: ";
    rosidl_generator_traits::value_to_yaml(msg.map_mode, out);
    out << "\n";
  }

  // member: free_thresh
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "free_thresh: ";
    rosidl_generator_traits::value_to_yaml(msg.free_thresh, out);
    out << "\n";
  }

  // member: occupied_thresh
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "occupied_thresh: ";
    rosidl_generator_traits::value_to_yaml(msg.occupied_thresh, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SaveMap_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::SaveMap_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).map_topic,
    std::forward<T>(msg).map_url,
    std::forward<T>(msg).image_format,
    std::forward<T>(msg).map_mode,
    std::forward<T>(msg).free_thresh,
    std::forward<T>(msg).occupied_thresh);
}

}  // namespace srv

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::srv::SaveMap_Request>()
{
  return "nav2_msgs::srv::SaveMap_Request";
}

template<>
constexpr const char * name<nav2_msgs::srv::SaveMap_Request>()
{
  return "nav2_msgs/srv/SaveMap_Request";
}

template<>
struct has_fixed_size<nav2_msgs::srv::SaveMap_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::srv::SaveMap_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::srv::SaveMap_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::SaveMap_Request>
{
  static constexpr std::size_t member_count = 6;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "map_topic",
    "map_url",
    "image_format",
    "map_mode",
    "free_thresh",
    "occupied_thresh",
  };
};

}  // namespace rosidl_generator_traits

namespace nav2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SaveMap_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: result
  {
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SaveMap_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result: ";
    rosidl_generator_traits::value_to_yaml(msg.result, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SaveMap_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::SaveMap_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).result);
}

}  // namespace srv

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::srv::SaveMap_Response>()
{
  return "nav2_msgs::srv::SaveMap_Response";
}

template<>
constexpr const char * name<nav2_msgs::srv::SaveMap_Response>()
{
  return "nav2_msgs/srv/SaveMap_Response";
}

template<>
struct has_fixed_size<nav2_msgs::srv::SaveMap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<nav2_msgs::srv::SaveMap_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<nav2_msgs::srv::SaveMap_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::SaveMap_Response>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "result",
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
  const SaveMap_Event & msg,
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
  const SaveMap_Event & msg,
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

inline std::string to_yaml(const SaveMap_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::SaveMap_Event>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::srv::SaveMap_Event>()
{
  return "nav2_msgs::srv::SaveMap_Event";
}

template<>
constexpr const char * name<nav2_msgs::srv::SaveMap_Event>()
{
  return "nav2_msgs/srv/SaveMap_Event";
}

template<>
struct has_fixed_size<nav2_msgs::srv::SaveMap_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::srv::SaveMap_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::srv::SaveMap_Request>::value && has_bounded_size<nav2_msgs::srv::SaveMap_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::srv::SaveMap_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::SaveMap_Event>
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
constexpr const char * data_type<nav2_msgs::srv::SaveMap>()
{
  return "nav2_msgs::srv::SaveMap";
}

template<>
constexpr const char * name<nav2_msgs::srv::SaveMap>()
{
  return "nav2_msgs/srv/SaveMap";
}

template<>
struct has_fixed_size<nav2_msgs::srv::SaveMap>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::srv::SaveMap_Request>::value &&
    has_fixed_size<nav2_msgs::srv::SaveMap_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::srv::SaveMap>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::srv::SaveMap_Request>::value &&
    has_bounded_size<nav2_msgs::srv::SaveMap_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::srv::SaveMap>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::srv::SaveMap_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::srv::SaveMap_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__SRV__DETAIL__SAVE_MAP__TRAITS_HPP_
