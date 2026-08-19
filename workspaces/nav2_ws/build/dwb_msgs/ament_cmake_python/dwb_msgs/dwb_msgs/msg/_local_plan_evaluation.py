# generated from rosidl_generator_py/resource/_idl.py.em
# with input from dwb_msgs:msg/LocalPlanEvaluation.idl
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
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_LocalPlanEvaluation(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'LocalPlanEvaluation'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class LocalPlanEvaluationConstants(typing.TypedDict):
        pass

    __constants: LocalPlanEvaluationConstants = {
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
                'dwb_msgs.msg.LocalPlanEvaluation')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__local_plan_evaluation
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__local_plan_evaluation
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__local_plan_evaluation
            cls._TYPE_SUPPORT = module.type_support_msg__msg__local_plan_evaluation
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__local_plan_evaluation

            from dwb_msgs.msg import TrajectoryScore
            if TrajectoryScore._TYPE_SUPPORT is None:
                TrajectoryScore.__import_type_support__()

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


class LocalPlanEvaluation(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_LocalPlanEvaluation):
    """Message class 'LocalPlanEvaluation'."""

    __slots__ = [
        '_header',
        '_twists',
        '_best_index',
        '_worst_index',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'twists': 'sequence<dwb_msgs/TrajectoryScore>',
        'best_index': 'uint16',
        'worst_index': 'uint16',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['dwb_msgs', 'msg'], 'TrajectoryScore')),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 twists: typing.Optional[collections.abc.Sequence[dwb_msgs.msg.TrajectoryScore]] = None,  # noqa: E501
                 best_index: typing.Optional[int] = None,  # noqa: E501
                 worst_index: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.twists = twists if twists is not None else []
        self.best_index = best_index if best_index is not None else int()
        self.worst_index = worst_index if worst_index is not None else int()

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
        if not isinstance(other, LocalPlanEvaluation):
            return False
        if self.header != other.header:
            return False
        if self.twists != other.twists:
            return False
        if self.best_index != other.best_index:
            return False
        if self.worst_index != other.worst_index:
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
    def twists(self) -> typing.Annotated[typing.Any, list[dwb_msgs.msg.TrajectoryScore]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'twists'."""
        return self._twists

    @twists.setter
    def twists(self, value: collections.abc.Sequence[dwb_msgs.msg.TrajectoryScore]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from dwb_msgs.msg import TrajectoryScore

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, TrajectoryScore) for v in value) and
                     True), \
                    "The 'twists' field must be sequence and each value of type 'TrajectoryScore'"

        if isinstance(value, list):
            self._twists = value
            return
        self._twists = list(value)

    @builtins.property
    def best_index(self) -> int:
        """Message field 'best_index'."""
        return self._best_index

    @best_index.setter
    def best_index(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'best_index' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'best_index' field must be an unsigned integer in [0, 65535]"

        self._best_index = value

    @builtins.property
    def worst_index(self) -> int:
        """Message field 'worst_index'."""
        return self._worst_index

    @worst_index.setter
    def worst_index(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'worst_index' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'worst_index' field must be an unsigned integer in [0, 65535]"

        self._worst_index = value
