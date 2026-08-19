// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from nav2_msgs:msg/ExclusionZoneDescription.idl
// generated code does not contain a copyright notice

#include "nav2_msgs/msg/detail/exclusion_zone_description__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_nav2_msgs
const rosidl_type_hash_t *
nav2_msgs__msg__ExclusionZoneDescription__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xf9, 0xad, 0xdb, 0xb3, 0xb5, 0xa2, 0x1a, 0x61,
      0x85, 0x6c, 0x99, 0x14, 0xd7, 0x45, 0xc8, 0xcd,
      0x6f, 0xdc, 0x98, 0x39, 0xf5, 0x8d, 0x8e, 0x91,
      0xe9, 0x28, 0xc3, 0x8e, 0xc9, 0xe1, 0xdb, 0x19,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "geometry_msgs/msg/detail/point32__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t geometry_msgs__msg__Point32__EXPECTED_HASH = {1, {
    0x2f, 0xc4, 0xdb, 0x7c, 0xae, 0x16, 0xa4, 0x58,
    0x2c, 0x79, 0xa5, 0x6b, 0x66, 0x17, 0x3a, 0x8d,
    0x48, 0xd5, 0x2c, 0x7d, 0xc5, 0x20, 0xdd, 0xc5,
    0x5a, 0x0d, 0x4b, 0xcf, 0x2a, 0x4b, 0xfd, 0xbc,
  }};
#endif

static char nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME[] = "nav2_msgs/msg/ExclusionZoneDescription";
static char geometry_msgs__msg__Point32__TYPE_NAME[] = "geometry_msgs/msg/Point32";

// Define type names, field names, and default values
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__zone_name[] = "zone_name";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__type[] = "type";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__frame_id[] = "frame_id";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__points[] = "points";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__radius[] = "radius";
static char nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__radius[] = "0.0";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__min_height[] = "min_height";
static char nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__min_height[] = "-1.7976931348623157e+308";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__max_height[] = "max_height";
static char nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__max_height[] = "1.7976931348623157e+308";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__enabled[] = "enabled";
static char nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__enabled[] = "True";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__visualize[] = "visualize";
static char nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__visualize[] = "False";
static char nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__frame_hold_timeout[] = "frame_hold_timeout";
static char nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__frame_hold_timeout[] = "0.0";

static rosidl_runtime_c__type_description__Field nav2_msgs__msg__ExclusionZoneDescription__FIELDS[] = {
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__zone_name, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__type, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__frame_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__points, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_UNBOUNDED_SEQUENCE,
      0,
      0,
      {geometry_msgs__msg__Point32__TYPE_NAME, 25, 25},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__radius, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__radius, 3, 3},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__min_height, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__min_height, 24, 24},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__max_height, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__max_height, 23, 23},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__enabled, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__enabled, 4, 4},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__visualize, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__visualize, 5, 5},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__FIELD_NAME__frame_hold_timeout, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {nav2_msgs__msg__ExclusionZoneDescription__DEFAULT_VALUE__frame_hold_timeout, 3, 3},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription nav2_msgs__msg__ExclusionZoneDescription__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {geometry_msgs__msg__Point32__TYPE_NAME, 25, 25},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
nav2_msgs__msg__ExclusionZoneDescription__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME, 38, 38},
      {nav2_msgs__msg__ExclusionZoneDescription__FIELDS, 10, 10},
    },
    {nav2_msgs__msg__ExclusionZoneDescription__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&geometry_msgs__msg__Point32__EXPECTED_HASH, geometry_msgs__msg__Point32__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = geometry_msgs__msg__Point32__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# Description of an exclusion zone for the collision monitor / detector.\n"
  "# Used by the AddExclusionZone service to add zones at runtime.\n"
  "\n"
  "string zone_name                                    # Unique name within the source\n"
  "string type                                         # \"polygon\" or \"circle\"\n"
  "string frame_id                                     # TF frame the zone is anchored to (empty = base_frame_id)\n"
  "geometry_msgs/Point32[] points                      # Polygon vertices in frame_id (ignored for circle)\n"
  "float64 radius 0.0                                  # Circle radius in metres (ignored for polygon)\n"
  "float64 min_height -1.7976931348623158e+308          # Lower z-bound in base frame (default: -DBL_MAX)\n"
  "float64 max_height 1.7976931348623158e+308           # Upper z-bound in base frame (default: +DBL_MAX)\n"
  "bool enabled true                                   # Whether zone is active on creation\n"
  "bool visualize false                                # Whether to publish the zone polygon for rviz\n"
  "float64 frame_hold_timeout 0.0                      # Extra staleness allowance (seconds)";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
nav2_msgs__msg__ExclusionZoneDescription__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME, 38, 38},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 1097, 1097},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
nav2_msgs__msg__ExclusionZoneDescription__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *nav2_msgs__msg__ExclusionZoneDescription__get_individual_type_description_source(NULL),
    sources[1] = *geometry_msgs__msg__Point32__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
