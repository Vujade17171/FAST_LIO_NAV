// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from nav2_msgs:msg/ExclusionZoneDescription.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "nav2_msgs/msg/exclusion_zone_description.h"


#ifndef NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__STRUCT_H_
#define NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__STRUCT_H_

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
// Member 'type'
// Member 'frame_id'
#include "rosidl_runtime_c/string.h"
// Member 'points'
#include "geometry_msgs/msg/detail/point32__struct.h"

/// Struct defined in msg/ExclusionZoneDescription in the package nav2_msgs.
/**
  * Description of an exclusion zone for the collision monitor / detector.
  * Used by the AddExclusionZone service to add zones at runtime.
 */
typedef struct nav2_msgs__msg__ExclusionZoneDescription
{
  /// Unique name within the source
  rosidl_runtime_c__String zone_name;
  /// "polygon" or "circle"
  rosidl_runtime_c__String type;
  /// TF frame the zone is anchored to (empty = base_frame_id)
  rosidl_runtime_c__String frame_id;
  /// Polygon vertices in frame_id (ignored for circle)
  geometry_msgs__msg__Point32__Sequence points;
  /// Circle radius in metres (ignored for polygon)
  double radius;
  /// Lower z-bound in base frame (default: -DBL_MAX)
  double min_height;
  /// Upper z-bound in base frame (default: +DBL_MAX)
  double max_height;
  /// Whether zone is active on creation
  bool enabled;
  /// Whether to publish the zone polygon for rviz
  bool visualize;
  /// Extra staleness allowance (seconds)
  double frame_hold_timeout;
} nav2_msgs__msg__ExclusionZoneDescription;

// Struct for a sequence of nav2_msgs__msg__ExclusionZoneDescription.
typedef struct nav2_msgs__msg__ExclusionZoneDescription__Sequence
{
  nav2_msgs__msg__ExclusionZoneDescription * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} nav2_msgs__msg__ExclusionZoneDescription__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // NAV2_MSGS__MSG__DETAIL__EXCLUSION_ZONE_DESCRIPTION__STRUCT_H_
