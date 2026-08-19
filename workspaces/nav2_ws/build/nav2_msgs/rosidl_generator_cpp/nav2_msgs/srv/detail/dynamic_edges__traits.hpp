// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:srv/DynamicEdges.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/srv/dynamic_edges.hpp"


#ifndef NAV2_MSGS__SRV__DETAIL__DYNAMIC_EDGES__TRAITS_HPP_
#define NAV2_MSGS__SRV__DETAIL__DYNAMIC_EDGES__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/srv/detail/dynamic_edges__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'adjust_edges'
#include "nav2_msgs/msg/detail/edge_cost__traits.hpp"

namespace nav2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const DynamicEdges_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: closed_edges
  {
    if (msg.closed_edges.size() == 0) {
      out << "closed_edges: []";
    } else {
      out << "closed_edges: [";
      size_t pending_items = msg.closed_edges.size();
      for (auto item : msg.closed_edges) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: opened_edges
  {
    if (msg.opened_edges.size() == 0) {
      out << "opened_edges: []";
    } else {
      out << "opened_edges: [";
      size_t pending_items = msg.opened_edges.size();
      for (auto item : msg.opened_edges) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: adjust_edges
  {
    if (msg.adjust_edges.size() == 0) {
      out << "adjust_edges: []";
    } else {
      out << "adjust_edges: [";
      size_t pending_items = msg.adjust_edges.size();
      for (auto item : msg.adjust_edges) {
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
  const DynamicEdges_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: closed_edges
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.closed_edges.size() == 0) {
      out << "closed_edges: []\n";
    } else {
      out << "closed_edges:\n";
      for (auto item : msg.closed_edges) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: opened_edges
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.opened_edges.size() == 0) {
      out << "opened_edges: []\n";
    } else {
      out << "opened_edges:\n";
      for (auto item : msg.opened_edges) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: adjust_edges
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.adjust_edges.size() == 0) {
      out << "adjust_edges: []\n";
    } else {
      out << "adjust_edges:\n";
      for (auto item : msg.adjust_edges) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DynamicEdges_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::DynamicEdges_Request>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).closed_edges,
    std::forward<T>(msg).opened_edges,
    std::forward<T>(msg).adjust_edges);
}

}  // namespace srv

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::srv::DynamicEdges_Request>()
{
  return "nav2_msgs::srv::DynamicEdges_Request";
}

template<>
constexpr const char * name<nav2_msgs::srv::DynamicEdges_Request>()
{
  return "nav2_msgs/srv/DynamicEdges_Request";
}

template<>
struct has_fixed_size<nav2_msgs::srv::DynamicEdges_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::srv::DynamicEdges_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::srv::DynamicEdges_Request>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::DynamicEdges_Request>
{
  static constexpr std::size_t member_count = 3;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "closed_edges",
    "opened_edges",
    "adjust_edges",
  };
};

}  // namespace rosidl_generator_traits

namespace nav2_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const DynamicEdges_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const DynamicEdges_Response & msg,
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
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const DynamicEdges_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::DynamicEdges_Response>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(std::forward<T>(msg).success);
}

}  // namespace srv

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::srv::DynamicEdges_Response>()
{
  return "nav2_msgs::srv::DynamicEdges_Response";
}

template<>
constexpr const char * name<nav2_msgs::srv::DynamicEdges_Response>()
{
  return "nav2_msgs/srv/DynamicEdges_Response";
}

template<>
struct has_fixed_size<nav2_msgs::srv::DynamicEdges_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<nav2_msgs::srv::DynamicEdges_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<nav2_msgs::srv::DynamicEdges_Response>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::DynamicEdges_Response>
{
  static constexpr std::size_t member_count = 1;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "success",
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
  const DynamicEdges_Event & msg,
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
  const DynamicEdges_Event & msg,
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

inline std::string to_yaml(const DynamicEdges_Event & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::srv::DynamicEdges_Event>, int> = 0>
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
constexpr const char * data_type<nav2_msgs::srv::DynamicEdges_Event>()
{
  return "nav2_msgs::srv::DynamicEdges_Event";
}

template<>
constexpr const char * name<nav2_msgs::srv::DynamicEdges_Event>()
{
  return "nav2_msgs/srv/DynamicEdges_Event";
}

template<>
struct has_fixed_size<nav2_msgs::srv::DynamicEdges_Event>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::srv::DynamicEdges_Event>
  : std::integral_constant<bool, has_bounded_size<nav2_msgs::srv::DynamicEdges_Request>::value && has_bounded_size<nav2_msgs::srv::DynamicEdges_Response>::value && has_bounded_size<service_msgs::msg::ServiceEventInfo>::value> {};

template<>
struct is_message<nav2_msgs::srv::DynamicEdges_Event>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::srv::DynamicEdges_Event>
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
constexpr const char * data_type<nav2_msgs::srv::DynamicEdges>()
{
  return "nav2_msgs::srv::DynamicEdges";
}

template<>
constexpr const char * name<nav2_msgs::srv::DynamicEdges>()
{
  return "nav2_msgs/srv/DynamicEdges";
}

template<>
struct has_fixed_size<nav2_msgs::srv::DynamicEdges>
  : std::integral_constant<
    bool,
    has_fixed_size<nav2_msgs::srv::DynamicEdges_Request>::value &&
    has_fixed_size<nav2_msgs::srv::DynamicEdges_Response>::value
  >
{
};

template<>
struct has_bounded_size<nav2_msgs::srv::DynamicEdges>
  : std::integral_constant<
    bool,
    has_bounded_size<nav2_msgs::srv::DynamicEdges_Request>::value &&
    has_bounded_size<nav2_msgs::srv::DynamicEdges_Response>::value
  >
{
};

template<>
struct is_service<nav2_msgs::srv::DynamicEdges>
  : std::true_type
{
};

template<>
struct is_service_request<nav2_msgs::srv::DynamicEdges_Request>
  : std::true_type
{
};

template<>
struct is_service_response<nav2_msgs::srv::DynamicEdges_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__SRV__DETAIL__DYNAMIC_EDGES__TRAITS_HPP_
