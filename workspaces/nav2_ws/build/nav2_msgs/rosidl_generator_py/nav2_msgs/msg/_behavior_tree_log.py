# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/BehaviorTreeLog.idl
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
    import nav2_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_BehaviorTreeLog(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'BehaviorTreeLog'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class BehaviorTreeLogConstants(typing.TypedDict):
        pass

    __constants: BehaviorTreeLogConstants = {
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
                'nav2_msgs.msg.BehaviorTreeLog')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__behavior_tree_log
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__behavior_tree_log
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__behavior_tree_log
            cls._TYPE_SUPPORT = module.type_support_msg__msg__behavior_tree_log
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__behavior_tree_log

            from builtin_interfaces.msg import Time
            if Time._TYPE_SUPPORT is None:
                Time.__import_type_support__()

            from nav2_msgs.msg import BehaviorTreeStatusChange
            if BehaviorTreeStatusChange._TYPE_SUPPORT is None:
                BehaviorTreeStatusChange.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class BehaviorTreeLog(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_BehaviorTreeLog):
    """Message class 'BehaviorTreeLog'."""

    __slots__ = [
        '_timestamp',
        '_event_log',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'timestamp': 'builtin_interfaces/Time',
        'event_log': 'sequence<nav2_msgs/BehaviorTreeStatusChange>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'msg'], 'BehaviorTreeStatusChange')),  # noqa: E501
    )

    def __init__(self, *,
                 timestamp: typing.Optional[builtin_interfaces.msg.Time] = None,  # noqa: E501
                 event_log: typing.Optional[collections.abc.Sequence[nav2_msgs.msg.BehaviorTreeStatusChange]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from builtin_interfaces.msg import Time
        self.timestamp = timestamp if timestamp is not None else Time()
        self.event_log = event_log if event_log is not None else []

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
        if not isinstance(other, BehaviorTreeLog):
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.event_log != other.event_log:
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
    def event_log(self) -> typing.Annotated[typing.Any, list[nav2_msgs.msg.BehaviorTreeStatusChange]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'event_log'."""
        return self._event_log

    @event_log.setter
    def event_log(self, value: collections.abc.Sequence[nav2_msgs.msg.BehaviorTreeStatusChange]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.msg import BehaviorTreeStatusChange

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, BehaviorTreeStatusChange) for v in value) and
                     True), \
                    "The 'event_log' field must be sequence and each value of type 'BehaviorTreeStatusChange'"

        if isinstance(value, list):
            self._event_log = value
            return
        self._event_log = list(value)
