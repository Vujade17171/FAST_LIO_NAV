# generated from rosidl_generator_py/resource/_idl.py.em
# with input from dwb_msgs:msg/Trajectory2D.idl
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
    import geometry_msgs.msg  # noqa: E402, I100, I201, I300
    import nav_2d_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Trajectory2D(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Trajectory2D'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class Trajectory2DConstants(typing.TypedDict):
        pass

    __constants: Trajectory2DConstants = {
    }

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('dwb_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'dwb_msgs.msg.Trajectory2D')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__trajectory2_d
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__trajectory2_d
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__trajectory2_d
            cls._TYPE_SUPPORT = module.type_support_msg__msg__trajectory2_d
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__trajectory2_d

            from builtin_interfaces.msg import Duration
            if Duration._TYPE_SUPPORT is None:
                Duration.__import_type_support__()

            from geometry_msgs.msg import Pose
            if Pose._TYPE_SUPPORT is None:
                Pose.__import_type_support__()

            from nav_2d_msgs.msg import Twist2D
            if Twist2D._TYPE_SUPPORT is None:
                Twist2D.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Trajectory2D(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Trajectory2D):
    """Message class 'Trajectory2D'."""

    __slots__ = [
        '_velocity',
        '_time_offsets',
        '_poses',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'velocity': 'nav_2d_msgs/Twist2D',
        'time_offsets': 'sequence<builtin_interfaces/Duration>',
        'poses': 'sequence<geometry_msgs/Pose>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['nav_2d_msgs', 'msg'], 'Twist2D'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose')),  # noqa: E501
    )

    def __init__(self, *,
                 velocity: typing.Optional[nav_2d_msgs.msg.Twist2D] = None,  # noqa: E501
                 time_offsets: typing.Optional[collections.abc.Sequence[builtin_interfaces.msg.Duration]] = None,  # noqa: E501
                 poses: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Pose]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from nav_2d_msgs.msg import Twist2D
        self.velocity = velocity if velocity is not None else Twist2D()
        self.time_offsets = time_offsets if time_offsets is not None else []
        self.poses = poses if poses is not None else []

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
        if not isinstance(other, Trajectory2D):
            return False
        if self.velocity != other.velocity:
            return False
        if self.time_offsets != other.time_offsets:
            return False
        if self.poses != other.poses:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def velocity(self) -> nav_2d_msgs.msg.Twist2D:
        """Message field 'velocity'."""
        return self._velocity

    @velocity.setter
    def velocity(self, value: nav_2d_msgs.msg.Twist2D) -> None:
        from nav_2d_msgs.msg import Twist2D

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Twist2D), \
                    "The 'velocity' field must be a sub message of type 'Twist2D'"

        self._velocity = value

    @builtins.property
    def time_offsets(self) -> typing.Annotated[typing.Any, list[builtin_interfaces.msg.Duration]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'time_offsets'."""
        return self._time_offsets

    @time_offsets.setter
    def time_offsets(self, value: collections.abc.Sequence[builtin_interfaces.msg.Duration]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from builtin_interfaces.msg import Duration

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Duration) for v in value) and
                     True), \
                    "The 'time_offsets' field must be sequence and each value of type 'Duration'"

        if isinstance(value, list):
            self._time_offsets = value
            return
        self._time_offsets = list(value)

    @builtins.property
    def poses(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Pose]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'poses'."""
        return self._poses

    @poses.setter
    def poses(self, value: collections.abc.Sequence[geometry_msgs.msg.Pose]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Pose

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Pose) for v in value) and
                     True), \
                    "The 'poses' field must be sequence and each value of type 'Pose'"

        if isinstance(value, list):
            self._poses = value
            return
        self._poses = list(value)
