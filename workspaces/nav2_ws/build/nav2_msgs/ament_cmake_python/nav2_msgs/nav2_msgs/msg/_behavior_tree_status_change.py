# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/BehaviorTreeStatusChange.idl
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
    import builtin_interfaces.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BehaviorTreeStatusChange(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'BehaviorTreeStatusChange'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class BehaviorTreeStatusChangeConstants(typing.TypedDict):
        pass

    __constants: BehaviorTreeStatusChangeConstants = {
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
                'nav2_msgs.msg.BehaviorTreeStatusChange')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__behavior_tree_status_change
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__behavior_tree_status_change
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__behavior_tree_status_change
            cls._TYPE_SUPPORT = module.type_support_msg__msg__behavior_tree_status_change
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__behavior_tree_status_change

            from builtin_interfaces.msg import Time
            if Time._TYPE_SUPPORT is None:
                Time.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BehaviorTreeStatusChange(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_BehaviorTreeStatusChange):
    """Message class 'BehaviorTreeStatusChange'."""

    __slots__ = [
        '_timestamp',
        '_node_name',
        '_uid',
        '_previous_status',
        '_current_status',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'timestamp': 'builtin_interfaces/Time',
        'node_name': 'string',
        'uid': 'uint16',
        'previous_status': 'string',
        'current_status': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 timestamp: typing.Optional[builtin_interfaces.msg.Time] = None,  # noqa: E501
                 node_name: typing.Optional[str] = None,  # noqa: E501
                 uid: typing.Optional[int] = None,  # noqa: E501
                 previous_status: typing.Optional[str] = None,  # noqa: E501
                 current_status: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from builtin_interfaces.msg import Time
        self.timestamp = timestamp if timestamp is not None else Time()
        self.node_name = node_name if node_name is not None else str()
        self.uid = uid if uid is not None else int()
        self.previous_status = previous_status if previous_status is not None else str()
        self.current_status = current_status if current_status is not None else str()

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
        if not isinstance(other, BehaviorTreeStatusChange):
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.node_name != other.node_name:
            return False
        if self.uid != other.uid:
            return False
        if self.previous_status != other.previous_status:
            return False
        if self.current_status != other.current_status:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def timestamp(self) -> builtin_interfaces.msg.Time:
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value: builtin_interfaces.msg.Time) -> None:
        from builtin_interfaces.msg import Time

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Time), \
                    "The 'timestamp' field must be a sub message of type 'Time'"

        self._timestamp = value

    @builtins.property
    def node_name(self) -> str:
        """Message field 'node_name'."""
        return self._node_name

    @node_name.setter
    def node_name(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'node_name' field must be of type 'str'"

        self._node_name = value

    @builtins.property
    def uid(self) -> int:
        """Message field 'uid'."""
        return self._uid

    @uid.setter
    def uid(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'uid' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'uid' field must be an unsigned integer in [0, 65535]"

        self._uid = value

    @builtins.property
    def previous_status(self) -> str:
        """Message field 'previous_status'."""
        return self._previous_status

    @previous_status.setter
    def previous_status(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'previous_status' field must be of type 'str'"

        self._previous_status = value

    @builtins.property
    def current_status(self) -> str:
        """Message field 'current_status'."""
        return self._current_status

    @current_status.setter
    def current_status(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'current_status' field must be of type 'str'"

        self._current_status = value
