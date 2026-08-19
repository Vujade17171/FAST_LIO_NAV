// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from fast_lio:msg/Pose6D.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "fast_lio/msg/pose6_d.hpp"


#ifndef FAST_LIO__MSG__DETAIL__POSE6_D__TRAITS_HPP_
#define FAST_LIO__MSG__DETAIL__POSE6_D__TRAITS_HPP_

#include <stdint.h>

#include <array>
#include <cstddef>
#include <sstream>
#include <string>
#include <string_view>
#include <tuple>
#include <type_traits>
#include <utility>

#include "fast_lio/msg/detail/pose6_d__struct.hpp"
#include "rosidl_runtime_cpp/buffer__traits.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace fast_lio
{

namespace msg
{

inline void to_flow_style_yaml(
  const Pose6D & msg,
  std::ostream & out)
{
  out << "{";
  // member: offset_time
  {
    out << "offset_time: ";
    rosidl_generator_traits::value_to_yaml(msg.offset_time, out);
    out << ", ";
  }

  // member: acc
  {
    if (msg.acc.size() == 0) {
      out << "acc: []";
    } else {
      out << "acc: [";
      size_t pending_items = msg.acc.size();
      for (auto item : msg.acc) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: gyr
  {
    if (msg.gyr.size() == 0) {
      out << "gyr: []";
    } else {
      out << "gyr: [";
      size_t pending_items = msg.gyr.size();
      for (auto item : msg.gyr) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: vel
  {
    if (msg.vel.size() == 0) {
      out << "vel: []";
    } else {
      out << "vel: [";
      size_t pending_items = msg.vel.size();
      for (auto item : msg.vel) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: pos
  {
    if (msg.pos.size() == 0) {
      out << "pos: []";
    } else {
      out << "pos: [";
      size_t pending_items = msg.pos.size();
      for (auto item : msg.pos) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
    out << ", ";
  }

  // member: rot
  {
    if (msg.rot.size() == 0) {
      out << "rot: []";
    } else {
      out << "rot: [";
      size_t pending_items = msg.rot.size();
      for (auto item : msg.rot) {
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
  const Pose6D & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: offset_time
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "offset_time: ";
    rosidl_generator_traits::value_to_yaml(msg.offset_time, out);
    out << "\n";
  }

  // member: acc
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.acc.size() == 0) {
      out << "acc: []\n";
    } else {
      out << "acc:\n";
      for (auto item : msg.acc) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: gyr
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.gyr.size() == 0) {
      out << "gyr: []\n";
    } else {
      out << "gyr:\n";
      for (auto item : msg.gyr) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: vel
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.vel.size() == 0) {
      out << "vel: []\n";
    } else {
      out << "vel:\n";
      for (auto item : msg.vel) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: pos
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.pos.size() == 0) {
      out << "pos: []\n";
    } else {
      out << "pos:\n";
      for (auto item : msg.pos) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }

  // member: rot
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.rot.size() == 0) {
      out << "rot: []\n";
    } else {
      out << "rot:\n";
      for (auto item : msg.rot) {
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

inline std::string to_yaml(const Pose6D & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

template<typename T, std::enable_if_t<std::is_same_v<std::decay_t<T>, fast_lio::msg::Pose6D>, int> = 0>
constexpr auto as_tuple_ref(T && msg)
{
  return std::forward_as_tuple(
    std::forward<T>(msg).offset_time,
    std::forward<T>(msg).acc,
    std::forward<T>(msg).gyr,
    std::forward<T>(msg).vel,
    std::forward<T>(msg).pos,
    std::forward<T>(msg).rot);
}

}  // namespace msg

}  // namespace fast_lio

namespace rosidl_generator_traits
{

template<>
constexpr const char * data_type<fast_lio::msg::Pose6D>()
{
  return "fast_lio::msg::Pose6D";
}

template<>
constexpr const char * name<fast_lio::msg::Pose6D>()
{
  return "fast_lio/msg/Pose6D";
}

template<>
struct has_fixed_size<fast_lio::msg::Pose6D>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<fast_lio::msg::Pose6D>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<fast_lio::msg::Pose6D>
  : std::true_type {};

template<>
struct MessageTraits<fast_lio::msg::Pose6D>
{
  static constexpr std::size_t member_count = 6;
  static constexpr std::array<std::string_view, member_count> member_names = {
    "offset_time",
    "acc",
    "gyr",
    "vel",
    "pos",
    "rot",
  };
};

}  // namespace rosidl_generator_traits

#endif  // FAST_LIO__MSG__DETAIL__POSE6_D__TRAITS_HPP_
