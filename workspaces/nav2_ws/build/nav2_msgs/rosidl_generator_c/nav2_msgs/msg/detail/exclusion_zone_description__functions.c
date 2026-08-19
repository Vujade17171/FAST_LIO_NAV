// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from nav2_msgs:msg/ExclusionZoneDescription.idl
// generated code does not contain a copyright notice
#include "nav2_msgs/msg/detail/exclusion_zone_description__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `zone_name`
// Member `type`
// Member `frame_id`
#include "rosidl_runtime_c/string_functions.h"
// Member `points`
#include "geometry_msgs/msg/detail/point32__functions.h"

bool
nav2_msgs__msg__ExclusionZoneDescription__init(nav2_msgs__msg__ExclusionZoneDescription * msg)
{
  if (!msg) {
    return false;
  }
  // zone_name
  if (!rosidl_runtime_c__String__init(&msg->zone_name)) {
    nav2_msgs__msg__ExclusionZoneDescription__fini(msg);
    return false;
  }
  // type
  if (!rosidl_runtime_c__String__init(&msg->type)) {
    nav2_msgs__msg__ExclusionZoneDescription__fini(msg);
    return false;
  }
  // frame_id
  if (!rosidl_runtime_c__String__init(&msg->frame_id)) {
    nav2_msgs__msg__ExclusionZoneDescription__fini(msg);
    return false;
  }
  // points
  if (!geometry_msgs__msg__Point32__Sequence__init(&msg->points, 0)) {
    nav2_msgs__msg__ExclusionZoneDescription__fini(msg);
    return false;
  }
  // radius
  msg->radius = 0.0l;
  // min_height
  msg->min_height = -1.7976931348623157e+308l;
  // max_height
  msg->max_height = 1.7976931348623157e+308l;
  // enabled
  msg->enabled = true;
  // visualize
  msg->visualize = false;
  // frame_hold_timeout
  msg->frame_hold_timeout = 0.0l;
  return true;
}

void
nav2_msgs__msg__ExclusionZoneDescription__fini(nav2_msgs__msg__ExclusionZoneDescription * msg)
{
  if (!msg) {
    return;
  }
  // zone_name
  rosidl_runtime_c__String__fini(&msg->zone_name);
  // type
  rosidl_runtime_c__String__fini(&msg->type);
  // frame_id
  rosidl_runtime_c__String__fini(&msg->frame_id);
  // points
  geometry_msgs__msg__Point32__Sequence__fini(&msg->points);
  // radius
  // min_height
  // max_height
  // enabled
  // visualize
  // frame_hold_timeout
}

bool
nav2_msgs__msg__ExclusionZoneDescription__are_equal(const nav2_msgs__msg__ExclusionZoneDescription * lhs, const nav2_msgs__msg__ExclusionZoneDescription * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // zone_name
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->zone_name), &(rhs->zone_name)))
  {
    return false;
  }
  // type
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->type), &(rhs->type)))
  {
    return false;
  }
  // frame_id
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->frame_id), &(rhs->frame_id)))
  {
    return false;
  }
  // points
  if (!geometry_msgs__msg__Point32__Sequence__are_equal(
      &(lhs->points), &(rhs->points)))
  {
    return false;
  }
  // radius
  if (lhs->radius != rhs->radius) {
    return false;
  }
  // min_height
  if (lhs->min_height != rhs->min_height) {
    return false;
  }
  // max_height
  if (lhs->max_height != rhs->max_height) {
    return false;
  }
  // enabled
  if (lhs->enabled != rhs->enabled) {
    return false;
  }
  // visualize
  if (lhs->visualize != rhs->visualize) {
    return false;
  }
  // frame_hold_timeout
  if (lhs->frame_hold_timeout != rhs->frame_hold_timeout) {
    return false;
  }
  return true;
}

