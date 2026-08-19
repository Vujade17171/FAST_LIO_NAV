# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/TrackingFeedback.idl
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


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TrackingFeedback(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'TrackingFeedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class TrackingFeedbackConstants(typing.TypedDict):
        pass

    __constants: TrackingFeedbackConstants = {
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
                'nav2_msgs.msg.TrackingFeedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__tracking_feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__tracking_feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__tracking_feedback
            cls._TYPE_SUPPORT = module.type_support_msg__msg__tracking_feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__tracking_feedback

            from geometry_msgs.msg import PoseStamped
            if PoseStamped._TYPE_SUPPORT is None:
                PoseStamped.__import_type_support__()

            from std_msgs.msg import Header
            if Header._TYPE_SUPPORT is None:
                Header.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TrackingFeedback(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_TrackingFeedback):
    """Message class 'TrackingFeedback'."""

    __slots__ = [
        '_header',
        '_position_tracking_error',
        '_heading_tracking_error',
        '_current_path_index',
        '_robot_pose',
        '_distance_to_goal',
        '_speed',
        '_remaining_path_length',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'position_tracking_error': 'float',
        'heading_tracking_error': 'float',
        'current_path_index': 'uint32',
        'robot_pose': 'geometry_msgs/PoseStamped',
        'distance_to_goal': 'float',
        'speed': 'float',
        'remaining_path_length': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 position_tracking_error: typing.Optional[float] = None,  # noqa: E501
                 heading_tracking_error: typing.Optional[float] = None,  # noqa: E501
                 current_path_index: typing.Optional[int] = None,  # noqa: E501
                 robot_pose: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 distance_to_goal: typing.Optional[float] = None,  # noqa: E501
                 speed: typing.Optional[float] = None,  # noqa: E501
                 remaining_path_length: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.position_tracking_error = position_tracking_error if position_tracking_error is not None else float()
        self.heading_tracking_error = heading_tracking_error if heading_tracking_error is not None else float()
        self.current_path_index = current_path_index if current_path_index is not None else int()
        from geometry_msgs.msg import PoseStamped
        self.robot_pose = robot_pose if robot_pose is not None else PoseStamped()
        self.distance_to_goal = distance_to_goal if distance_to_goal is not None else float()
        self.speed = speed if speed is not None else float()
        self.remaining_path_length = remaining_path_length if remaining_path_length is not None else float()

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
        if not isinstance(other, TrackingFeedback):
            return False
        if self.header != other.header:
            return False
        if self.position_tracking_error != other.position_tracking_error:
            return False
        if self.heading_tracking_error != other.heading_tracking_error:
            return False
        if self.current_path_index != other.current_path_index:
            return False
        if self.robot_pose != other.robot_pose:
            return False
        if self.distance_to_goal != other.distance_to_goal:
            return False
        if self.speed != other.speed:
            return False
        if self.remaining_path_length != other.remaining_path_length:
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
    def position_tracking_error(self) -> float:
        """Message field 'position_tracking_error'."""
        return self._position_tracking_error

    @position_tracking_error.setter
    def position_tracking_error(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'position_tracking_error' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'position_tracking_error' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._position_tracking_error = value

    @builtins.property
    def heading_tracking_error(self) -> float:
        """Message field 'heading_tracking_error'."""
        return self._heading_tracking_error

    @heading_tracking_error.setter
    def heading_tracking_error(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'heading_tracking_error' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'heading_tracking_error' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._heading_tracking_error = value

    @builtins.property
    def current_path_index(self) -> int:
        """Message field 'current_path_index'."""
        return self._current_path_index

    @current_path_index.setter
    def current_path_index(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'current_path_index' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'current_path_index' field must be an unsigned integer in [0, 4294967295]"

        self._current_path_index = value

    @builtins.property
    def robot_pose(self) -> geometry_msgs.msg.PoseStamped:
        """Message field 'robot_pose'."""
        return self._robot_pose

    @robot_pose.setter
    def robot_pose(self, value: geometry_msgs.msg.PoseStamped) -> None:
        from geometry_msgs.msg import PoseStamped

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, PoseStamped), \
                    "The 'robot_pose' field must be a sub message of type 'PoseStamped'"

        self._robot_pose = value

    @builtins.property
    def distance_to_goal(self) -> float:
        """Message field 'distance_to_goal'."""
        return self._distance_to_goal

    @distance_to_goal.setter
    def distance_to_goal(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'distance_to_goal' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'distance_to_goal' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._distance_to_goal = value

    @builtins.property
    def speed(self) -> float:
        """Message field 'speed'."""
        return self._speed

    @speed.setter
    def speed(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'speed' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'speed' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._speed = value

    @builtins.property
    def remaining_path_length(self) -> float:
        """Message field 'remaining_path_length'."""
        return self._remaining_path_length

    @remaining_path_length.setter
    def remaining_path_length(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'remaining_path_length' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'remaining_path_length' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._remaining_path_length = value
