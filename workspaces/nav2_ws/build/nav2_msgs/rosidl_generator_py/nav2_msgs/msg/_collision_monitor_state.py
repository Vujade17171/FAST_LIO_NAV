# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/CollisionMonitorState.idl
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

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CollisionMonitorState(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'CollisionMonitorState'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CollisionMonitorStateConstants(typing.TypedDict):
        DO_NOTHING: typing.Literal[0]
        STOP: typing.Literal[1]
        SLOWDOWN: typing.Literal[2]
        APPROACH: typing.Literal[3]
        LIMIT: typing.Literal[4]

    __constants: CollisionMonitorStateConstants = {
        'DO_NOTHING': 0,
        'STOP': 1,
        'SLOWDOWN': 2,
        'APPROACH': 3,
        'LIMIT': 4,
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
                'nav2_msgs.msg.CollisionMonitorState')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__collision_monitor_state
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__collision_monitor_state
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__collision_monitor_state
            cls._TYPE_SUPPORT = module.type_support_msg__msg__collision_monitor_state
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__collision_monitor_state

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'DO_NOTHING': metacls.__constants['DO_NOTHING'],
            'STOP': metacls.__constants['STOP'],
            'SLOWDOWN': metacls.__constants['SLOWDOWN'],
            'APPROACH': metacls.__constants['APPROACH'],
            'LIMIT': metacls.__constants['LIMIT'],
        }

    @property
    def DO_NOTHING(self) -> typing.Literal[0]:
        """Message constant 'DO_NOTHING'."""
        return Metaclass_CollisionMonitorState.__constants['DO_NOTHING']

    @property
    def STOP(self) -> typing.Literal[1]:
        """Message constant 'STOP'."""
        return Metaclass_CollisionMonitorState.__constants['STOP']

    @property
    def SLOWDOWN(self) -> typing.Literal[2]:
        """Message constant 'SLOWDOWN'."""
        return Metaclass_CollisionMonitorState.__constants['SLOWDOWN']

    @property
    def APPROACH(self) -> typing.Literal[3]:
        """Message constant 'APPROACH'."""
        return Metaclass_CollisionMonitorState.__constants['APPROACH']

    @property
    def LIMIT(self) -> typing.Literal[4]:
        """Message constant 'LIMIT'."""
        return Metaclass_CollisionMonitorState.__constants['LIMIT']


class CollisionMonitorState(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_CollisionMonitorState):
    """
    Message class 'CollisionMonitorState'.

    Constants:
      DO_NOTHING
      STOP
      SLOWDOWN
      APPROACH
      LIMIT
    """

    __slots__ = [
        '_action_type',
        '_polygon_name',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'action_type': 'uint8',
        'polygon_name': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 action_type: typing.Optional[int] = None,  # noqa: E501
                 polygon_name: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.action_type = action_type if action_type is not None else int()
        self.polygon_name = polygon_name if polygon_name is not None else str()

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
        if not isinstance(other, CollisionMonitorState):
            return False
        if self.action_type != other.action_type:
            return False
        if self.polygon_name != other.polygon_name:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def action_type(self) -> int:
        """Message field 'action_type'."""
        return self._action_type

    @action_type.setter
    def action_type(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'action_type' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'action_type' field must be an unsigned integer in [0, 255]"

        self._action_type = value

    @builtins.property
    def polygon_name(self) -> str:
        """Message field 'polygon_name'."""
        return self._polygon_name

    @polygon_name.setter
    def polygon_name(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'polygon_name' field must be of type 'str'"

        self._polygon_name = value
