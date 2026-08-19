# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:action/ComputePathToPose.idl
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


class Metaclass_ComputePathToPose_Goal(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_Goal'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_GoalConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_GoalConstants = {
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
                'nav2_msgs.action.ComputePathToPose_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__goal

            from geometry_msgs.msg import PoseStamped
            if PoseStamped._TYPE_SUPPORT is None:
                PoseStamped.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComputePathToPose_Goal(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_Goal):
    """Message class 'ComputePathToPose_Goal'."""

    __slots__ = [
        '_goal',
        '_start',
        '_viapoints',
        '_planner_id',
        '_use_start',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal': 'geometry_msgs/PoseStamped',
        'start': 'geometry_msgs/PoseStamped',
        'viapoints': 'sequence<geometry_msgs/PoseStamped>',
        'planner_id': 'string',
        'use_start': 'boolean',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped')),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, *,
                 goal: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 start: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 viapoints: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.PoseStamped]] = None,  # noqa: E501
                 planner_id: typing.Optional[str] = None,  # noqa: E501
                 use_start: typing.Optional[bool] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from geometry_msgs.msg import PoseStamped
        self.goal = goal if goal is not None else PoseStamped()
        from geometry_msgs.msg import PoseStamped
        self.start = start if start is not None else PoseStamped()
        self.viapoints = viapoints if viapoints is not None else []
        self.planner_id = planner_id if planner_id is not None else str()
        self.use_start = use_start if use_start is not None else bool()

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
        if not isinstance(other, ComputePathToPose_Goal):
            return False
        if self.goal != other.goal:
            return False
        if self.start != other.start:
            return False
        if self.viapoints != other.viapoints:
            return False
        if self.planner_id != other.planner_id:
            return False
        if self.use_start != other.use_start:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal(self) -> geometry_msgs.msg.PoseStamped:
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value: geometry_msgs.msg.PoseStamped) -> None:
        from geometry_msgs.msg import PoseStamped

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, PoseStamped), \
                    "The 'goal' field must be a sub message of type 'PoseStamped'"

        self._goal = value

    @builtins.property
    def start(self) -> geometry_msgs.msg.PoseStamped:
        """Message field 'start'."""
        return self._start

    @start.setter
    def start(self, value: geometry_msgs.msg.PoseStamped) -> None:
        from geometry_msgs.msg import PoseStamped

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, PoseStamped), \
                    "The 'start' field must be a sub message of type 'PoseStamped'"

        self._start = value

    @builtins.property
    def viapoints(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.PoseStamped]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'viapoints'."""
        return self._viapoints

    @viapoints.setter
    def viapoints(self, value: collections.abc.Sequence[geometry_msgs.msg.PoseStamped]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import PoseStamped

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, PoseStamped) for v in value) and
                     True), \
                    "The 'viapoints' field must be sequence and each value of type 'PoseStamped'"

        if isinstance(value, list):
            self._viapoints = value
            return
        self._viapoints = list(value)

    @builtins.property
    def planner_id(self) -> str:
        """Message field 'planner_id'."""
        return self._planner_id

    @planner_id.setter
    def planner_id(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'planner_id' field must be of type 'str'"

        self._planner_id = value

    @builtins.property
    def use_start(self) -> bool:
        """Message field 'use_start'."""
        return self._use_start

    @use_start.setter
    def use_start(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'use_start' field must be of type 'bool'"

        self._use_start = value


if typing.TYPE_CHECKING:
    import builtin_interfaces.msg  # noqa: E402, I100, I201, I300
    import nav_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_Result(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_Result'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_ResultConstants(typing.TypedDict):
        NONE: typing.Literal[0]
        GOAL_REJECTED: typing.Literal[1]
        SEND_GOAL_FAILURE: typing.Literal[2]
        UNKNOWN: typing.Literal[200]
        INVALID_PLANNER: typing.Literal[201]
        TF_ERROR: typing.Literal[202]
        START_OUTSIDE_MAP: typing.Literal[203]
        GOAL_OUTSIDE_MAP: typing.Literal[204]
        START_OCCUPIED: typing.Literal[205]
        GOAL_OCCUPIED: typing.Literal[206]
        TIMEOUT: typing.Literal[207]
        NO_VALID_PATH: typing.Literal[208]

    __constants: ComputePathToPose_ResultConstants = {
        'NONE': 0,
        'GOAL_REJECTED': 1,
        'SEND_GOAL_FAILURE': 2,
        'UNKNOWN': 200,
        'INVALID_PLANNER': 201,
        'TF_ERROR': 202,
        'START_OUTSIDE_MAP': 203,
        'GOAL_OUTSIDE_MAP': 204,
        'START_OCCUPIED': 205,
        'GOAL_OCCUPIED': 206,
        'TIMEOUT': 207,
        'NO_VALID_PATH': 208,
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
                'nav2_msgs.action.ComputePathToPose_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__result

            from builtin_interfaces.msg import Duration
            if Duration._TYPE_SUPPORT is None:
                Duration.__import_type_support__()

            from nav_msgs.msg import Path
            if Path._TYPE_SUPPORT is None:
                Path.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'NONE': metacls.__constants['NONE'],
            'GOAL_REJECTED': metacls.__constants['GOAL_REJECTED'],
            'SEND_GOAL_FAILURE': metacls.__constants['SEND_GOAL_FAILURE'],
            'UNKNOWN': metacls.__constants['UNKNOWN'],
            'INVALID_PLANNER': metacls.__constants['INVALID_PLANNER'],
            'TF_ERROR': metacls.__constants['TF_ERROR'],
            'START_OUTSIDE_MAP': metacls.__constants['START_OUTSIDE_MAP'],
            'GOAL_OUTSIDE_MAP': metacls.__constants['GOAL_OUTSIDE_MAP'],
            'START_OCCUPIED': metacls.__constants['START_OCCUPIED'],
            'GOAL_OCCUPIED': metacls.__constants['GOAL_OCCUPIED'],
            'TIMEOUT': metacls.__constants['TIMEOUT'],
            'NO_VALID_PATH': metacls.__constants['NO_VALID_PATH'],
        }

    @property
    def NONE(self) -> typing.Literal[0]:
        """Message constant 'NONE'."""
        return Metaclass_ComputePathToPose_Result.__constants['NONE']

    @property
    def GOAL_REJECTED(self) -> typing.Literal[1]:
        """Message constant 'GOAL_REJECTED'."""
        return Metaclass_ComputePathToPose_Result.__constants['GOAL_REJECTED']

    @property
    def SEND_GOAL_FAILURE(self) -> typing.Literal[2]:
        """Message constant 'SEND_GOAL_FAILURE'."""
        return Metaclass_ComputePathToPose_Result.__constants['SEND_GOAL_FAILURE']

    @property
    def UNKNOWN(self) -> typing.Literal[200]:
        """Message constant 'UNKNOWN'."""
        return Metaclass_ComputePathToPose_Result.__constants['UNKNOWN']

    @property
    def INVALID_PLANNER(self) -> typing.Literal[201]:
        """Message constant 'INVALID_PLANNER'."""
        return Metaclass_ComputePathToPose_Result.__constants['INVALID_PLANNER']

    @property
    def TF_ERROR(self) -> typing.Literal[202]:
        """Message constant 'TF_ERROR'."""
        return Metaclass_ComputePathToPose_Result.__constants['TF_ERROR']

    @property
    def START_OUTSIDE_MAP(self) -> typing.Literal[203]:
        """Message constant 'START_OUTSIDE_MAP'."""
        return Metaclass_ComputePathToPose_Result.__constants['START_OUTSIDE_MAP']

    @property
    def GOAL_OUTSIDE_MAP(self) -> typing.Literal[204]:
        """Message constant 'GOAL_OUTSIDE_MAP'."""
        return Metaclass_ComputePathToPose_Result.__constants['GOAL_OUTSIDE_MAP']

    @property
    def START_OCCUPIED(self) -> typing.Literal[205]:
        """Message constant 'START_OCCUPIED'."""
        return Metaclass_ComputePathToPose_Result.__constants['START_OCCUPIED']

    @property
    def GOAL_OCCUPIED(self) -> typing.Literal[206]:
        """Message constant 'GOAL_OCCUPIED'."""
        return Metaclass_ComputePathToPose_Result.__constants['GOAL_OCCUPIED']

    @property
    def TIMEOUT(self) -> typing.Literal[207]:
        """Message constant 'TIMEOUT'."""
        return Metaclass_ComputePathToPose_Result.__constants['TIMEOUT']

    @property
    def NO_VALID_PATH(self) -> typing.Literal[208]:
        """Message constant 'NO_VALID_PATH'."""
        return Metaclass_ComputePathToPose_Result.__constants['NO_VALID_PATH']


class ComputePathToPose_Result(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_Result):
    """
    Message class 'ComputePathToPose_Result'.

    Constants:
      NONE
      GOAL_REJECTED
      SEND_GOAL_FAILURE
      UNKNOWN
      INVALID_PLANNER
      TF_ERROR
      START_OUTSIDE_MAP
      GOAL_OUTSIDE_MAP
      START_OCCUPIED
      GOAL_OCCUPIED
      TIMEOUT
      NO_VALID_PATH
    """

    __slots__ = [
        '_path',
        '_planning_time',
        '_error_code',
        '_error_msg',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'path': 'nav_msgs/Path',
        'planning_time': 'builtin_interfaces/Duration',
        'error_code': 'uint16',
        'error_msg': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['nav_msgs', 'msg'], 'Path'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 path: typing.Optional[nav_msgs.msg.Path] = None,  # noqa: E501
                 planning_time: typing.Optional[builtin_interfaces.msg.Duration] = None,  # noqa: E501
                 error_code: typing.Optional[int] = None,  # noqa: E501
                 error_msg: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from nav_msgs.msg import Path
        self.path = path if path is not None else Path()
        from builtin_interfaces.msg import Duration
        self.planning_time = planning_time if planning_time is not None else Duration()
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
        if not isinstance(other, ComputePathToPose_Result):
            return False
        if self.path != other.path:
            return False
        if self.planning_time != other.planning_time:
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
    def path(self) -> nav_msgs.msg.Path:
        """Message field 'path'."""
        return self._path

    @path.setter
    def path(self, value: nav_msgs.msg.Path) -> None:
        from nav_msgs.msg import Path

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Path), \
                    "The 'path' field must be a sub message of type 'Path'"

        self._path = value

    @builtins.property
    def planning_time(self) -> builtin_interfaces.msg.Duration:
        """Message field 'planning_time'."""
        return self._planning_time

    @planning_time.setter
    def planning_time(self, value: builtin_interfaces.msg.Duration) -> None:
        from builtin_interfaces.msg import Duration

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Duration), \
                    "The 'planning_time' field must be a sub message of type 'Duration'"

        self._planning_time = value

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


# Import statements for member types

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_Feedback(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_Feedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_FeedbackConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_FeedbackConstants = {
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
                'nav2_msgs.action.ComputePathToPose_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__feedback

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComputePathToPose_Feedback(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_Feedback):
    """Message class 'ComputePathToPose_Feedback'."""

    __slots__ = [
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
    )

    def __init__(self, *,
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'

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
        if not isinstance(other, ComputePathToPose_Feedback):
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)


if typing.TYPE_CHECKING:
    import nav2_msgs.action._compute_path_to_pose  # noqa: E402, I100, I201, I300
    import unique_identifier_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_SendGoal_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_SendGoal_RequestConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_SendGoal_RequestConstants = {
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
                'nav2_msgs.action.ComputePathToPose_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__send_goal__request

            from nav2_msgs.action import ComputePathToPose
            if ComputePathToPose.Goal._TYPE_SUPPORT is None:
                ComputePathToPose.Goal.__import_type_support__()

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


class ComputePathToPose_SendGoal_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_SendGoal_Request):
    """Message class 'ComputePathToPose_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'nav2_msgs/ComputePathToPose_Goal',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputePathToPose_Goal'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 goal: typing.Optional[nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Goal] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._compute_path_to_pose import ComputePathToPose_Goal
        self.goal = goal if goal is not None else ComputePathToPose_Goal()

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
        if not isinstance(other, ComputePathToPose_SendGoal_Request):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None:
        from unique_identifier_msgs.msg import UUID

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, UUID), \
                    "The 'goal_id' field must be a sub message of type 'UUID'"

        self._goal_id = value

    @builtins.property
    def goal(self) -> nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Goal:
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value: nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Goal) -> None:
        from nav2_msgs.action._compute_path_to_pose import ComputePathToPose_Goal

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ComputePathToPose_Goal), \
                    "The 'goal' field must be a sub message of type 'ComputePathToPose_Goal'"

        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_SendGoal_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_SendGoal_ResponseConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_SendGoal_ResponseConstants = {
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
                'nav2_msgs.action.ComputePathToPose_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__send_goal__response

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


class ComputePathToPose_SendGoal_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_SendGoal_Response):
    """Message class 'ComputePathToPose_SendGoal_Response'."""

    __slots__ = [
        '_accepted',
        '_stamp',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'accepted': 'boolean',
        'stamp': 'builtin_interfaces/Time',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
    )

    def __init__(self, *,
                 accepted: typing.Optional[bool] = None,  # noqa: E501
                 stamp: typing.Optional[builtin_interfaces.msg.Time] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.accepted = accepted if accepted is not None else bool()
        from builtin_interfaces.msg import Time
        self.stamp = stamp if stamp is not None else Time()

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
        if not isinstance(other, ComputePathToPose_SendGoal_Response):
            return False
        if self.accepted != other.accepted:
            return False
        if self.stamp != other.stamp:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def accepted(self) -> bool:
        """Message field 'accepted'."""
        return self._accepted

    @accepted.setter
    def accepted(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'accepted' field must be of type 'bool'"

        self._accepted = value

    @builtins.property
    def stamp(self) -> builtin_interfaces.msg.Time:
        """Message field 'stamp'."""
        return self._stamp

    @stamp.setter
    def stamp(self, value: builtin_interfaces.msg.Time) -> None:
        from builtin_interfaces.msg import Time

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Time), \
                    "The 'stamp' field must be a sub message of type 'Time'"

        self._stamp = value


if typing.TYPE_CHECKING:
    import nav2_msgs.action  # noqa: E402, I100, I201, I300
    import service_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_SendGoal_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_SendGoal_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_SendGoal_EventConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_SendGoal_EventConstants = {
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
                'nav2_msgs.action.ComputePathToPose_SendGoal_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__send_goal__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__send_goal__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__send_goal__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__send_goal__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__send_goal__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo._TYPE_SUPPORT is None:
                ServiceEventInfo.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComputePathToPose_SendGoal_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_SendGoal_Event):
    """Message class 'ComputePathToPose_SendGoal_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/ComputePathToPose_SendGoal_Request, 1>',
        'response': 'sequence<nav2_msgs/ComputePathToPose_SendGoal_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputePathToPose_SendGoal_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputePathToPose_SendGoal_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_SendGoal_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_SendGoal_Response]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from service_msgs.msg import ServiceEventInfo
        self.info = info if info is not None else ServiceEventInfo()
        self.request = request if request is not None else []
        self.response = response if response is not None else []

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
        if not isinstance(other, ComputePathToPose_SendGoal_Event):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self) -> service_msgs.msg.ServiceEventInfo:
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value: service_msgs.msg.ServiceEventInfo) -> None:
        from service_msgs.msg import ServiceEventInfo

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ServiceEventInfo), \
                    "The 'info' field must be a sub message of type 'ServiceEventInfo'"

        self._info = value

    @builtins.property
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputePathToPose_SendGoal_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_SendGoal_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputePathToPose_SendGoal_Request

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     len(value) <= 1 and
                     all(isinstance(v, ComputePathToPose_SendGoal_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'ComputePathToPose_SendGoal_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputePathToPose_SendGoal_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_SendGoal_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputePathToPose_SendGoal_Response

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     len(value) <= 1 and
                     all(isinstance(v, ComputePathToPose_SendGoal_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'ComputePathToPose_SendGoal_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias  # noqa: I100, I300


class Metaclass_ComputePathToPose_SendGoal(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'ComputePathToPose_SendGoal'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('nav2_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'nav2_msgs.action.ComputePathToPose_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__compute_path_to_pose__send_goal

            from nav2_msgs.action import _compute_path_to_pose
            if _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal_Request._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal_Request.__import_type_support__()
            if _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal_Response._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal_Response.__import_type_support__()
            if _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal_Event._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal_Event.__import_type_support__()


class ComputePathToPose_SendGoal(rosidl_pycommon.interface_base_classes.BaseService[
    ComputePathToPose_SendGoal_Request,
    ComputePathToPose_SendGoal_Response
], metaclass=Metaclass_ComputePathToPose_SendGoal):
    Request: TypeAlias = ComputePathToPose_SendGoal_Request
    Response: TypeAlias = ComputePathToPose_SendGoal_Response
    Event: TypeAlias = ComputePathToPose_SendGoal_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_GetResult_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_GetResult_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_GetResult_RequestConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_GetResult_RequestConstants = {
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
                'nav2_msgs.action.ComputePathToPose_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__get_result__request

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


class ComputePathToPose_GetResult_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_GetResult_Request):
    """Message class 'ComputePathToPose_GetResult_Request'."""

    __slots__ = [
        '_goal_id',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()

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
        if not isinstance(other, ComputePathToPose_GetResult_Request):
            return False
        if self.goal_id != other.goal_id:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None:
        from unique_identifier_msgs.msg import UUID

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, UUID), \
                    "The 'goal_id' field must be a sub message of type 'UUID'"

        self._goal_id = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_GetResult_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_GetResult_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_GetResult_ResponseConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_GetResult_ResponseConstants = {
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
                'nav2_msgs.action.ComputePathToPose_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__get_result__response

            from nav2_msgs.action import ComputePathToPose
            if ComputePathToPose.Result._TYPE_SUPPORT is None:
                ComputePathToPose.Result.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComputePathToPose_GetResult_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_GetResult_Response):
    """Message class 'ComputePathToPose_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'status': 'int8',
        'result': 'nav2_msgs/ComputePathToPose_Result',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputePathToPose_Result'),  # noqa: E501
    )

    def __init__(self, *,
                 status: typing.Optional[int] = None,  # noqa: E501
                 result: typing.Optional[nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Result] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.status = status if status is not None else int()
        from nav2_msgs.action._compute_path_to_pose import ComputePathToPose_Result
        self.result = result if result is not None else ComputePathToPose_Result()

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
        if not isinstance(other, ComputePathToPose_GetResult_Response):
            return False
        if self.status != other.status:
            return False
        if self.result != other.result:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def status(self) -> int:
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'status' field must be of type 'int'"
                assert value >= -128 and value < 128, \
                    "The 'status' field must be an integer in [-128, 127]"

        self._status = value

    @builtins.property
    def result(self) -> nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Result:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Result) -> None:
        from nav2_msgs.action._compute_path_to_pose import ComputePathToPose_Result

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ComputePathToPose_Result), \
                    "The 'result' field must be a sub message of type 'ComputePathToPose_Result'"

        self._result = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_GetResult_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_GetResult_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_GetResult_EventConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_GetResult_EventConstants = {
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
                'nav2_msgs.action.ComputePathToPose_GetResult_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__get_result__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__get_result__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__get_result__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__get_result__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__get_result__event

            from service_msgs.msg import ServiceEventInfo
            if ServiceEventInfo._TYPE_SUPPORT is None:
                ServiceEventInfo.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComputePathToPose_GetResult_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_GetResult_Event):
    """Message class 'ComputePathToPose_GetResult_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/ComputePathToPose_GetResult_Request, 1>',
        'response': 'sequence<nav2_msgs/ComputePathToPose_GetResult_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputePathToPose_GetResult_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputePathToPose_GetResult_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_GetResult_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_GetResult_Response]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from service_msgs.msg import ServiceEventInfo
        self.info = info if info is not None else ServiceEventInfo()
        self.request = request if request is not None else []
        self.response = response if response is not None else []

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
        if not isinstance(other, ComputePathToPose_GetResult_Event):
            return False
        if self.info != other.info:
            return False
        if self.request != other.request:
            return False
        if self.response != other.response:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def info(self) -> service_msgs.msg.ServiceEventInfo:
        """Message field 'info'."""
        return self._info

    @info.setter
    def info(self, value: service_msgs.msg.ServiceEventInfo) -> None:
        from service_msgs.msg import ServiceEventInfo

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ServiceEventInfo), \
                    "The 'info' field must be a sub message of type 'ServiceEventInfo'"

        self._info = value

    @builtins.property
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputePathToPose_GetResult_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_GetResult_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputePathToPose_GetResult_Request

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     len(value) <= 1 and
                     all(isinstance(v, ComputePathToPose_GetResult_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'ComputePathToPose_GetResult_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputePathToPose_GetResult_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.ComputePathToPose_GetResult_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputePathToPose_GetResult_Response

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     len(value) <= 1 and
                     all(isinstance(v, ComputePathToPose_GetResult_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'ComputePathToPose_GetResult_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


class Metaclass_ComputePathToPose_GetResult(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'ComputePathToPose_GetResult'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('nav2_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'nav2_msgs.action.ComputePathToPose_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__compute_path_to_pose__get_result

            from nav2_msgs.action import _compute_path_to_pose
            if _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult_Request._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult_Request.__import_type_support__()
            if _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult_Response._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult_Response.__import_type_support__()
            if _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult_Event._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult_Event.__import_type_support__()


class ComputePathToPose_GetResult(rosidl_pycommon.interface_base_classes.BaseService[
    ComputePathToPose_GetResult_Request,
    ComputePathToPose_GetResult_Response
], metaclass=Metaclass_ComputePathToPose_GetResult):
    Request: TypeAlias = ComputePathToPose_GetResult_Request
    Response: TypeAlias = ComputePathToPose_GetResult_Response
    Event: TypeAlias = ComputePathToPose_GetResult_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputePathToPose_FeedbackMessage(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputePathToPose_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputePathToPose_FeedbackMessageConstants(typing.TypedDict):
        pass

    __constants: ComputePathToPose_FeedbackMessageConstants = {
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
                'nav2_msgs.action.ComputePathToPose_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_path_to_pose__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_path_to_pose__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_path_to_pose__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_path_to_pose__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_path_to_pose__feedback_message

            from nav2_msgs.action import ComputePathToPose
            if ComputePathToPose.Feedback._TYPE_SUPPORT is None:
                ComputePathToPose.Feedback.__import_type_support__()

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


class ComputePathToPose_FeedbackMessage(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputePathToPose_FeedbackMessage):
    """Message class 'ComputePathToPose_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'nav2_msgs/ComputePathToPose_Feedback',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputePathToPose_Feedback'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 feedback: typing.Optional[nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Feedback] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._compute_path_to_pose import ComputePathToPose_Feedback
        self.feedback = feedback if feedback is not None else ComputePathToPose_Feedback()

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
        if not isinstance(other, ComputePathToPose_FeedbackMessage):
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.feedback != other.feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def goal_id(self) -> unique_identifier_msgs.msg.UUID:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: unique_identifier_msgs.msg.UUID) -> None:
        from unique_identifier_msgs.msg import UUID

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, UUID), \
                    "The 'goal_id' field must be a sub message of type 'UUID'"

        self._goal_id = value

    @builtins.property
    def feedback(self) -> nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Feedback:
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value: nav2_msgs.action._compute_path_to_pose.ComputePathToPose_Feedback) -> None:
        from nav2_msgs.action._compute_path_to_pose import ComputePathToPose_Feedback

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ComputePathToPose_Feedback), \
                    "The 'feedback' field must be a sub message of type 'ComputePathToPose_Feedback'"

        self._feedback = value