bool
nav2_msgs__msg__ExclusionZoneDescription__copy(
  const nav2_msgs__msg__ExclusionZoneDescription * input,
  nav2_msgs__msg__ExclusionZoneDescription * output)
{
  if (!input || !output) {
    return false;
  }
  // zone_name
  if (!rosidl_runtime_c__String__copy(
      &(input->zone_name), &(output->zone_name)))
  {
    return false;
  }
  // type
  if (!rosidl_runtime_c__String__copy(
      &(input->type), &(output->type)))
  {
    return false;
  }
  // frame_id
  if (!rosidl_runtime_c__String__copy(
      &(input->frame_id), &(output->frame_id)))
  {
    return false;
  }
  // points
  if (!geometry_msgs__msg__Point32__Sequence__copy(
      &(input->points), &(output->points)))
  {
    return false;
  }
  // radius
  output->radius = input->radius;
  // min_height
  output->min_height = input->min_height;
  // max_height
  output->max_height = input->max_height;
  // enabled
  output->enabled = input->enabled;
  // visualize
  output->visualize = input->visualize;
  // frame_hold_timeout
  output->frame_hold_timeout = input->frame_hold_timeout;
  return true;
}

nav2_msgs__msg__ExclusionZoneDescription *
nav2_msgs__msg__ExclusionZoneDescription__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  nav2_msgs__msg__ExclusionZoneDescription * msg = (nav2_msgs__msg__ExclusionZoneDescription *)allocator.allocate(sizeof(nav2_msgs__msg__ExclusionZoneDescription), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(nav2_msgs__msg__ExclusionZoneDescription));
  bool success = nav2_msgs__msg__ExclusionZoneDescription__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
nav2_msgs__msg__ExclusionZoneDescription__destroy(nav2_msgs__msg__ExclusionZoneDescription * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    nav2_msgs__msg__ExclusionZoneDescription__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
nav2_msgs__msg__ExclusionZoneDescription__Sequence__init(nav2_msgs__msg__ExclusionZoneDescription__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  nav2_msgs__msg__ExclusionZoneDescription * data = NULL;

  if (size) {
    if (size > SIZE_MAX / sizeof(nav2_msgs__msg__ExclusionZoneDescription)) {
      return false;
    }
    data = (nav2_msgs__msg__ExclusionZoneDescription *)allocator.zero_allocate(size, sizeof(nav2_msgs__msg__ExclusionZoneDescription), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = nav2_msgs__msg__ExclusionZoneDescription__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        nav2_msgs__msg__ExclusionZoneDescription__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
nav2_msgs__msg__ExclusionZoneDescription__Sequence__fini(nav2_msgs__msg__ExclusionZoneDescription__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      nav2_msgs__msg__ExclusionZoneDescription__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

nav2_msgs__msg__ExclusionZoneDescription__Sequence *
nav2_msgs__msg__ExclusionZoneDescription__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  nav2_msgs__msg__ExclusionZoneDescription__Sequence * array = (nav2_msgs__msg__ExclusionZoneDescription__Sequence *)allocator.allocate(sizeof(nav2_msgs__msg__ExclusionZoneDescription__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = nav2_msgs__msg__ExclusionZoneDescription__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
nav2_msgs__msg__ExclusionZoneDescription__Sequence__destroy(nav2_msgs__msg__ExclusionZoneDescription__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    nav2_msgs__msg__ExclusionZoneDescription__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
nav2_msgs__msg__ExclusionZoneDescription__Sequence__are_equal(const nav2_msgs__msg__ExclusionZoneDescription__Sequence * lhs, const nav2_msgs__msg__ExclusionZoneDescription__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!nav2_msgs__msg__ExclusionZoneDescription__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
nav2_msgs__msg__ExclusionZoneDescription__Sequence__copy(
  const nav2_msgs__msg__ExclusionZoneDescription__Sequence * input,
  nav2_msgs__msg__ExclusionZoneDescription__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    if (input->size > SIZE_MAX / sizeof(nav2_msgs__msg__ExclusionZoneDescription)) {
      return false;
    }
    const size_t allocation_size =
      input->size * sizeof(nav2_msgs__msg__ExclusionZoneDescription);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    nav2_msgs__msg__ExclusionZoneDescription * data =
      (nav2_msgs__msg__ExclusionZoneDescription *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!nav2_msgs__msg__ExclusionZoneDescription__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          nav2_msgs__msg__ExclusionZoneDescription__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!nav2_msgs__msg__ExclusionZoneDescription__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
