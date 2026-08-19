// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from nav2_msgs:srv/AddExclusionZone.idl
// generated code does not contain a copyright notice

#include "nav2_msgs/srv/detail/add_exclusion_zone__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_nav2_msgs
const rosidl_type_hash_t *
nav2_msgs__srv__AddExclusionZone__get_type_hash(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x1c, 0x40, 0x8a, 0x3f, 0xcf, 0x9a, 0xdf, 0xc2,
      0x7e, 0x7f, 0x98, 0x86, 0xb0, 0xc8, 0x42, 0x54,
      0x7c, 0xb8, 0xa7, 0xb0, 0x7f, 0xe1, 0x4b, 0x06,
      0xc1, 0xfa, 0x3e, 0x82, 0x56, 0x3b, 0x08, 0x61,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_nav2_msgs
const rosidl_type_hash_t *
nav2_msgs__srv__AddExclusionZone_Request__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x01, 0x07, 0x91, 0x81, 0xdb, 0xa1, 0xc7, 0xf0,
      0xdb, 0x22, 0x46, 0x90, 0xe0, 0xc2, 0xd5, 0xb8,
      0x27, 0x18, 0x0e, 0x27, 0x3f, 0x45, 0x63, 0x6e,
      0x23, 0x78, 0x48, 0x15, 0x17, 0x55, 0x44, 0x04,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_nav2_msgs
const rosidl_type_hash_t *
nav2_msgs__srv__AddExclusionZone_Response__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xa1, 0x9f, 0x5d, 0x48, 0xad, 0x7f, 0x65, 0x65,
      0x88, 0x6d, 0x0e, 0x09, 0x95, 0x0e, 0x22, 0x1d,
      0xc6, 0xe7, 0xab, 0xbb, 0xea, 0xba, 0xf0, 0x07,
      0x8b, 0x0a, 0xcf, 0xf9, 0x2b, 0x5b, 0x14, 0x79,
    }};
  return &hash;
}

ROSIDL_GENERATOR_C_PUBLIC_nav2_msgs
const rosidl_type_hash_t *
nav2_msgs__srv__AddExclusionZone_Event__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0xee, 0xc9, 0x45, 0x36, 0xa5, 0x7e, 0xf8, 0x09,
      0xe8, 0x67, 0x92, 0x73, 0x84, 0xe9, 0xa0, 0x0a,
      0xf7, 0xad, 0xea, 0x88, 0x8b, 0xc1, 0x61, 0xa6,
      0x96, 0xfc, 0x4b, 0x03, 0x3b, 0x2a, 0x80, 0xd6,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "builtin_interfaces/msg/detail/time__functions.h"
#include "geometry_msgs/msg/detail/point32__functions.h"
#include "nav2_msgs/msg/detail/exclusion_zone_description__functions.h"
#include "service_msgs/msg/detail/service_event_info__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t builtin_interfaces__msg__Time__EXPECTED_HASH = {1, {
    0xb1, 0x06, 0x23, 0x5e, 0x25, 0xa4, 0xc5, 0xed,
    0x35, 0x09, 0x8a, 0xa0, 0xa6, 0x1a, 0x3e, 0xe9,
    0xc9, 0xb1, 0x8d, 0x19, 0x7f, 0x39, 0x8b, 0x0e,
    0x42, 0x06, 0xce, 0xa9, 0xac, 0xf9, 0xc1, 0x97,
  }};
static const rosidl_type_hash_t geometry_msgs__msg__Point32__EXPECTED_HASH = {1, {
    0x2f, 0xc4, 0xdb, 0x7c, 0xae, 0x16, 0xa4, 0x58,
    0x2c, 0x79, 0xa5, 0x6b, 0x66, 0x17, 0x3a, 0x8d,
    0x48, 0xd5, 0x2c, 0x7d, 0xc5, 0x20, 0xdd, 0xc5,
    0x5a, 0x0d, 0x4b, 0xcf, 0x2a, 0x4b, 0xfd, 0xbc,
  }};
