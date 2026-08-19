# generated from rosidl_generator_py/resource/_idl.py.em
# with input from livox_ros_driver2:msg/CustomPoint.idl
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


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CustomPoint(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'CustomPoint'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CustomPointConstants(typing.TypedDict):
        pass

    __constants: CustomPointConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('livox_ros_driver2')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'livox_ros_driver2.msg.CustomPoint')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__custom_point
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__custom_point
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__custom_point
            cls._TYPE_SUPPORT = module.type_support_msg__msg__custom_point
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__custom_point

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CustomPoint(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_CustomPoint):
    """Message class 'CustomPoint'."""

    __slots__ = [
        '_offset_time',
        '_x',
        '_y',
        '_z',
        '_reflectivity',
        '_tag',
        '_line',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'offset_time': 'uint32',
        'x': 'float',
        'y': 'float',
        'z': 'float',
        'reflectivity': 'uint8',
        'tag': 'uint8',
        'line': 'uint8',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
    )

    def __init__(self, *,
                 offset_time: typing.Optional[int] = None,  # noqa: E501
                 x: typing.Optional[float] = None,  # noqa: E501
                 y: typing.Optional[float] = None,  # noqa: E501
                 z: typing.Optional[float] = None,  # noqa: E501
                 reflectivity: typing.Optional[int] = None,  # noqa: E501
                 tag: typing.Optional[int] = None,  # noqa: E501
                 line: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.offset_time = offset_time if offset_time is not None else int()
        self.x = x if x is not None else float()
        self.y = y if y is not None else float()
        self.z = z if z is not None else float()
        self.reflectivity = reflectivity if reflectivity is not None else int()
        self.tag = tag if tag is not None else int()
        self.line = line if line is not None else int()

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
        if not isinstance(other, CustomPoint):
            return False
        if self.offset_time != other.offset_time:
            return False
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        if self.z != other.z:
            return False
        if self.reflectivity != other.reflectivity:
            return False
        if self.tag != other.tag:
            return False
        if self.line != other.line:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def offset_time(self) -> int:
        """Message field 'offset_time'."""
        return self._offset_time

    @offset_time.setter
    def offset_time(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'offset_time' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'offset_time' field must be an unsigned integer in [0, 4294967295]"

        self._offset_time = value

    @builtins.property
    def x(self) -> float:
        """Message field 'x'."""
        return self._x

    @x.setter
    def x(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'x' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'x' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._x = value

    @builtins.property
    def y(self) -> float:
        """Message field 'y'."""
        return self._y

    @y.setter
    def y(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'y' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'y' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._y = value

    @builtins.property
    def z(self) -> float:
        """Message field 'z'."""
        return self._z

    @z.setter
    def z(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'z' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'z' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._z = value

    @builtins.property
    def reflectivity(self) -> int:
        """Message field 'reflectivity'."""
        return self._reflectivity

    @reflectivity.setter
    def reflectivity(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'reflectivity' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'reflectivity' field must be an unsigned integer in [0, 255]"

        self._reflectivity = value

    @builtins.property
    def tag(self) -> int:
        """Message field 'tag'."""
        return self._tag

    @tag.setter
    def tag(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'tag' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'tag' field must be an unsigned integer in [0, 255]"

        self._tag = value

    @builtins.property
    def line(self) -> int:
        """Message field 'line'."""
        return self._line

    @line.setter
    def line(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'line' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'line' field must be an unsigned integer in [0, 255]"

        self._line = value
