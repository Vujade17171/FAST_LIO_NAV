// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from nav2_msgs:srv/RemoveExclusionZone.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/srv/remove_exclusion_zone.h"


#ifndef NAV2_MSGS__SRV__DETAIL__REMOVE_EXCLUSION_ZONE__STRUCT_H_
#define NAV2_MSGS__SRV__DETAIL__REMOVE_EXCLUSION_ZONE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'zone_name'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/RemoveExclusionZone in the package nav2_msgs.
typedef struct nav2_msgs__srv__RemoveExclusionZone_Request
{
  /// Name of zone to remove (ignored if remove_all is true)
  rosidl_runtime_c__String zone_name;
  /// If true, remove all zones from this source
  bool remove_all;
} nav2_msgs__srv__RemoveExclusionZone_Request;

// Struct for a sequence of nav2_msgs__srv__RemoveExclusionZone_Request.
typedef struct nav2_msgs__srv__RemoveExclusionZone_Request__Sequence
{
  nav2_msgs__srv__RemoveExclusionZone_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} nav2_msgs__srv__RemoveExclusionZone_Request__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'message'
// already included above
// #include "rosidl_runtime_c/string.h"

/// Struct defined in srv/RemoveExclusionZone in the package nav2_msgs.
typedef struct nav2_msgs__srv__RemoveExclusionZone_Response
{
  bool success;
  rosidl_runtime_c__String message;
} nav2_msgs__srv__RemoveExclusionZone_Response;

// Struct for a sequence of nav2_msgs__srv__RemoveExclusionZone_Response.
typedef struct nav2_msgs__srv__RemoveExclusionZone_Response__Sequence
{
  nav2_msgs__srv__RemoveExclusionZone_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} nav2_msgs__srv__RemoveExclusionZone_Response__Sequence;

// Constants defined in the message

// Include directives for member types
// Member 'info'
#include "service_msgs/msg/detail/service_event_info__struct.h"

// constants for array fields with an upper bound
// request
enum
{
  nav2_msgs__srv__RemoveExclusionZone_Event__request__MAX_SIZE = 1
};
// response
enum
{
  nav2_msgs__srv__RemoveExclusionZone_Event__response__MAX_SIZE = 1
};

/// Struct defined in srv/RemoveExclusionZone in the package nav2_msgs.
typedef struct nav2_msgs__srv__RemoveExclusionZone_Event
{
  service_msgs__msg__ServiceEventInfo info;
  nav2_msgs__srv__RemoveExclusionZone_Request__Sequence request;
  nav2_msgs__srv__RemoveExclusionZone_Response__Sequence response;
} nav2_msgs__srv__RemoveExclusionZone_Event;

// Struct for a sequence of nav2_msgs__srv__RemoveExclusionZone_Event.
typedef struct nav2_msgs__srv__RemoveExclusionZone_Event__Sequence
{
  nav2_msgs__srv__RemoveExclusionZone_Event * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} nav2_msgs__srv__RemoveExclusionZone_Event__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // NAV2_MSGS__SRV__DETAIL__REMOVE_EXCLUSION_ZONE__STRUCT_H_
