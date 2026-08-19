# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/CircleObject.idl
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
    import std_msgs.msg  # noqa: E402, I100, I201, I300
    import unique_identifier_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CircleObject(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'CircleObject'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CircleObjectConstants(typing.TypedDict):
        pass

    __constants: CircleObjectConstants = {
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
                'nav2_msgs.msg.CircleObject')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__circle_object
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__circle_object
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__circle_object
            cls._TYPE_SUPPORT = module.type_support_msg__msg__circle_object
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__circle_object

            from geometry_msgs.msg import Point32
            if Point32._TYPE_SUPPORT is None:
                Point32.__import_type_support__()

            from std_msgs.msg import Header
            if Header._TYPE_SUPPORT is None:
                Header.__import_type_support__()

            from unique_identifier_msgs.msg import UUID
            if UUID._TYPE_SUPPORT is None:
                UUID.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CircleObject(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_CircleObject):
    """Message class 'CircleObject'."""

    __slots__ = [
        '_header',
        '_uuid',
        '_center',
        '_radius',
        '_fill',
        '_value',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'uuid': 'unique_identifier_msgs/UUID',
        'center': 'geometry_msgs/Point32',
        'radius': 'float',
        'fill': 'boolean',
        'value': 'int8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 uuid: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 center: typing.Optional[geometry_msgs.msg.Point32] = None,  # noqa: E501
                 radius: typing.Optional[float] = None,  # noqa: E501
                 fill: typing.Optional[bool] = None,  # noqa: E501
                 value: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        from unique_identifier_msgs.msg import UUID
        self.uuid = uuid if uuid is not None else UUID()
        from geometry_msgs.msg import Point32
        self.center = center if center is not None else Point32()
        self.radius = radius if radius is not None else float()
        self.fill = fill if fill is not None else bool()
        self.value = value if value is not None else int()

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
        if not isinstance(other, CircleObject):
            return False
        if self.header != other.header:
            return False
        if self.uuid != other.uuid:
            return False
        if self.center != other.center:
            return False
        if self.radius != other.radius:
            return False
        if self.fill != other.fill:
            return False
        if self.value != other.value:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def header(self) -> std_msgs.msg.Header:
        """Message field 'header'."""
        return self._header

    @header.setter
    def header(self, value: std_msgs.msg.Header) -> None:
        from std_msgs.msg import Header

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Header), \
                    "The 'header' field must be a sub message of type 'Header'"

        self._header = value

    @builtins.property
    def uuid(self) -> unique_identifier_msgs.msg.UUID:
        """Message field 'uuid'."""
        return self._uuid

    @uuid.setter
    def uuid(self, value: unique_identifier_msgs.msg.UUID) -> None:
        from unique_identifier_msgs.msg import UUID

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, UUID), \
                    "The 'uuid' field must be a sub message of type 'UUID'"

        self._uuid = value

    @builtins.property
    def center(self) -> geometry_msgs.msg.Point32:
        """Message field 'center'."""
        return self._center

    @center.setter
    def center(self, value: geometry_msgs.msg.Point32) -> None:
        from geometry_msgs.msg import Point32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Point32), \
                    "The 'center' field must be a sub message of type 'Point32'"

        self._center = value

    @builtins.property
    def radius(self) -> float:
        """Message field 'radius'."""
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'radius' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'radius' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._radius = value

    @builtins.property
    def fill(self) -> bool:
        """Message field 'fill'."""
        return self._fill

    @fill.setter
    def fill(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'fill' field must be of type 'bool'"

        self._fill = value

    @builtins.property
    def value(self) -> int:
        """Message field 'value'."""
        return self._value

    @value.setter
    def value(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'value' field must be of type 'int'"
                assert value >= -128 and value < 128, \
                    "The 'value' field must be an integer in [-128, 127]"

        self._value = value