class Metaclass_ComputePathToPose(rosidl_pycommon.interface_base_classes.ActionTypeSupportMeta):
    """Metaclass of action 'ComputePathToPose'."""

    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    @classmethod
    def __import_type_support__(cls) -> None:
        try:
            from rosidl_generator_py import import_type_support  # type: ignore[attr-defined]
            module = import_type_support('nav2_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'nav2_msgs.action.ComputePathToPose')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__compute_path_to_pose

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from nav2_msgs.action import _compute_path_to_pose
            if _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_SendGoal.__import_type_support__()
            if _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_GetResult.__import_type_support__()
            if _compute_path_to_pose.Metaclass_ComputePathToPose_FeedbackMessage._TYPE_SUPPORT is None:
                _compute_path_to_pose.Metaclass_ComputePathToPose_FeedbackMessage.__import_type_support__()


class _ComputePathToPose_Impl(rosidl_pycommon.interface_base_classes.BaseImpl[
        ComputePathToPose_SendGoal,
        ComputePathToPose_GetResult,
        ComputePathToPose_FeedbackMessage
]):

    # The send_goal service using a wrapped version of the goal message as a request.
    SendGoalService: TypeAlias = ComputePathToPose_SendGoal
    # The get_result service using a wrapped version of the result message as a response.
    GetResultService: TypeAlias = ComputePathToPose_GetResult
    # The feedback message with generic fields which wraps the feedback message.
    FeedbackMessage: TypeAlias = ComputePathToPose_FeedbackMessage

    # The generic service to cancel a goal.
    from action_msgs.srv._cancel_goal import CancelGoal
    CancelGoalService: TypeAlias = CancelGoal
    # The generic message for get the status of a goal.
    from action_msgs.msg._goal_status_array import GoalStatusArray
    GoalStatusMessage: TypeAlias = GoalStatusArray


class ComputePathToPose(rosidl_pycommon.interface_base_classes.BaseAction[
    ComputePathToPose_Goal,
    ComputePathToPose_Result,
    ComputePathToPose_Feedback,
    _ComputePathToPose_Impl
], metaclass=Metaclass_ComputePathToPose):

    # The goal message defined in the action definition.
    Goal: TypeAlias = ComputePathToPose_Goal
    # The result message defined in the action definition.
    Result: TypeAlias = ComputePathToPose_Result
    # The feedback message defined in the action definition.
    Feedback: TypeAlias = ComputePathToPose_Feedback

    Impl: TypeAlias = _ComputePathToPose_Impl

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Action classes can not be instantiated')
