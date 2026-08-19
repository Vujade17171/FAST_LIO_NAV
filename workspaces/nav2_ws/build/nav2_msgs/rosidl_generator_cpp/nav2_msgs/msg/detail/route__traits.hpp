// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from nav2_msgs:msg/Route.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/route.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__ROUTE__TRAITS_HPP_
#define NAV2_MSGS__MSG__DETAIL__ROUTE__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "nav2_msgs/msg/detail/route__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"
// Member 'nodes'
#include "nav2_msgs/msg/detail/route_node__traits.hpp"
// Member 'edges'
#include "nav2_msgs/msg/detail/route_edge__traits.hpp"

namespace nav2_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Route & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: route_cost
  {
    out << "route_cost: ";
    rosidl_generator_traits::value_to_yaml(msg.route_cost, out);
    out << ", ";
  }

  // member: nodes
  {
    if (msg.nodes.size() == 0) {
      out << "nodes: []";
    } else {
      out << "nodes: [";
      size_t pending_items = msg.nodes.size();
      for (auto item : msg.nodes) {
        to_flow_style_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: edges
  {
    if (msg.edges.size() == 0) {
      out << "edges: []";
    } else {
      out << "edges: [";
      size_t pending_items = msg.edges.size();
      for (auto item : msg.edges) {
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
  const Route & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: route_cost
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "route_cost: ";
    rosidl_generator_traits::value_to_yaml(msg.route_cost, out);
    out << "\n";
  }

  // member: nodes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.nodes.size() == 0) {
      out << "nodes: []\n";
    } else {
      out << "nodes:\n";
      for (auto item : msg.nodes) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }

  // member: edges
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.edges.size() == 0) {
      out << "edges: []\n";
    } else {
      out << "edges:\n";
      for (auto item : msg.edges) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "-\n";
        to_block_style_yaml(item, out, indentation + 2);
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Route & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, nav2_msgs::msg::Route>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).header,
    std::forward<T>(msg).route_cost,
    std::forward<T>(msg).nodes,
    std::forward<T>(msg).edges);
}

}  // namespace msg

}  // namespace nav2_msgs

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<nav2_msgs::msg::Route>()
{
  return "nav2_msgs::msg::Route";
}

template<>
constexpr const char * name<nav2_msgs::msg::Route>()
{
  return "nav2_msgs/msg/Route";
}

template<>
struct has_fixed_size<nav2_msgs::msg::Route>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<nav2_msgs::msg::Route>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<nav2_msgs::msg::Route>
  : std::true_type {};

template<>
struct MessageTraits<nav2_msgs::msg::Route>
{
  static constexpr std::size_t member_count = 4;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "header",
    "route_cost",
    "nodes",
    "edges",
  };
};

}  // namespace rosidl_generator_traits

#endif  // NAV2_MSGS__MSG__DETAIL__ROUTE__TRAITS_HPP_