static const rosidl_type_hash_t nav2_msgs__msg__ExclusionZoneDescription__EXPECTED_HASH = {1, {
    0xf9, 0xad, 0xdb, 0xb3, 0xb5, 0xa2, 0x1a, 0x61,
    0x85, 0x6c, 0x99, 0x14, 0xd7, 0x45, 0xc8, 0xcd,
    0x6f, 0xdc, 0x98, 0x39, 0xf5, 0x8d, 0x8e, 0x91,
    0xe9, 0x28, 0xc3, 0x8e, 0xc9, 0xe1, 0xdb, 0x19,
  }};
static const rosidl_type_hash_t service_msgs__msg__ServiceEventInfo__EXPECTED_HASH = {1, {
    0x41, 0xbc, 0xbb, 0xe0, 0x7a, 0x75, 0xc9, 0xb5,
    0x2b, 0xc9, 0x6b, 0xfd, 0x5c, 0x24, 0xd7, 0xf0,
    0xfc, 0x0a, 0x08, 0xc0, 0xcb, 0x79, 0x21, 0xb3,
    0x37, 0x3c, 0x57, 0x32, 0x34, 0x5a, 0x6f, 0x45,
  }};
#endif

static char nav2_msgs__srv__AddExclusionZone__TYPE_NAME[] = "nav2_msgs/srv/AddExclusionZone";
static char builtin_interfaces__msg__Time__TYPE_NAME[] = "builtin_interfaces/msg/Time";
static char geometry_msgs__msg__Point32__TYPE_NAME[] = "geometry_msgs/msg/Point32";
static char nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME[] = "nav2_msgs/msg/ExclusionZoneDescription";
static char nav2_msgs__srv__AddExclusionZone_Event__TYPE_NAME[] = "nav2_msgs/srv/AddExclusionZone_Event";
static char nav2_msgs__srv__AddExclusionZone_Request__TYPE_NAME[] = "nav2_msgs/srv/AddExclusionZone_Request";
static char nav2_msgs__srv__AddExclusionZone_Response__TYPE_NAME[] = "nav2_msgs/srv/AddExclusionZone_Response";
static char service_msgs__msg__ServiceEventInfo__TYPE_NAME[] = "service_msgs/msg/ServiceEventInfo";

// Define type names, field names, and default values
static char nav2_msgs__srv__AddExclusionZone__FIELD_NAME__request_message[] = "request_message";
static char nav2_msgs__srv__AddExclusionZone__FIELD_NAME__response_message[] = "response_message";
static char nav2_msgs__srv__AddExclusionZone__FIELD_NAME__event_message[] = "event_message";

static rosidl_runtime_c__type_description__Field nav2_msgs__srv__AddExclusionZone__FIELDS[] = {
  {
    {nav2_msgs__srv__AddExclusionZone__FIELD_NAME__request_message, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {nav2_msgs__srv__AddExclusionZone_Request__TYPE_NAME, 38, 38},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone__FIELD_NAME__response_message, 16, 16},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {nav2_msgs__srv__AddExclusionZone_Response__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone__FIELD_NAME__event_message, 13, 13},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {nav2_msgs__srv__AddExclusionZone_Event__TYPE_NAME, 36, 36},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription nav2_msgs__srv__AddExclusionZone__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Point32__TYPE_NAME, 25, 25},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Event__TYPE_NAME, 36, 36},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Request__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Response__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
nav2_msgs__srv__AddExclusionZone__get_type_description(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {nav2_msgs__srv__AddExclusionZone__TYPE_NAME, 30, 30},
      {nav2_msgs__srv__AddExclusionZone__FIELDS, 3, 3},
    },
    {nav2_msgs__srv__AddExclusionZone__REFERENCED_TYPE_DESCRIPTIONS, 7, 7},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Point32__EXPECTED_HASH, geometry_msgs__msg__Point32__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = geometry_msgs__msg__Point32__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&nav2_msgs__msg__ExclusionZoneDescription__EXPECTED_HASH, nav2_msgs__msg__ExclusionZoneDescription__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = nav2_msgs__msg__ExclusionZoneDescription__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = nav2_msgs__srv__AddExclusionZone_Event__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[4].fields = nav2_msgs__srv__AddExclusionZone_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[5].fields = nav2_msgs__srv__AddExclusionZone_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[6].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char nav2_msgs__srv__AddExclusionZone_Request__FIELD_NAME__zone[] = "zone";

