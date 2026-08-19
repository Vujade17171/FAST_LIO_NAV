# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:action/ComputeAndTrackRoute.idl
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


class Metaclass_ComputeAndTrackRoute_Goal(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_Goal'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_GoalConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_GoalConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__goal

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


class ComputeAndTrackRoute_Goal(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_Goal):
    """Message class 'ComputeAndTrackRoute_Goal'."""

    __slots__ = [
        '_start_id',
        '_start',
        '_goal_id',
        '_goal',
        '_use_start',
        '_use_poses',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'start_id': 'uint16',
        'start': 'geometry_msgs/PoseStamped',
        'goal_id': 'uint16',
        'goal': 'geometry_msgs/PoseStamped',
        'use_start': 'boolean',
        'use_poses': 'boolean',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, *,
                 start_id: typing.Optional[int] = None,  # noqa: E501
                 start: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 goal_id: typing.Optional[int] = None,  # noqa: E501
                 goal: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 use_start: typing.Optional[bool] = None,  # noqa: E501
                 use_poses: typing.Optional[bool] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.start_id = start_id if start_id is not None else int()
        from geometry_msgs.msg import PoseStamped
        self.start = start if start is not None else PoseStamped()
        self.goal_id = goal_id if goal_id is not None else int()
        from geometry_msgs.msg import PoseStamped
        self.goal = goal if goal is not None else PoseStamped()
        self.use_start = use_start if use_start is not None else bool()
        self.use_poses = use_poses if use_poses is not None else bool()

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
        if not isinstance(other, ComputeAndTrackRoute_Goal):
            return False
        if self.start_id != other.start_id:
            return False
        if self.start != other.start:
            return False
        if self.goal_id != other.goal_id:
            return False
        if self.goal != other.goal:
            return False
        if self.use_start != other.use_start:
            return False
        if self.use_poses != other.use_poses:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def start_id(self) -> int:
        """Message field 'start_id'."""
        return self._start_id

    @start_id.setter
    def start_id(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'start_id' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'start_id' field must be an unsigned integer in [0, 65535]"

        self._start_id = value

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
    def goal_id(self) -> int:
        """Message field 'goal_id'."""
        return self._goal_id

    @goal_id.setter
    def goal_id(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'goal_id' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'goal_id' field must be an unsigned integer in [0, 65535]"

        self._goal_id = value

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

    @builtins.property
    def use_poses(self) -> bool:
        """Message field 'use_poses'."""
        return self._use_poses

    @use_poses.setter
    def use_poses(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'use_poses' field must be of type 'bool'"

        self._use_poses = value


if typing.TYPE_CHECKING:
    import builtin_interfaces.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputeAndTrackRoute_Result(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_Result'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_ResultConstants(typing.TypedDict):
        NONE: typing.Literal[0]
        GOAL_REJECTED: typing.Literal[1]
        SEND_GOAL_FAILURE: typing.Literal[2]
        UNKNOWN: typing.Literal[400]
        TF_ERROR: typing.Literal[401]
        NO_VALID_GRAPH: typing.Literal[402]
        INDETERMINANT_NODES_ON_GRAPH: typing.Literal[403]
        TIMEOUT: typing.Literal[404]
        NO_VALID_ROUTE: typing.Literal[405]
        OPERATION_FAILED: typing.Literal[406]
        INVALID_EDGE_SCORER_USE: typing.Literal[407]

    __constants: ComputeAndTrackRoute_ResultConstants = {
        'NONE': 0,
        'GOAL_REJECTED': 1,
        'SEND_GOAL_FAILURE': 2,
        'UNKNOWN': 400,
        'TF_ERROR': 401,
        'NO_VALID_GRAPH': 402,
        'INDETERMINANT_NODES_ON_GRAPH': 403,
        'TIMEOUT': 404,
        'NO_VALID_ROUTE': 405,
        'OPERATION_FAILED': 406,
        'INVALID_EDGE_SCORER_USE': 407,
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
                'nav2_msgs.action.ComputeAndTrackRoute_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__result

            from builtin_interfaces.msg import Duration
            if Duration._TYPE_SUPPORT is None:
                Duration.__import_type_support__()

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
            'TF_ERROR': metacls.__constants['TF_ERROR'],
            'NO_VALID_GRAPH': metacls.__constants['NO_VALID_GRAPH'],
            'INDETERMINANT_NODES_ON_GRAPH': metacls.__constants['INDETERMINANT_NODES_ON_GRAPH'],
            'TIMEOUT': metacls.__constants['TIMEOUT'],
            'NO_VALID_ROUTE': metacls.__constants['NO_VALID_ROUTE'],
            'OPERATION_FAILED': metacls.__constants['OPERATION_FAILED'],
            'INVALID_EDGE_SCORER_USE': metacls.__constants['INVALID_EDGE_SCORER_USE'],
            'ERROR_CODE__DEFAULT': 0,
        }

    @property
    def NONE(self) -> typing.Literal[0]:
        """Message constant 'NONE'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['NONE']

    @property
    def GOAL_REJECTED(self) -> typing.Literal[1]:
        """Message constant 'GOAL_REJECTED'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['GOAL_REJECTED']

    @property
    def SEND_GOAL_FAILURE(self) -> typing.Literal[2]:
        """Message constant 'SEND_GOAL_FAILURE'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['SEND_GOAL_FAILURE']

    @property
    def UNKNOWN(self) -> typing.Literal[400]:
        """Message constant 'UNKNOWN'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['UNKNOWN']

    @property
    def TF_ERROR(self) -> typing.Literal[401]:
        """Message constant 'TF_ERROR'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['TF_ERROR']

    @property
    def NO_VALID_GRAPH(self) -> typing.Literal[402]:
        """Message constant 'NO_VALID_GRAPH'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['NO_VALID_GRAPH']

    @property
    def INDETERMINANT_NODES_ON_GRAPH(self) -> typing.Literal[403]:
        """Message constant 'INDETERMINANT_NODES_ON_GRAPH'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['INDETERMINANT_NODES_ON_GRAPH']

    @property
    def TIMEOUT(self) -> typing.Literal[404]:
        """Message constant 'TIMEOUT'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['TIMEOUT']

    @property
    def NO_VALID_ROUTE(self) -> typing.Literal[405]:
        """Message constant 'NO_VALID_ROUTE'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['NO_VALID_ROUTE']

    @property
    def OPERATION_FAILED(self) -> typing.Literal[406]:
        """Message constant 'OPERATION_FAILED'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['OPERATION_FAILED']

    @property
    def INVALID_EDGE_SCORER_USE(self) -> typing.Literal[407]:
        """Message constant 'INVALID_EDGE_SCORER_USE'."""
        return Metaclass_ComputeAndTrackRoute_Result.__constants['INVALID_EDGE_SCORER_USE']

    @property
    def ERROR_CODE__DEFAULT(cls) -> typing.Literal[0]:
        """Return default value for message field 'error_code'."""
        return 0


class ComputeAndTrackRoute_Result(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_Result):
    """
    Message class 'ComputeAndTrackRoute_Result'.

    Constants:
      NONE
      GOAL_REJECTED
      SEND_GOAL_FAILURE
      UNKNOWN
      TF_ERROR
      NO_VALID_GRAPH
      INDETERMINANT_NODES_ON_GRAPH
      TIMEOUT
      NO_VALID_ROUTE
      OPERATION_FAILED
      INVALID_EDGE_SCORER_USE
    """

    __slots__ = [
        '_execution_duration',
        '_error_code',
        '_error_msg',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'execution_duration': 'builtin_interfaces/Duration',
        'error_code': 'uint16',
        'error_msg': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 execution_duration: typing.Optional[builtin_interfaces.msg.Duration] = None,  # noqa: E501
                 error_code: typing.Optional[int] = None,  # noqa: E501
                 error_msg: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from builtin_interfaces.msg import Duration
        self.execution_duration = execution_duration if execution_duration is not None else Duration()
        self.error_code = error_code if error_code is not None else ComputeAndTrackRoute_Result.ERROR_CODE__DEFAULT
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
        if not isinstance(other, ComputeAndTrackRoute_Result):
            return False
        if self.execution_duration != other.execution_duration:
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
    def execution_duration(self) -> builtin_interfaces.msg.Duration:
        """Message field 'execution_duration'."""
        return self._execution_duration

    @execution_duration.setter
    def execution_duration(self, value: builtin_interfaces.msg.Duration) -> None:
        from builtin_interfaces.msg import Duration

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Duration), \
                    "The 'execution_duration' field must be a sub message of type 'Duration'"

        self._execution_duration = value

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


if typing.TYPE_CHECKING:
    import nav2_msgs.msg  # noqa: E402, I100, I201, I300
    import nav_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputeAndTrackRoute_Feedback(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_Feedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_FeedbackConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_FeedbackConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__feedback

            from nav2_msgs.msg import Route
            if Route._TYPE_SUPPORT is None:
                Route.__import_type_support__()

            from nav_msgs.msg import Path
            if Path._TYPE_SUPPORT is None:
                Path.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComputeAndTrackRoute_Feedback(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_Feedback):
    """Message class 'ComputeAndTrackRoute_Feedback'."""

    __slots__ = [
        '_last_node_id',
        '_next_node_id',
        '_current_edge_id',
        '_route',
        '_path',
        '_operations_triggered',
        '_rerouted',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'last_node_id': 'uint16',
        'next_node_id': 'uint16',
        'current_edge_id': 'uint16',
        'route': 'nav2_msgs/Route',
        'path': 'nav_msgs/Path',
        'operations_triggered': 'sequence<string>',
        'rerouted': 'boolean',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'msg'], 'Route'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav_msgs', 'msg'], 'Path'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.UnboundedString()),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, *,
                 last_node_id: typing.Optional[int] = None,  # noqa: E501
                 next_node_id: typing.Optional[int] = None,  # noqa: E501
                 current_edge_id: typing.Optional[int] = None,  # noqa: E501
                 route: typing.Optional[nav2_msgs.msg.Route] = None,  # noqa: E501
                 path: typing.Optional[nav_msgs.msg.Path] = None,  # noqa: E501
                 operations_triggered: typing.Optional[collections.abc.Sequence[str]] = None,  # noqa: E501
                 rerouted: typing.Optional[bool] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.last_node_id = last_node_id if last_node_id is not None else int()
        self.next_node_id = next_node_id if next_node_id is not None else int()
        self.current_edge_id = current_edge_id if current_edge_id is not None else int()
        from nav2_msgs.msg import Route
        self.route = route if route is not None else Route()
        from nav_msgs.msg import Path
        self.path = path if path is not None else Path()
        self.operations_triggered = operations_triggered if operations_triggered is not None else []
        self.rerouted = rerouted if rerouted is not None else bool()

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
        if not isinstance(other, ComputeAndTrackRoute_Feedback):
            return False
        if self.last_node_id != other.last_node_id:
            return False
        if self.next_node_id != other.next_node_id:
            return False
        if self.current_edge_id != other.current_edge_id:
            return False
        if self.route != other.route:
            return False
        if self.path != other.path:
            return False
        if self.operations_triggered != other.operations_triggered:
            return False
        if self.rerouted != other.rerouted:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def last_node_id(self) -> int:
        """Message field 'last_node_id'."""
        return self._last_node_id

    @last_node_id.setter
    def last_node_id(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'last_node_id' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'last_node_id' field must be an unsigned integer in [0, 65535]"

        self._last_node_id = value

    @builtins.property
    def next_node_id(self) -> int:
        """Message field 'next_node_id'."""
        return self._next_node_id

    @next_node_id.setter
    def next_node_id(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'next_node_id' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'next_node_id' field must be an unsigned integer in [0, 65535]"

        self._next_node_id = value

    @builtins.property
    def current_edge_id(self) -> int:
        """Message field 'current_edge_id'."""
        return self._current_edge_id

    @current_edge_id.setter
    def current_edge_id(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'current_edge_id' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'current_edge_id' field must be an unsigned integer in [0, 65535]"

        self._current_edge_id = value

    @builtins.property
    def route(self) -> nav2_msgs.msg.Route:
        """Message field 'route'."""
        return self._route

    @route.setter
    def route(self, value: nav2_msgs.msg.Route) -> None:
        from nav2_msgs.msg import Route

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Route), \
                    "The 'route' field must be a sub message of type 'Route'"

        self._route = value

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
    def operations_triggered(self) -> typing.Annotated[typing.Any, list[str]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'operations_triggered'."""
        return self._operations_triggered

    @operations_triggered.setter
    def operations_triggered(self, value: collections.abc.Sequence[str]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, str) for v in value) and
                     True), \
                    "The 'operations_triggered' field must be sequence and each value of type 'str'"

        if isinstance(value, list):
            self._operations_triggered = value
            return
        self._operations_triggered = list(value)

    @builtins.property
    def rerouted(self) -> bool:
        """Message field 'rerouted'."""
        return self._rerouted

    @rerouted.setter
    def rerouted(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'rerouted' field must be of type 'bool'"

        self._rerouted = value


if typing.TYPE_CHECKING:
    import nav2_msgs.action._compute_and_track_route  # noqa: E402, I100, I201, I300
    import unique_identifier_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputeAndTrackRoute_SendGoal_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_SendGoal_RequestConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_SendGoal_RequestConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__send_goal__request

            from nav2_msgs.action import ComputeAndTrackRoute
            if ComputeAndTrackRoute.Goal._TYPE_SUPPORT is None:
                ComputeAndTrackRoute.Goal.__import_type_support__()

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


class ComputeAndTrackRoute_SendGoal_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_SendGoal_Request):
    """Message class 'ComputeAndTrackRoute_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'nav2_msgs/ComputeAndTrackRoute_Goal',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputeAndTrackRoute_Goal'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 goal: typing.Optional[nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Goal] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._compute_and_track_route import ComputeAndTrackRoute_Goal
        self.goal = goal if goal is not None else ComputeAndTrackRoute_Goal()

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
        if not isinstance(other, ComputeAndTrackRoute_SendGoal_Request):
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
    def goal(self) -> nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Goal:
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value: nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Goal) -> None:
        from nav2_msgs.action._compute_and_track_route import ComputeAndTrackRoute_Goal

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ComputeAndTrackRoute_Goal), \
                    "The 'goal' field must be a sub message of type 'ComputeAndTrackRoute_Goal'"

        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputeAndTrackRoute_SendGoal_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_SendGoal_ResponseConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_SendGoal_ResponseConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__send_goal__response

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


class ComputeAndTrackRoute_SendGoal_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_SendGoal_Response):
    """Message class 'ComputeAndTrackRoute_SendGoal_Response'."""

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
        if not isinstance(other, ComputeAndTrackRoute_SendGoal_Response):
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


class Metaclass_ComputeAndTrackRoute_SendGoal_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_SendGoal_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_SendGoal_EventConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_SendGoal_EventConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__send_goal__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__send_goal__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__send_goal__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__send_goal__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__send_goal__event

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


class ComputeAndTrackRoute_SendGoal_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_SendGoal_Event):
    """Message class 'ComputeAndTrackRoute_SendGoal_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/ComputeAndTrackRoute_SendGoal_Request, 1>',
        'response': 'sequence<nav2_msgs/ComputeAndTrackRoute_SendGoal_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputeAndTrackRoute_SendGoal_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputeAndTrackRoute_SendGoal_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Response]] = None,  # noqa: E501
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
        if not isinstance(other, ComputeAndTrackRoute_SendGoal_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputeAndTrackRoute_SendGoal_Request

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
                     all(isinstance(v, ComputeAndTrackRoute_SendGoal_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'ComputeAndTrackRoute_SendGoal_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_SendGoal_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputeAndTrackRoute_SendGoal_Response

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
                     all(isinstance(v, ComputeAndTrackRoute_SendGoal_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'ComputeAndTrackRoute_SendGoal_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias  # noqa: I100, I300


class Metaclass_ComputeAndTrackRoute_SendGoal(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'ComputeAndTrackRoute_SendGoal'."""

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
                'nav2_msgs.action.ComputeAndTrackRoute_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__compute_and_track_route__send_goal

            from nav2_msgs.action import _compute_and_track_route
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal_Request._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal_Request.__import_type_support__()
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal_Response._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal_Response.__import_type_support__()
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal_Event._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal_Event.__import_type_support__()


class ComputeAndTrackRoute_SendGoal(rosidl_pycommon.interface_base_classes.BaseService[
    ComputeAndTrackRoute_SendGoal_Request,
    ComputeAndTrackRoute_SendGoal_Response
], metaclass=Metaclass_ComputeAndTrackRoute_SendGoal):
    Request: TypeAlias = ComputeAndTrackRoute_SendGoal_Request
    Response: TypeAlias = ComputeAndTrackRoute_SendGoal_Response
    Event: TypeAlias = ComputeAndTrackRoute_SendGoal_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputeAndTrackRoute_GetResult_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_GetResult_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_GetResult_RequestConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_GetResult_RequestConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__get_result__request

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


class ComputeAndTrackRoute_GetResult_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_GetResult_Request):
    """Message class 'ComputeAndTrackRoute_GetResult_Request'."""

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
        if not isinstance(other, ComputeAndTrackRoute_GetResult_Request):
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


class Metaclass_ComputeAndTrackRoute_GetResult_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_GetResult_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_GetResult_ResponseConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_GetResult_ResponseConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__get_result__response

            from nav2_msgs.action import ComputeAndTrackRoute
            if ComputeAndTrackRoute.Result._TYPE_SUPPORT is None:
                ComputeAndTrackRoute.Result.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ComputeAndTrackRoute_GetResult_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_GetResult_Response):
    """Message class 'ComputeAndTrackRoute_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'status': 'int8',
        'result': 'nav2_msgs/ComputeAndTrackRoute_Result',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputeAndTrackRoute_Result'),  # noqa: E501
    )

    def __init__(self, *,
                 status: typing.Optional[int] = None,  # noqa: E501
                 result: typing.Optional[nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Result] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.status = status if status is not None else int()
        from nav2_msgs.action._compute_and_track_route import ComputeAndTrackRoute_Result
        self.result = result if result is not None else ComputeAndTrackRoute_Result()

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
        if not isinstance(other, ComputeAndTrackRoute_GetResult_Response):
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
    def result(self) -> nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Result:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Result) -> None:
        from nav2_msgs.action._compute_and_track_route import ComputeAndTrackRoute_Result

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ComputeAndTrackRoute_Result), \
                    "The 'result' field must be a sub message of type 'ComputeAndTrackRoute_Result'"

        self._result = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputeAndTrackRoute_GetResult_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_GetResult_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_GetResult_EventConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_GetResult_EventConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_GetResult_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__get_result__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__get_result__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__get_result__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__get_result__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__get_result__event

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


class ComputeAndTrackRoute_GetResult_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_GetResult_Event):
    """Message class 'ComputeAndTrackRoute_GetResult_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/ComputeAndTrackRoute_GetResult_Request, 1>',
        'response': 'sequence<nav2_msgs/ComputeAndTrackRoute_GetResult_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputeAndTrackRoute_GetResult_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputeAndTrackRoute_GetResult_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_GetResult_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_GetResult_Response]] = None,  # noqa: E501
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
        if not isinstance(other, ComputeAndTrackRoute_GetResult_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputeAndTrackRoute_GetResult_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_GetResult_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputeAndTrackRoute_GetResult_Request

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
                     all(isinstance(v, ComputeAndTrackRoute_GetResult_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'ComputeAndTrackRoute_GetResult_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.ComputeAndTrackRoute_GetResult_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.ComputeAndTrackRoute_GetResult_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import ComputeAndTrackRoute_GetResult_Response

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
                     all(isinstance(v, ComputeAndTrackRoute_GetResult_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'ComputeAndTrackRoute_GetResult_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


class Metaclass_ComputeAndTrackRoute_GetResult(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'ComputeAndTrackRoute_GetResult'."""

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
                'nav2_msgs.action.ComputeAndTrackRoute_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__compute_and_track_route__get_result

            from nav2_msgs.action import _compute_and_track_route
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult_Request._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult_Request.__import_type_support__()
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult_Response._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult_Response.__import_type_support__()
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult_Event._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult_Event.__import_type_support__()


class ComputeAndTrackRoute_GetResult(rosidl_pycommon.interface_base_classes.BaseService[
    ComputeAndTrackRoute_GetResult_Request,
    ComputeAndTrackRoute_GetResult_Response
], metaclass=Metaclass_ComputeAndTrackRoute_GetResult):
    Request: TypeAlias = ComputeAndTrackRoute_GetResult_Request
    Response: TypeAlias = ComputeAndTrackRoute_GetResult_Response
    Event: TypeAlias = ComputeAndTrackRoute_GetResult_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_ComputeAndTrackRoute_FeedbackMessage(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ComputeAndTrackRoute_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ComputeAndTrackRoute_FeedbackMessageConstants(typing.TypedDict):
        pass

    __constants: ComputeAndTrackRoute_FeedbackMessageConstants = {
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
                'nav2_msgs.action.ComputeAndTrackRoute_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__compute_and_track_route__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__compute_and_track_route__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__compute_and_track_route__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__compute_and_track_route__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__compute_and_track_route__feedback_message

            from nav2_msgs.action import ComputeAndTrackRoute
            if ComputeAndTrackRoute.Feedback._TYPE_SUPPORT is None:
                ComputeAndTrackRoute.Feedback.__import_type_support__()

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


class ComputeAndTrackRoute_FeedbackMessage(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ComputeAndTrackRoute_FeedbackMessage):
    """Message class 'ComputeAndTrackRoute_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'nav2_msgs/ComputeAndTrackRoute_Feedback',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'ComputeAndTrackRoute_Feedback'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 feedback: typing.Optional[nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Feedback] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._compute_and_track_route import ComputeAndTrackRoute_Feedback
        self.feedback = feedback if feedback is not None else ComputeAndTrackRoute_Feedback()

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
        if not isinstance(other, ComputeAndTrackRoute_FeedbackMessage):
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
    def feedback(self) -> nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Feedback:
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value: nav2_msgs.action._compute_and_track_route.ComputeAndTrackRoute_Feedback) -> None:
        from nav2_msgs.action._compute_and_track_route import ComputeAndTrackRoute_Feedback

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, ComputeAndTrackRoute_Feedback), \
                    "The 'feedback' field must be a sub message of type 'ComputeAndTrackRoute_Feedback'"

        self._feedback = value


class Metaclass_ComputeAndTrackRoute(rosidl_pycommon.interface_base_classes.ActionTypeSupportMeta):
    """Metaclass of action 'ComputeAndTrackRoute'."""

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
                'nav2_msgs.action.ComputeAndTrackRoute')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__compute_and_track_route

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from nav2_msgs.action import _compute_and_track_route
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_SendGoal.__import_type_support__()
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_GetResult.__import_type_support__()
            if _compute_and_track_route.Metaclass_ComputeAndTrackRoute_FeedbackMessage._TYPE_SUPPORT is None:
                _compute_and_track_route.Metaclass_ComputeAndTrackRoute_FeedbackMessage.__import_type_support__()


class _ComputeAndTrackRoute_Impl(rosidl_pycommon.interface_base_classes.BaseImpl[
        ComputeAndTrackRoute_SendGoal,
        ComputeAndTrackRoute_GetResult,
        ComputeAndTrackRoute_FeedbackMessage
]):

    # The send_goal service using a wrapped version of the goal message as a request.
    SendGoalService: TypeAlias = ComputeAndTrackRoute_SendGoal
    # The get_result service using a wrapped version of the result message as a response.
    GetResultService: TypeAlias = ComputeAndTrackRoute_GetResult
    # The feedback message with generic fields which wraps the feedback message.
    FeedbackMessage: TypeAlias = ComputeAndTrackRoute_FeedbackMessage

    # The generic service to cancel a goal.
    from action_msgs.srv._cancel_goal import CancelGoal
    CancelGoalService: TypeAlias = CancelGoal
    # The generic message for get the status of a goal.
    from action_msgs.msg._goal_status_array import GoalStatusArray
    GoalStatusMessage: TypeAlias = GoalStatusArray


class ComputeAndTrackRoute(rosidl_pycommon.interface_base_classes.BaseAction[
    ComputeAndTrackRoute_Goal,
    ComputeAndTrackRoute_Result,
    ComputeAndTrackRoute_Feedback,
    _ComputeAndTrackRoute_Impl
], metaclass=Metaclass_ComputeAndTrackRoute):

    # The goal message defined in the action definition.
    Goal: TypeAlias = ComputeAndTrackRoute_Goal
    # The result message defined in the action definition.
    Result: TypeAlias = ComputeAndTrackRoute_Result
    # The feedback message defined in the action definition.
    Feedback: TypeAlias = ComputeAndTrackRoute_Feedback

    Impl: TypeAlias = _ComputeAndTrackRoute_Impl

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Action classes can not be instantiated')
