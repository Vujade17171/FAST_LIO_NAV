# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/RouteEdge.idl
# generated code does not contain a copyright notice

from __future__ import annotations

import collections.abc
import os
import typing

import rosidl_pycommon.interface_base_classes

if typing.TYPE_CHECKING:
    from ctypes import Structure

    class PyCapsule(Structure):
        pass  # don't need to define the full structure


# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
ros_python_check_fields = os.getenv('ROS_PYTHON_CHECK_FIELDS', default='')


if typing.TYPE_CHECKING:
    import geometry_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_RouteEdge(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'RouteEdge'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RouteEdgeConstants(typing.TypedDict):
        pass

    __constants: RouteEdgeConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('nav2_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'nav2_msgs.msg.RouteEdge')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__route_edge
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__route_edge
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__route_edge
            cls._TYPE_SUPPORT = module.type_support_msg__msg__route_edge
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__route_edge

            from geometry_msgs.msg import Point
            if Point._TYPE_SUPPORT is None:
                Point.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class RouteEdge(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_RouteEdge):
    """Message class 'RouteEdge'."""

    __slots__ = [
        '_edgeid',
        '_start',
        '_end',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'edgeid': 'uint16',
        'start': 'geometry_msgs/Point',
        'end': 'geometry_msgs/Point',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point'),  # noqa: E501
    )

    def __init__(self, *,
                 edgeid: typing.Optional[int] = None,  # noqa: E501
                 start: typing.Optional[geometry_msgs.msg.Point] = None,  # noqa: E501
                 end: typing.Optional[geometry_msgs.msg.Point] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.edgeid = edgeid if edgeid is not None else int()
        from geometry_msgs.msg import Point
        self.start = start if start is not None else Point()
        from geometry_msgs.msg import Point
        self.end = end if end is not None else Point()

    def __repr__(self) -> str:
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args: list[str] = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    from rosidl_buffer import Buffer as _RosidlBuffer
                    if not isinstance(field, _RosidlBuffer):
                        if self._check_fields:
                            assert fieldstr.startswith('array(')
                        prefix = "array('X', "
                        suffix = ')'
                        fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, RouteEdge):
            return False
        if self.edgeid != other.edgeid:
            return False
        if self.start != other.start:
            return False
        if self.end != other.end:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def edgeid(self) -> int:
        """Message field 'edgeid'."""
        return self._edgeid

    @edgeid.setter
    def edgeid(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'edgeid' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'edgeid' field must be an unsigned integer in [0, 65535]"

        self._edgeid = value

    @builtins.property
    def start(self) -> geometry_msgs.msg.Point:
        """Message field 'start'."""
        return self._start

    @start.setter
    def start(self, value: geometry_msgs.msg.Point) -> None:
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Point), \
                    "The 'start' field must be a sub message of type 'Point'"

        self._start = value

    @builtins.property
    def end(self) -> geometry_msgs.msg.Point:
        """Message field 'end'."""
        return self._end

    @end.setter
    def end(self, value: geometry_msgs.msg.Point) -> None:
        from geometry_msgs.msg import Point

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Point), \
                    "The 'end' field must be a sub message of type 'Point'"

        self._end = value
