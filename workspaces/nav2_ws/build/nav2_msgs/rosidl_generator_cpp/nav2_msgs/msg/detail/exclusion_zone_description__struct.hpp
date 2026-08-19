// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from nav2_msgs:msg/ExclusionZoneDescription.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/exclusion_zone_description.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__STRUCT_HPP_
#define NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_buffer/buffer.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'points'
#include "geometry_msgs/msg/detail/point32__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__nav2_msgs__msg__ExclusionZoneDescription __attribute__((deprecated))
#else
# define DEPRECATED__nav2_msgs__msg__ExclusionZoneDescription __declspec(deprecated)
#endif

namespace nav2_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ExclusionZoneDescription_
{
  using Type = ExclusionZoneDescription_<ContainerAllocator>;

  explicit ExclusionZoneDescription_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->radius = 0.0;
      this->min_height = -1.7976931348623157e+308;
      this->max_height = 1.7976931348623157e+308;
      this->enabled = true;
      this->visualize = false;
      this->frame_hold_timeout = 0.0;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->zone_name = "";
      this->type = "";
      this->frame_id = "";
      this->radius = 0.0;
      this->min_height = 0.0;
      this->max_height = 0.0;
      this->enabled = false;
      this->visualize = false;
      this->frame_hold_timeout = 0.0;
    }
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->zone_name = "";
      this->type = "";
      this->frame_id = "";
    }
  }

  explicit ExclusionZoneDescription_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : zone_name(_alloc),
    type(_alloc),
    frame_id(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::DEFAULTS_ONLY == _init)
    {
      this->radius = 0.0;
      this->min_height = -1.7976931348623157e+308;
      this->max_height = 1.7976931348623157e+308;
      this->enabled = true;
      this->visualize = false;
      this->frame_hold_timeout = 0.0;
    } else if (rosidl_runtime_cpp::MessageInitialization::ZERO == _init) {
      this->zone_name = "";
      this->type = "";
      this->frame_id = "";
      this->radius = 0.0;
      this->min_height = 0.0;
      this->max_height = 0.0;
      this->enabled = false;
      this->visualize = false;
      this->frame_hold_timeout = 0.0;
    }
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->zone_name = "";
      this->type = "";
      this->frame_id = "";
    }
  }

  // field types and members
  using _zone_name_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _zone_name_type zone_name;
  using _type_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _type_type type;
  using _frame_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _frame_id_type frame_id;
  using _points_type =
    std::vector<geometry_msgs::msg::Point32_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<geometry_msgs::msg::Point32_<ContainerAllocator>>>;
  _points_type points;
  using _radius_type =
    double;
  _radius_type radius;
  using _min_height_type =
    double;
  _min_height_type min_height;
  using _max_height_type =
    double;
  _max_height_type max_height;
  using _enabled_type =
    bool;
  _enabled_type enabled;
  using _visualize_type =
    bool;
  _visualize_type visualize;
  using _frame_hold_timeout_type =
    double;
  _frame_hold_timeout_type frame_hold_timeout;

  // setters for named parameter idiom
  Type & set__zone_name(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->zone_name = _arg;
    return *this;
  }
  Type & set__type(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->type = _arg;
    return *this;
  }
  Type & set__frame_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->frame_id = _arg;
    return *this;
  }
  Type & set__points(
    const std::vector<geometry_msgs::msg::Point32_<ContainerAllocator>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<geometry_msgs::msg::Point32_<ContainerAllocator>>> & _arg)
  {
    this->points = _arg;
    return *this;
  }
  Type & set__radius(
    const double & _arg)
  {
    this->radius = _arg;
    return *this;
  }
  Type & set__min_height(
    const double & _arg)
  {
    this->min_height = _arg;
    return *this;
  }
  Type & set__max_height(
    const double & _arg)
  {
    this->max_height = _arg;
    return *this;
  }
  Type & set__enabled(
    const bool & _arg)
  {
    this->enabled = _arg;
    return *this;
  }
  Type & set__visualize(
    const bool & _arg)
  {
    this->visualize = _arg;
    return *this;
  }
  Type & set__frame_hold_timeout(
    const double & _arg)
  {
    this->frame_hold_timeout = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator> *;
  using ConstRawPtr =
    const nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__nav2_msgs__msg__ExclusionZoneDescription
    std::shared_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__nav2_msgs__msg__ExclusionZoneDescription
    std::shared_ptr<nav2_msgs::msg::ExclusionZoneDescription_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ExclusionZoneDescription_ & other) const
  {
    if (this->zone_name != other.zone_name) {
      return false;
    }
    if (this->type != other.type) {
      return false;
    }
    if (this->frame_id != other.frame_id) {
      return false;
    }
    if (this->points != other.points) {
      return false;
    }
    if (this->radius != other.radius) {
      return false;
    }
    if (this->min_height != other.min_height) {
      return false;
    }
    if (this->max_height != other.max_height) {
      return false;
    }
    if (this->enabled != other.enabled) {
      return false;
    }
    if (this->visualize != other.visualize) {
      return false;
    }
    if (this->frame_hold_timeout != other.frame_hold_timeout) {
      return false;
    }
    return true;
  }
  bool operator!=(const ExclusionZoneDescription_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ExclusionZoneDescription_

// alias to use template instance with default allocator
using ExclusionZoneDescription =
  nav2_msgs::msg::ExclusionZoneDescription_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace nav2_msgs

#endif  // NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__STRUCT_HPP_
