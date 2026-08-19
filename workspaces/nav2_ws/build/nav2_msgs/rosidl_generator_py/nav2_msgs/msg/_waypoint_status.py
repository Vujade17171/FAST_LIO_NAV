# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/WaypointStatus.idl
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


class Metaclass_WaypointStatus(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'WaypointStatus'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class WaypointStatusConstants(typing.TypedDict):
        PENDING: typing.Literal[0]
        COMPLETED: typing.Literal[1]
        SKIPPED: typing.Literal[2]
        FAILED: typing.Literal[3]

    __constants: WaypointStatusConstants = {
        'PENDING': 0,
        'COMPLETED': 1,
        'SKIPPED': 2,
        'FAILED': 3,
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
                'nav2_msgs.msg.WaypointStatus')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__waypoint_status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__waypoint_status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__waypoint_status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__waypoint_status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__waypoint_status

            from geometry_msgs.msg import PoseStamped
            if PoseStamped._TYPE_SUPPORT is None:
                PoseStamped.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'PENDING': metacls.__constants['PENDING'],
            'COMPLETED': metacls.__constants['COMPLETED'],
            'SKIPPED': metacls.__constants['SKIPPED'],
            'FAILED': metacls.__constants['FAILED'],
        }

    @property
    def PENDING(self) -> typing.Literal[0]:
        """Message constant 'PENDING'."""
        return Metaclass_WaypointStatus.__constants['PENDING']

    @property
    def COMPLETED(self) -> typing.Literal[1]:
        """Message constant 'COMPLETED'."""
        return Metaclass_WaypointStatus.__constants['COMPLETED']

    @property
    def SKIPPED(self) -> typing.Literal[2]:
        """Message constant 'SKIPPED'."""
        return Metaclass_WaypointStatus.__constants['SKIPPED']

    @property
    def FAILED(self) -> typing.Literal[3]:
        """Message constant 'FAILED'."""
        return Metaclass_WaypointStatus.__constants['FAILED']


class WaypointStatus(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_WaypointStatus):
    """
    Message class 'WaypointStatus'.

    Constants:
      PENDING
      COMPLETED
      SKIPPED
      FAILED
    """

    __slots__ = [
        '_waypoint_status',
        '_waypoint_index',
        '_waypoint_pose',
        '_error_code',
        '_error_msg',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'waypoint_status': 'uint8',
        'waypoint_index': 'uint32',
        'waypoint_pose': 'geometry_msgs/PoseStamped',
        'error_code': 'uint16',
        'error_msg': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 waypoint_status: typing.Optional[int] = None,  # noqa: E501
                 waypoint_index: typing.Optional[int] = None,  # noqa: E501
                 waypoint_pose: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 error_code: typing.Optional[int] = None,  # noqa: E501
                 error_msg: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.waypoint_status = waypoint_status if waypoint_status is not None else int()
        self.waypoint_index = waypoint_index if waypoint_index is not None else int()
        from geometry_msgs.msg import PoseStamped
        self.waypoint_pose = waypoint_pose if waypoint_pose is not None else PoseStamped()
        self.error_code = error_code if error_code is not None else int()
        self.error_msg = error_msg if error_msg is not None else str()

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
        if not isinstance(other, WaypointStatus):
            return False
        if self.waypoint_status != other.waypoint_status:
            return False
        if self.waypoint_index != other.waypoint_index:
            return False
        if self.waypoint_pose != other.waypoint_pose:
            return False
        if self.error_code != other.error_code:
            return False
        if self.error_msg != other.error_msg:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def waypoint_status(self) -> int:
        """Message field 'waypoint_status'."""
        return self._waypoint_status

    @waypoint_status.setter
    def waypoint_status(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'waypoint_status' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'waypoint_status' field must be an unsigned integer in [0, 255]"

        self._waypoint_status = value

    @builtins.property
    def waypoint_index(self) -> int:
        """Message field 'waypoint_index'."""
        return self._waypoint_index

    @waypoint_index.setter
    def waypoint_index(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'waypoint_index' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'waypoint_index' field must be an unsigned integer in [0, 4294967295]"

        self._waypoint_index = value

    @builtins.property
    def waypoint_pose(self) -> geometry_msgs.msg.PoseStamped:
        """Message field 'waypoint_pose'."""
        return self._waypoint_pose

    @waypoint_pose.setter
    def waypoint_pose(self, value: geometry_msgs.msg.PoseStamped) -> None:
        from geometry_msgs.msg import PoseStamped

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, PoseStamped), \
                    "The 'waypoint_pose' field must be a sub message of type 'PoseStamped'"

        self._waypoint_pose = value

    @builtins.property
    def error_code(self) -> int:
        """Message field 'error_code'."""
        return self._error_code

    @error_code.setter
    def error_code(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'error_code' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'error_code' field must be an unsigned integer in [0, 65535]"

        self._error_code = value

    @builtins.property
    def error_msg(self) -> str:
        """Message field 'error_msg'."""
        return self._error_msg

    @error_msg.setter
    def error_msg(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'error_msg' field must be of type 'str'"

        self._error_msg = value
