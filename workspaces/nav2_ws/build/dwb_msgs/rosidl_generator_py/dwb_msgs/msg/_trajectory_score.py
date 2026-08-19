# generated from rosidl_generator_py/resource/_idl.py.em
# with input from dwb_msgs:msg/TrajectoryScore.idl
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
    import dwb_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_TrajectoryScore(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'TrajectoryScore'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class TrajectoryScoreConstants(typing.TypedDict):
        pass

    __constants: TrajectoryScoreConstants = {
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
                'dwb_msgs.msg.TrajectoryScore')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__trajectory_score
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__trajectory_score
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__trajectory_score
            cls._TYPE_SUPPORT = module.type_support_msg__msg__trajectory_score
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__trajectory_score

            from dwb_msgs.msg import CriticScore
            if CriticScore._TYPE_SUPPORT is None:
                CriticScore.__import_type_support__()

            from dwb_msgs.msg import Trajectory2D
            if Trajectory2D._TYPE_SUPPORT is None:
                Trajectory2D.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class TrajectoryScore(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_TrajectoryScore):
    """Message class 'TrajectoryScore'."""

    __slots__ = [
        '_traj',
        '_scores',
        '_total',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'traj': 'dwb_msgs/Trajectory2D',
        'scores': 'sequence<dwb_msgs/CriticScore>',
        'total': 'float',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['dwb_msgs', 'msg'], 'Trajectory2D'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['dwb_msgs', 'msg'], 'CriticScore')),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, *,
                 traj: typing.Optional[dwb_msgs.msg.Trajectory2D] = None,  # noqa: E501
                 scores: typing.Optional[collections.abc.Sequence[dwb_msgs.msg.CriticScore]] = None,  # noqa: E501
                 total: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from dwb_msgs.msg import Trajectory2D
        self.traj = traj if traj is not None else Trajectory2D()
        self.scores = scores if scores is not None else []
        self.total = total if total is not None else float()

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
        if not isinstance(other, TrajectoryScore):
            return False
        if self.traj != other.traj:
            return False
        if self.scores != other.scores:
            return False
        if self.total != other.total:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def traj(self) -> dwb_msgs.msg.Trajectory2D:
        """Message field 'traj'."""
        return self._traj

    @traj.setter
    def traj(self, value: dwb_msgs.msg.Trajectory2D) -> None:
        from dwb_msgs.msg import Trajectory2D

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Trajectory2D), \
                    "The 'traj' field must be a sub message of type 'Trajectory2D'"

        self._traj = value

    @builtins.property
    def scores(self) -> typing.Annotated[typing.Any, list[dwb_msgs.msg.CriticScore]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'scores'."""
        return self._scores

    @scores.setter
    def scores(self, value: collections.abc.Sequence[dwb_msgs.msg.CriticScore]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from dwb_msgs.msg import CriticScore

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, CriticScore) for v in value) and
                     True), \
                    "The 'scores' field must be sequence and each value of type 'CriticScore'"

        if isinstance(value, list):
            self._scores = value
            return
        self._scores = list(value)

    @builtins.property
    def total(self) -> float:
        """Message field 'total'."""
        return self._total

    @total.setter
    def total(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'total' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'total' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._total = value
