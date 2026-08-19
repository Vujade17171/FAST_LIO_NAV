// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from nav2_msgs:msg/ExclusionZoneDescription.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "nav2_msgs/msg/detail/exclusion_zone_description__rosidl_typesupport_introspection_c.h"
#include "nav2_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "nav2_msgs/msg/detail/exclusion_zone_description__functions.h"
#include "nav2_msgs/msg/detail/exclusion_zone_description__struct.h"


// Include directives for member types
// Member `zone_name`
// Member `type`
// Member `frame_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `points`
#include "geometry_msgs/msg/point32.h"
// Member `points`
#include "geometry_msgs/msg/detail/point32__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  nav2_msgs__msg__ExclusionZoneDescription__init(message_memory);
}

void nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_fini_function(void * message_memory)
{
  nav2_msgs__msg__ExclusionZoneDescription__fini(message_memory);
}

size_t nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__size_function__ExclusionZoneDescription__points(
  const void * untyped_member)
{
  const geometry_msgs__msg__Point32__Sequence * member =
    (const geometry_msgs__msg__Point32__Sequence *)(untyped_member);
  return member->size;
}

const void * nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__get_const_function__ExclusionZoneDescription__points(
  const void * untyped_member, size_t index)
{
  const geometry_msgs__msg__Point32__Sequence * member =
    (const geometry_msgs__msg__Point32__Sequence *)(untyped_member);
  return &member->data[index];
}

void * nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__get_function__ExclusionZoneDescription__points(
  void * untyped_member, size_t index)
{
  geometry_msgs__msg__Point32__Sequence * member =
    (geometry_msgs__msg__Point32__Sequence *)(untyped_member);
  return &member->data[index];
}

void nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__fetch_function__ExclusionZoneDescription__points(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const geometry_msgs__msg__Point32 * item =
    ((const geometry_msgs__msg__Point32 *)
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__get_const_function__ExclusionZoneDescription__points(untyped_member, index));
  geometry_msgs__msg__Point32 * value =
    (geometry_msgs__msg__Point32 *)(untyped_value);
  *value = *item;
}

void nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__assign_function__ExclusionZoneDescription__points(
  void * untyped_member, size_t index, const void * untyped_value)
{
  geometry_msgs__msg__Point32 * item =
    ((geometry_msgs__msg__Point32 *)
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__get_function__ExclusionZoneDescription__points(untyped_member, index));
  const geometry_msgs__msg__Point32 * value =
    (const geometry_msgs__msg__Point32 *)(untyped_value);
  *item = *value;
}

bool nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__resize_function__ExclusionZoneDescription__points(
  void * untyped_member, size_t size)
{
  geometry_msgs__msg__Point32__Sequence * member =
    (geometry_msgs__msg__Point32__Sequence *)(untyped_member);
  geometry_msgs__msg__Point32__Sequence__fini(member);
  return geometry_msgs__msg__Point32__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_member_array[10] = {
  {
    "zone_name",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, zone_name),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "type",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, type),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "frame_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, frame_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "points",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is key
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, points),  // bytes offset in struct
    NULL,  // default value
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__size_function__ExclusionZoneDescription__points,  // size() function pointer
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__get_const_function__ExclusionZoneDescription__points,  // get_const(index) function pointer
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__get_function__ExclusionZoneDescription__points,  // get(index) function pointer
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__fetch_function__ExclusionZoneDescription__points,  // fetch(index, &value) function pointer
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__assign_function__ExclusionZoneDescription__points,  // assign(index, value) function pointer
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__resize_function__ExclusionZoneDescription__points,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "radius",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, radius),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "min_height",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, min_height),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "max_height",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, max_height),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "enabled",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, enabled),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "visualize",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, visualize),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  },
  {
    "frame_hold_timeout",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_DOUBLE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(nav2_msgs__msg__ExclusionZoneDescription, frame_hold_timeout),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL,  // resize(index) function pointer
    false  // is_rosidl_buffer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_members = {
  "nav2_msgs__msg",  // message namespace
  "ExclusionZoneDescription",  // message name
  10,  // number of fields
  sizeof(nav2_msgs__msg__ExclusionZoneDescription),
  false,  // has_any_key_member_
  nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_member_array,  // message members
  nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_init_function,  // function to initialize message memory (memory has to be allocated)
  nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_type_support_handle = {
  0,
  &nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_members,
  get_message_typesupport_handle_function,
  &nav2_msgs__msg__ExclusionZoneDescription__get_type_hash,
  &nav2_msgs__msg__ExclusionZoneDescription__get_type_description,
  &nav2_msgs__msg__ExclusionZoneDescription__get_type_description_sources,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_nav2_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, nav2_msgs, msg, ExclusionZoneDescription)() {
  nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_member_array[3].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, Point32)();
  if (!nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_type_support_handle.typesupport_identifier) {
    nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &nav2_msgs__msg__ExclusionZoneDescription__rosidl_typesupport_introspection_c__ExclusionZoneDescription_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