static rosidl_runtime_c__type_description__Field nav2_msgs__srv__AddExclusionZone_Request__FIELDS[] = {
  {
    {nav2_msgs__srv__AddExclusionZone_Request__FIELD_NAME__zone, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME, 38, 38},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription nav2_msgs__srv__AddExclusionZone_Request__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {geometry_msgs__msg__Point32__TYPE_NAME, 25, 25},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
nav2_msgs__srv__AddExclusionZone_Request__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {nav2_msgs__srv__AddExclusionZone_Request__TYPE_NAME, 38, 38},
      {nav2_msgs__srv__AddExclusionZone_Request__FIELDS, 1, 1},
    },
    {nav2_msgs__srv__AddExclusionZone_Request__REFERENCED_TYPE_DESCRIPTIONS, 2, 2},
  };
  if (!constructed) {
    assert(0 == memcmp(&geometry_msgs__msg__Point32__EXPECTED_HASH, geometry_msgs__msg__Point32__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = geometry_msgs__msg__Point32__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&nav2_msgs__msg__ExclusionZoneDescription__EXPECTED_HASH, nav2_msgs__msg__ExclusionZoneDescription__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = nav2_msgs__msg__ExclusionZoneDescription__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char nav2_msgs__srv__AddExclusionZone_Response__FIELD_NAME__success[] = "success";
static char nav2_msgs__srv__AddExclusionZone_Response__FIELD_NAME__message[] = "message";

static rosidl_runtime_c__type_description__Field nav2_msgs__srv__AddExclusionZone_Response__FIELDS[] = {
  {
    {nav2_msgs__srv__AddExclusionZone_Response__FIELD_NAME__success, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_BOOLEAN,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Response__FIELD_NAME__message, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
nav2_msgs__srv__AddExclusionZone_Response__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {nav2_msgs__srv__AddExclusionZone_Response__TYPE_NAME, 39, 39},
      {nav2_msgs__srv__AddExclusionZone_Response__FIELDS, 2, 2},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}
// Define type names, field names, and default values
static char nav2_msgs__srv__AddExclusionZone_Event__FIELD_NAME__info[] = "info";
static char nav2_msgs__srv__AddExclusionZone_Event__FIELD_NAME__request[] = "request";
static char nav2_msgs__srv__AddExclusionZone_Event__FIELD_NAME__response[] = "response";

static rosidl_runtime_c__type_description__Field nav2_msgs__srv__AddExclusionZone_Event__FIELDS[] = {
  {
    {nav2_msgs__srv__AddExclusionZone_Event__FIELD_NAME__info, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Event__FIELD_NAME__request, 7, 7},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {nav2_msgs__srv__AddExclusionZone_Request__TYPE_NAME, 38, 38},
    },
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Event__FIELD_NAME__response, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE_BOUNDED_SEQUENCE,
      1,
      0,
      {nav2_msgs__srv__AddExclusionZone_Response__TYPE_NAME, 39, 39},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription nav2_msgs__srv__AddExclusionZone_Event__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {builtin_interfaces__msg__Time__TYPE_NAME, 27, 27},
    {NULL, 0, 0},
  },
  {
    {geometry_msgs__msg__Point32__TYPE_NAME, 25, 25},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__msg__ExclusionZoneDescription__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Request__TYPE_NAME, 38, 38},
    {NULL, 0, 0},
  },
  {
    {nav2_msgs__srv__AddExclusionZone_Response__TYPE_NAME, 39, 39},
    {NULL, 0, 0},
  },
  {
    {service_msgs__msg__ServiceEventInfo__TYPE_NAME, 33, 33},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
nav2_msgs__srv__AddExclusionZone_Event__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {nav2_msgs__srv__AddExclusionZone_Event__TYPE_NAME, 36, 36},
      {nav2_msgs__srv__AddExclusionZone_Event__FIELDS, 3, 3},
    },
    {nav2_msgs__srv__AddExclusionZone_Event__REFERENCED_TYPE_DESCRIPTIONS, 6, 6},
  };
  if (!constructed) {
    assert(0 == memcmp(&builtin_interfaces__msg__Time__EXPECTED_HASH, builtin_interfaces__msg__Time__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = builtin_interfaces__msg__Time__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&geometry_msgs__msg__Point32__EXPECTED_HASH, geometry_msgs__msg__Point32__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[1].fields = geometry_msgs__msg__Point32__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&nav2_msgs__msg__ExclusionZoneDescription__EXPECTED_HASH, nav2_msgs__msg__ExclusionZoneDescription__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[2].fields = nav2_msgs__msg__ExclusionZoneDescription__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[3].fields = nav2_msgs__srv__AddExclusionZone_Request__get_type_description(NULL)->type_description.fields;
    description.referenced_type_descriptions.data[4].fields = nav2_msgs__srv__AddExclusionZone_Response__get_type_description(NULL)->type_description.fields;
    assert(0 == memcmp(&service_msgs__msg__ServiceEventInfo__EXPECTED_HASH, service_msgs__msg__ServiceEventInfo__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[5].fields = service_msgs__msg__ServiceEventInfo__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# Add an exclusion zone to a collision monitor / detector source at runtime.\n"
  "\n"
  "nav2_msgs/ExclusionZoneDescription zone\n"
  "---\n"
  "bool success\n"
  "string message";

static char srv_encoding[] = "srv";
static char implicit_encoding[] = "implicit";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
nav2_msgs__srv__AddExclusionZone__get_individual_type_description_source(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {nav2_msgs__srv__AddExclusionZone__TYPE_NAME, 30, 30},
    {srv_encoding, 3, 3},
    {toplevel_type_raw_source, 150, 150},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
nav2_msgs__srv__AddExclusionZone_Request__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {nav2_msgs__srv__AddExclusionZone_Request__TYPE_NAME, 38, 38},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
nav2_msgs__srv__AddExclusionZone_Response__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {nav2_msgs__srv__AddExclusionZone_Response__TYPE_NAME, 39, 39},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource *
nav2_msgs__srv__AddExclusionZone_Event__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {nav2_msgs__srv__AddExclusionZone_Event__TYPE_NAME, 36, 36},
    {implicit_encoding, 8, 8},
    {NULL, 0, 0},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
nav2_msgs__srv__AddExclusionZone__get_type_description_sources(
  const rosidl_service_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[8];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 8, 8};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *nav2_msgs__srv__AddExclusionZone__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *geometry_msgs__msg__Point32__get_individual_type_description_source(NULL);
    sources[3] = *nav2_msgs__msg__ExclusionZoneDescription__get_individual_type_description_source(NULL);
    sources[4] = *nav2_msgs__srv__AddExclusionZone_Event__get_individual_type_description_source(NULL);
    sources[5] = *nav2_msgs__srv__AddExclusionZone_Request__get_individual_type_description_source(NULL);
    sources[6] = *nav2_msgs__srv__AddExclusionZone_Response__get_individual_type_description_source(NULL);
    sources[7] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
nav2_msgs__srv__AddExclusionZone_Request__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[3];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 3, 3};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *nav2_msgs__srv__AddExclusionZone_Request__get_individual_type_description_source(NULL),
    sources[1] = *geometry_msgs__msg__Point32__get_individual_type_description_source(NULL);
    sources[2] = *nav2_msgs__msg__ExclusionZoneDescription__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
nav2_msgs__srv__AddExclusionZone_Response__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *nav2_msgs__srv__AddExclusionZone_Response__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
nav2_msgs__srv__AddExclusionZone_Event__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[7];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 7, 7};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *nav2_msgs__srv__AddExclusionZone_Event__get_individual_type_description_source(NULL),
    sources[1] = *builtin_interfaces__msg__Time__get_individual_type_description_source(NULL);
    sources[2] = *geometry_msgs__msg__Point32__get_individual_type_description_source(NULL);
    sources[3] = *nav2_msgs__msg__ExclusionZoneDescription__get_individual_type_description_source(NULL);
    sources[4] = *nav2_msgs__srv__AddExclusionZone_Request__get_individual_type_description_source(NULL);
    sources[5] = *nav2_msgs__srv__AddExclusionZone_Response__get_individual_type_description_source(NULL);
    sources[6] = *service_msgs__msg__ServiceEventInfo__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
