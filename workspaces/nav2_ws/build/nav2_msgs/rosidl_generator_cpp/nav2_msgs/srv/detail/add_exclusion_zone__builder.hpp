// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from nav2_msgs:srv/AddExclusionZone.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/srv/add_exclusion_zone.hpp"


#ifndef NAV2_MSGS__SRV__DETAIL__ADD_EXCLUSION_ZONE__BUILDER_HPP_
#define NAV2_MSGS__SRV__DETAIL__ADD_EXCLUSION_ZONE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "nav2_msgs/srv/detail/add_exclusion_zone__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace nav2_msgs
{

namespace srv
{

namespace builder
{

class Init_AddExclusionZone_Request_zone
{
public:
  Init_AddExclusionZone_Request_zone()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::nav2_msgs::srv::AddExclusionZone_Request zone(::nav2_msgs::srv::AddExclusionZone_Request::_zone_type arg)
  {
    msg_.zone = std::move(arg);
    return std::move(msg_);
  }

private:
  ::nav2_msgs::srv::AddExclusionZone_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::nav2_msgs::srv::AddExclusionZone_Request>()
{
  return nav2_msgs::srv::builder::Init_AddExclusionZone_Request_zone();
}

}  // namespace nav2_msgs


namespace nav2_msgs
{

namespace srv
{

namespace builder
{

class Init_AddExclusionZone_Response_message
{
public:
  explicit Init_AddExclusionZone_Response_message(::nav2_msgs::srv::AddExclusionZone_Response & msg)
  : msg_(msg)
  {}
  ::nav2_msgs::srv::AddExclusionZone_Response message(::nav2_msgs::srv::AddExclusionZone_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::nav2_msgs::srv::AddExclusionZone_Response msg_;
};

class Init_AddExclusionZone_Response_success
{
public:
  Init_AddExclusionZone_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddExclusionZone_Response_message success(::nav2_msgs::srv::AddExclusionZone_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_AddExclusionZone_Response_message(msg_);
  }

private:
  ::nav2_msgs::srv::AddExclusionZone_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::nav2_msgs::srv::AddExclusionZone_Response>()
{
  return nav2_msgs::srv::builder::Init_AddExclusionZone_Response_success();
}

}  // namespace nav2_msgs


namespace nav2_msgs
{

namespace srv
{

namespace builder
{

class Init_AddExclusionZone_Event_response
{
public:
  explicit Init_AddExclusionZone_Event_response(::nav2_msgs::srv::AddExclusionZone_Event & msg)
  : msg_(msg)
  {}
  ::nav2_msgs::srv::AddExclusionZone_Event response(::nav2_msgs::srv::AddExclusionZone_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::nav2_msgs::srv::AddExclusionZone_Event msg_;
};

class Init_AddExclusionZone_Event_request
{
public:
  explicit Init_AddExclusionZone_Event_request(::nav2_msgs::srv::AddExclusionZone_Event & msg)
  : msg_(msg)
  {}
  Init_AddExclusionZone_Event_response request(::nav2_msgs::srv::AddExclusionZone_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_AddExclusionZone_Event_response(msg_);
  }

private:
  ::nav2_msgs::srv::AddExclusionZone_Event msg_;
};

class Init_AddExclusionZone_Event_info
{
public:
  Init_AddExclusionZone_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AddExclusionZone_Event_request info(::nav2_msgs::srv::AddExclusionZone_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_AddExclusionZone_Event_request(msg_);
  }

private:
  ::nav2_msgs::srv::AddExclusionZone_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::nav2_msgs::srv::AddExclusionZone_Event>()
{
  return nav2_msgs::srv::builder::Init_AddExclusionZone_Event_info();
}

}  // namespace nav2_msgs

#endif  // NAV2_MSGS__SRV__DETAIL__ADD_EXCLUSION_ZONE__BUILDER_HPP_
