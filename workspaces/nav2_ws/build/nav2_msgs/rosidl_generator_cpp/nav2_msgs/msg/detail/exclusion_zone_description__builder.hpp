// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from nav2_msgs:msg/ExclusionZoneDescription.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/exclusion_zone_description.hpp"


#ifndef NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__BUILDER_HPP_
#define NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "nav2_msgs/msg/detail/exclusion_zone_description__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace nav2_msgs
{

namespace msg
{

namespace builder
{

class Init_ExclusionZoneDescription_frame_hold_timeout
{
public:
  explicit Init_ExclusionZoneDescription_frame_hold_timeout(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  ::nav2_msgs::msg::ExclusionZoneDescription frame_hold_timeout(::nav2_msgs::msg::ExclusionZoneDescription::_frame_hold_timeout_type arg)
  {
    msg_.frame_hold_timeout = std::move(arg);
    return std::move(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_visualize
{
public:
  explicit Init_ExclusionZoneDescription_visualize(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_frame_hold_timeout visualize(::nav2_msgs::msg::ExclusionZoneDescription::_visualize_type arg)
  {
    msg_.visualize = std::move(arg);
    return Init_ExclusionZoneDescription_frame_hold_timeout(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_enabled
{
public:
  explicit Init_ExclusionZoneDescription_enabled(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_visualize enabled(::nav2_msgs::msg::ExclusionZoneDescription::_enabled_type arg)
  {
    msg_.enabled = std::move(arg);
    return Init_ExclusionZoneDescription_visualize(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_max_height
{
public:
  explicit Init_ExclusionZoneDescription_max_height(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_enabled max_height(::nav2_msgs::msg::ExclusionZoneDescription::_max_height_type arg)
  {
    msg_.max_height = std::move(arg);
    return Init_ExclusionZoneDescription_enabled(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_min_height
{
public:
  explicit Init_ExclusionZoneDescription_min_height(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_max_height min_height(::nav2_msgs::msg::ExclusionZoneDescription::_min_height_type arg)
  {
    msg_.min_height = std::move(arg);
    return Init_ExclusionZoneDescription_max_height(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_radius
{
public:
  explicit Init_ExclusionZoneDescription_radius(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_min_height radius(::nav2_msgs::msg::ExclusionZoneDescription::_radius_type arg)
  {
    msg_.radius = std::move(arg);
    return Init_ExclusionZoneDescription_min_height(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_points
{
public:
  explicit Init_ExclusionZoneDescription_points(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_radius points(::nav2_msgs::msg::ExclusionZoneDescription::_points_type arg)
  {
    msg_.points = std::move(arg);
    return Init_ExclusionZoneDescription_radius(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_frame_id
{
public:
  explicit Init_ExclusionZoneDescription_frame_id(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_points frame_id(::nav2_msgs::msg::ExclusionZoneDescription::_frame_id_type arg)
  {
    msg_.frame_id = std::move(arg);
    return Init_ExclusionZoneDescription_points(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_type
{
public:
  explicit Init_ExclusionZoneDescription_type(::nav2_msgs::msg::ExclusionZoneDescription & msg)
  : msg_(msg)
  {}
  Init_ExclusionZoneDescription_frame_id type(::nav2_msgs::msg::ExclusionZoneDescription::_type_type arg)
  {
    msg_.type = std::move(arg);
    return Init_ExclusionZoneDescription_frame_id(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

class Init_ExclusionZoneDescription_zone_name
{
public:
  Init_ExclusionZoneDescription_zone_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ExclusionZoneDescription_type zone_name(::nav2_msgs::msg::ExclusionZoneDescription::_zone_name_type arg)
  {
    msg_.zone_name = std::move(arg);
    return Init_ExclusionZoneDescription_type(msg_);
  }

private:
  ::nav2_msgs::msg::ExclusionZoneDescription msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::nav2_msgs::msg::ExclusionZoneDescription>()
{
  return nav2_msgs::msg::builder::Init_ExclusionZoneDescription_zone_name();
}

}  // namespace nav2_msgs

#endif  // NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__BUILDER_HPP_
