# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:action/FollowPath.idl
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
    import nav_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FollowPath_Goal(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_Goal'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_GoalConstants(typing.TypedDict):
        pass

    __constants: FollowPath_GoalConstants = {
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
                'nav2_msgs.action.FollowPath_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__goal

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


class FollowPath_Goal(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_Goal):
    """Message class 'FollowPath_Goal'."""

    __slots__ = [
        '_path',
        '_controller_id',
        '_goal_checker_id',
        '_progress_checker_id',
        '_path_handler_id',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'path': 'nav_msgs/Path',
        'controller_id': 'string',
        'goal_checker_id': 'string',
        'progress_checker_id': 'string',
        'path_handler_id': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['nav_msgs', 'msg'], 'Path'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 path: typing.Optional[nav_msgs.msg.Path] = None,  # noqa: E501
                 controller_id: typing.Optional[str] = None,  # noqa: E501
                 goal_checker_id: typing.Optional[str] = None,  # noqa: E501
                 progress_checker_id: typing.Optional[str] = None,  # noqa: E501
                 path_handler_id: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from nav_msgs.msg import Path
        self.path = path if path is not None else Path()
        self.controller_id = controller_id if controller_id is not None else str()
        self.goal_checker_id = goal_checker_id if goal_checker_id is not None else str()
        self.progress_checker_id = progress_checker_id if progress_checker_id is not None else str()
        self.path_handler_id = path_handler_id if path_handler_id is not None else str()

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
        if not isinstance(other, FollowPath_Goal):
            return False
        if self.path != other.path:
            return False
        if self.controller_id != other.controller_id:
            return False
        if self.goal_checker_id != other.goal_checker_id:
            return False
        if self.progress_checker_id != other.progress_checker_id:
            return False
        if self.path_handler_id != other.path_handler_id:
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
    def controller_id(self) -> str:
        """Message field 'controller_id'."""
        return self._controller_id

    @controller_id.setter
    def controller_id(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'controller_id' field must be of type 'str'"

        self._controller_id = value

    @builtins.property
    def goal_checker_id(self) -> str:
        """Message field 'goal_checker_id'."""
        return self._goal_checker_id

    @goal_checker_id.setter
    def goal_checker_id(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'goal_checker_id' field must be of type 'str'"

        self._goal_checker_id = value

    @builtins.property
    def progress_checker_id(self) -> str:
        """Message field 'progress_checker_id'."""
        return self._progress_checker_id

    @progress_checker_id.setter
    def progress_checker_id(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'progress_checker_id' field must be of type 'str'"

        self._progress_checker_id = value

    @builtins.property
    def path_handler_id(self) -> str:
        """Message field 'path_handler_id'."""
        return self._path_handler_id

    @path_handler_id.setter
    def path_handler_id(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'path_handler_id' field must be of type 'str'"

        self._path_handler_id = value


if typing.TYPE_CHECKING:
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FollowPath_Result(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_Result'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_ResultConstants(typing.TypedDict):
        NONE: typing.Literal[0]
        GOAL_REJECTED: typing.Literal[1]
        SEND_GOAL_FAILURE: typing.Literal[2]
        UNKNOWN: typing.Literal[100]
        INVALID_CONTROLLER: typing.Literal[101]
        TF_ERROR: typing.Literal[102]
        INVALID_PATH: typing.Literal[103]
        PATIENCE_EXCEEDED: typing.Literal[104]
        FAILED_TO_MAKE_PROGRESS: typing.Literal[105]
        NO_VALID_CONTROL: typing.Literal[106]
        CONTROLLER_TIMED_OUT: typing.Literal[107]
        TIMEOUT: typing.Literal[108]

    __constants: FollowPath_ResultConstants = {
        'NONE': 0,
        'GOAL_REJECTED': 1,
        'SEND_GOAL_FAILURE': 2,
        'UNKNOWN': 100,
        'INVALID_CONTROLLER': 101,
        'TF_ERROR': 102,
        'INVALID_PATH': 103,
        'PATIENCE_EXCEEDED': 104,
        'FAILED_TO_MAKE_PROGRESS': 105,
        'NO_VALID_CONTROL': 106,
        'CONTROLLER_TIMED_OUT': 107,
        'TIMEOUT': 108,
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
                'nav2_msgs.action.FollowPath_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__result

            from std_msgs.msg import Empty
            if Empty._TYPE_SUPPORT is None:
                Empty.__import_type_support__()

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
            'INVALID_CONTROLLER': metacls.__constants['INVALID_CONTROLLER'],
            'TF_ERROR': metacls.__constants['TF_ERROR'],
            'INVALID_PATH': metacls.__constants['INVALID_PATH'],
            'PATIENCE_EXCEEDED': metacls.__constants['PATIENCE_EXCEEDED'],
            'FAILED_TO_MAKE_PROGRESS': metacls.__constants['FAILED_TO_MAKE_PROGRESS'],
            'NO_VALID_CONTROL': metacls.__constants['NO_VALID_CONTROL'],
            'CONTROLLER_TIMED_OUT': metacls.__constants['CONTROLLER_TIMED_OUT'],
            'TIMEOUT': metacls.__constants['TIMEOUT'],
        }

    @property
    def NONE(self) -> typing.Literal[0]:
        """Message constant 'NONE'."""
        return Metaclass_FollowPath_Result.__constants['NONE']

    @property
    def GOAL_REJECTED(self) -> typing.Literal[1]:
        """Message constant 'GOAL_REJECTED'."""
        return Metaclass_FollowPath_Result.__constants['GOAL_REJECTED']

    @property
    def SEND_GOAL_FAILURE(self) -> typing.Literal[2]:
        """Message constant 'SEND_GOAL_FAILURE'."""
        return Metaclass_FollowPath_Result.__constants['SEND_GOAL_FAILURE']

    @property
    def UNKNOWN(self) -> typing.Literal[100]:
        """Message constant 'UNKNOWN'."""
        return Metaclass_FollowPath_Result.__constants['UNKNOWN']

    @property
    def INVALID_CONTROLLER(self) -> typing.Literal[101]:
        """Message constant 'INVALID_CONTROLLER'."""
        return Metaclass_FollowPath_Result.__constants['INVALID_CONTROLLER']

    @property
    def TF_ERROR(self) -> typing.Literal[102]:
        """Message constant 'TF_ERROR'."""
        return Metaclass_FollowPath_Result.__constants['TF_ERROR']

    @property
    def INVALID_PATH(self) -> typing.Literal[103]:
        """Message constant 'INVALID_PATH'."""
        return Metaclass_FollowPath_Result.__constants['INVALID_PATH']

    @property
    def PATIENCE_EXCEEDED(self) -> typing.Literal[104]:
        """Message constant 'PATIENCE_EXCEEDED'."""
        return Metaclass_FollowPath_Result.__constants['PATIENCE_EXCEEDED']

    @property
    def FAILED_TO_MAKE_PROGRESS(self) -> typing.Literal[105]:
        """Message constant 'FAILED_TO_MAKE_PROGRESS'."""
        return Metaclass_FollowPath_Result.__constants['FAILED_TO_MAKE_PROGRESS']

    @property
    def NO_VALID_CONTROL(self) -> typing.Literal[106]:
        """Message constant 'NO_VALID_CONTROL'."""
        return Metaclass_FollowPath_Result.__constants['NO_VALID_CONTROL']

    @property
    def CONTROLLER_TIMED_OUT(self) -> typing.Literal[107]:
        """Message constant 'CONTROLLER_TIMED_OUT'."""
        return Metaclass_FollowPath_Result.__constants['CONTROLLER_TIMED_OUT']

    @property
    def TIMEOUT(self) -> typing.Literal[108]:
        """Message constant 'TIMEOUT'."""
        return Metaclass_FollowPath_Result.__constants['TIMEOUT']


class FollowPath_Result(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_Result):
    """
    Message class 'FollowPath_Result'.

    Constants:
      NONE
      GOAL_REJECTED
      SEND_GOAL_FAILURE
      UNKNOWN
      INVALID_CONTROLLER
      TF_ERROR
      INVALID_PATH
      PATIENCE_EXCEEDED
      FAILED_TO_MAKE_PROGRESS
      NO_VALID_CONTROL
      CONTROLLER_TIMED_OUT
      TIMEOUT
    """

    __slots__ = [
        '_result',
        '_error_code',
        '_error_msg',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'result': 'std_msgs/Empty',
        'error_code': 'uint16',
        'error_msg': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Empty'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 result: typing.Optional[std_msgs.msg.Empty] = None,  # noqa: E501
                 error_code: typing.Optional[int] = None,  # noqa: E501
                 error_msg: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Empty
        self.result = result if result is not None else Empty()
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
        if not isinstance(other, FollowPath_Result):
            return False
        if self.result != other.result:
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
    def result(self) -> std_msgs.msg.Empty:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: std_msgs.msg.Empty) -> None:
        from std_msgs.msg import Empty

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Empty), \
                    "The 'result' field must be a sub message of type 'Empty'"

        self._result = value

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


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FollowPath_Feedback(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_Feedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_FeedbackConstants(typing.TypedDict):
        pass

    __constants: FollowPath_FeedbackConstants = {
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
                'nav2_msgs.action.FollowPath_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__feedback

            from nav2_msgs.msg import TrackingFeedback
            if TrackingFeedback._TYPE_SUPPORT is None:
                TrackingFeedback.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FollowPath_Feedback(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_Feedback):
    """Message class 'FollowPath_Feedback'."""

    __slots__ = [
        '_tracking_feedback',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'tracking_feedback': 'nav2_msgs/TrackingFeedback',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'msg'], 'TrackingFeedback'),  # noqa: E501
    )

    def __init__(self, *,
                 tracking_feedback: typing.Optional[nav2_msgs.msg.TrackingFeedback] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from nav2_msgs.msg import TrackingFeedback
        self.tracking_feedback = tracking_feedback if tracking_feedback is not None else TrackingFeedback()

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
        if not isinstance(other, FollowPath_Feedback):
            return False
        if self.tracking_feedback != other.tracking_feedback:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def tracking_feedback(self) -> nav2_msgs.msg.TrackingFeedback:
        """Message field 'tracking_feedback'."""
        return self._tracking_feedback

    @tracking_feedback.setter
    def tracking_feedback(self, value: nav2_msgs.msg.TrackingFeedback) -> None:
        from nav2_msgs.msg import TrackingFeedback

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, TrackingFeedback), \
                    "The 'tracking_feedback' field must be a sub message of type 'TrackingFeedback'"

        self._tracking_feedback = value


if typing.TYPE_CHECKING:
    import nav2_msgs.action._follow_path  # noqa: E402, I100, I201, I300
    import unique_identifier_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FollowPath_SendGoal_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_SendGoal_RequestConstants(typing.TypedDict):
        pass

    __constants: FollowPath_SendGoal_RequestConstants = {
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
                'nav2_msgs.action.FollowPath_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__send_goal__request

            from nav2_msgs.action import FollowPath
            if FollowPath.Goal._TYPE_SUPPORT is None:
                FollowPath.Goal.__import_type_support__()

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


class FollowPath_SendGoal_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_SendGoal_Request):
    """Message class 'FollowPath_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'nav2_msgs/FollowPath_Goal',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'FollowPath_Goal'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 goal: typing.Optional[nav2_msgs.action._follow_path.FollowPath_Goal] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._follow_path import FollowPath_Goal
        self.goal = goal if goal is not None else FollowPath_Goal()

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
        if not isinstance(other, FollowPath_SendGoal_Request):
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
    def goal(self) -> nav2_msgs.action._follow_path.FollowPath_Goal:
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value: nav2_msgs.action._follow_path.FollowPath_Goal) -> None:
        from nav2_msgs.action._follow_path import FollowPath_Goal

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, FollowPath_Goal), \
                    "The 'goal' field must be a sub message of type 'FollowPath_Goal'"

        self._goal = value


if typing.TYPE_CHECKING:
    import builtin_interfaces.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FollowPath_SendGoal_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_SendGoal_ResponseConstants(typing.TypedDict):
        pass

    __constants: FollowPath_SendGoal_ResponseConstants = {
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
                'nav2_msgs.action.FollowPath_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__send_goal__response

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


class FollowPath_SendGoal_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_SendGoal_Response):
    """Message class 'FollowPath_SendGoal_Response'."""

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
        if not isinstance(other, FollowPath_SendGoal_Response):
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


class Metaclass_FollowPath_SendGoal_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_SendGoal_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_SendGoal_EventConstants(typing.TypedDict):
        pass

    __constants: FollowPath_SendGoal_EventConstants = {
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
                'nav2_msgs.action.FollowPath_SendGoal_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__send_goal__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__send_goal__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__send_goal__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__send_goal__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__send_goal__event

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


class FollowPath_SendGoal_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_SendGoal_Event):
    """Message class 'FollowPath_SendGoal_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/FollowPath_SendGoal_Request, 1>',
        'response': 'sequence<nav2_msgs/FollowPath_SendGoal_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'FollowPath_SendGoal_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'FollowPath_SendGoal_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.FollowPath_SendGoal_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.FollowPath_SendGoal_Response]] = None,  # noqa: E501
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
        if not isinstance(other, FollowPath_SendGoal_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.FollowPath_SendGoal_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.FollowPath_SendGoal_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import FollowPath_SendGoal_Request

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
                     all(isinstance(v, FollowPath_SendGoal_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'FollowPath_SendGoal_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.FollowPath_SendGoal_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.FollowPath_SendGoal_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import FollowPath_SendGoal_Response

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
                     all(isinstance(v, FollowPath_SendGoal_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'FollowPath_SendGoal_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias  # noqa: I100, I300


class Metaclass_FollowPath_SendGoal(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'FollowPath_SendGoal'."""

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
                'nav2_msgs.action.FollowPath_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__follow_path__send_goal

            from nav2_msgs.action import _follow_path
            if _follow_path.Metaclass_FollowPath_SendGoal_Request._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_SendGoal_Request.__import_type_support__()
            if _follow_path.Metaclass_FollowPath_SendGoal_Response._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_SendGoal_Response.__import_type_support__()
            if _follow_path.Metaclass_FollowPath_SendGoal_Event._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_SendGoal_Event.__import_type_support__()


class FollowPath_SendGoal(rosidl_pycommon.interface_base_classes.BaseService[
    FollowPath_SendGoal_Request,
    FollowPath_SendGoal_Response
], metaclass=Metaclass_FollowPath_SendGoal):
    Request: TypeAlias = FollowPath_SendGoal_Request
    Response: TypeAlias = FollowPath_SendGoal_Response
    Event: TypeAlias = FollowPath_SendGoal_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FollowPath_GetResult_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_GetResult_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_GetResult_RequestConstants(typing.TypedDict):
        pass

    __constants: FollowPath_GetResult_RequestConstants = {
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
                'nav2_msgs.action.FollowPath_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__get_result__request

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


class FollowPath_GetResult_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_GetResult_Request):
    """Message class 'FollowPath_GetResult_Request'."""

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
        if not isinstance(other, FollowPath_GetResult_Request):
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


class Metaclass_FollowPath_GetResult_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_GetResult_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_GetResult_ResponseConstants(typing.TypedDict):
        pass

    __constants: FollowPath_GetResult_ResponseConstants = {
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
                'nav2_msgs.action.FollowPath_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__get_result__response

            from nav2_msgs.action import FollowPath
            if FollowPath.Result._TYPE_SUPPORT is None:
                FollowPath.Result.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FollowPath_GetResult_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_GetResult_Response):
    """Message class 'FollowPath_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'status': 'int8',
        'result': 'nav2_msgs/FollowPath_Result',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'FollowPath_Result'),  # noqa: E501
    )

    def __init__(self, *,
                 status: typing.Optional[int] = None,  # noqa: E501
                 result: typing.Optional[nav2_msgs.action._follow_path.FollowPath_Result] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.status = status if status is not None else int()
        from nav2_msgs.action._follow_path import FollowPath_Result
        self.result = result if result is not None else FollowPath_Result()

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
        if not isinstance(other, FollowPath_GetResult_Response):
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
    def result(self) -> nav2_msgs.action._follow_path.FollowPath_Result:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: nav2_msgs.action._follow_path.FollowPath_Result) -> None:
        from nav2_msgs.action._follow_path import FollowPath_Result

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, FollowPath_Result), \
                    "The 'result' field must be a sub message of type 'FollowPath_Result'"

        self._result = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FollowPath_GetResult_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_GetResult_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_GetResult_EventConstants(typing.TypedDict):
        pass

    __constants: FollowPath_GetResult_EventConstants = {
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
                'nav2_msgs.action.FollowPath_GetResult_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__get_result__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__get_result__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__get_result__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__get_result__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__get_result__event

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


class FollowPath_GetResult_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_GetResult_Event):
    """Message class 'FollowPath_GetResult_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/FollowPath_GetResult_Request, 1>',
        'response': 'sequence<nav2_msgs/FollowPath_GetResult_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'FollowPath_GetResult_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'FollowPath_GetResult_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.FollowPath_GetResult_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.FollowPath_GetResult_Response]] = None,  # noqa: E501
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
        if not isinstance(other, FollowPath_GetResult_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.FollowPath_GetResult_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.FollowPath_GetResult_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import FollowPath_GetResult_Request

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
                     all(isinstance(v, FollowPath_GetResult_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'FollowPath_GetResult_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.FollowPath_GetResult_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.FollowPath_GetResult_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import FollowPath_GetResult_Response

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
                     all(isinstance(v, FollowPath_GetResult_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'FollowPath_GetResult_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


class Metaclass_FollowPath_GetResult(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'FollowPath_GetResult'."""

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
                'nav2_msgs.action.FollowPath_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__follow_path__get_result

            from nav2_msgs.action import _follow_path
            if _follow_path.Metaclass_FollowPath_GetResult_Request._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_GetResult_Request.__import_type_support__()
            if _follow_path.Metaclass_FollowPath_GetResult_Response._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_GetResult_Response.__import_type_support__()
            if _follow_path.Metaclass_FollowPath_GetResult_Event._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_GetResult_Event.__import_type_support__()


class FollowPath_GetResult(rosidl_pycommon.interface_base_classes.BaseService[
    FollowPath_GetResult_Request,
    FollowPath_GetResult_Response
], metaclass=Metaclass_FollowPath_GetResult):
    Request: TypeAlias = FollowPath_GetResult_Request
    Response: TypeAlias = FollowPath_GetResult_Response
    Event: TypeAlias = FollowPath_GetResult_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_FollowPath_FeedbackMessage(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'FollowPath_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class FollowPath_FeedbackMessageConstants(typing.TypedDict):
        pass

    __constants: FollowPath_FeedbackMessageConstants = {
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
                'nav2_msgs.action.FollowPath_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__follow_path__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__follow_path__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__follow_path__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__follow_path__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__follow_path__feedback_message

            from nav2_msgs.action import FollowPath
            if FollowPath.Feedback._TYPE_SUPPORT is None:
                FollowPath.Feedback.__import_type_support__()

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


class FollowPath_FeedbackMessage(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_FollowPath_FeedbackMessage):
    """Message class 'FollowPath_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'nav2_msgs/FollowPath_Feedback',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'FollowPath_Feedback'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 feedback: typing.Optional[nav2_msgs.action._follow_path.FollowPath_Feedback] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._follow_path import FollowPath_Feedback
        self.feedback = feedback if feedback is not None else FollowPath_Feedback()

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
        if not isinstance(other, FollowPath_FeedbackMessage):
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
    def feedback(self) -> nav2_msgs.action._follow_path.FollowPath_Feedback:
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value: nav2_msgs.action._follow_path.FollowPath_Feedback) -> None:
        from nav2_msgs.action._follow_path import FollowPath_Feedback

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, FollowPath_Feedback), \
                    "The 'feedback' field must be a sub message of type 'FollowPath_Feedback'"

        self._feedback = value


class Metaclass_FollowPath(rosidl_pycommon.interface_base_classes.ActionTypeSupportMeta):
    """Metaclass of action 'FollowPath'."""

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
                'nav2_msgs.action.FollowPath')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__follow_path

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from nav2_msgs.action import _follow_path
            if _follow_path.Metaclass_FollowPath_SendGoal._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_SendGoal.__import_type_support__()
            if _follow_path.Metaclass_FollowPath_GetResult._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_GetResult.__import_type_support__()
            if _follow_path.Metaclass_FollowPath_FeedbackMessage._TYPE_SUPPORT is None:
                _follow_path.Metaclass_FollowPath_FeedbackMessage.__import_type_support__()


class _FollowPath_Impl(rosidl_pycommon.interface_base_classes.BaseImpl[
        FollowPath_SendGoal,
        FollowPath_GetResult,
        FollowPath_FeedbackMessage
]):

    # The send_goal service using a wrapped version of the goal message as a request.
    SendGoalService: TypeAlias = FollowPath_SendGoal
    # The get_result service using a wrapped version of the result message as a response.
    GetResultService: TypeAlias = FollowPath_GetResult
    # The feedback message with generic fields which wraps the feedback message.
    FeedbackMessage: TypeAlias = FollowPath_FeedbackMessage

    # The generic service to cancel a goal.
    from action_msgs.srv._cancel_goal import CancelGoal
    CancelGoalService: TypeAlias = CancelGoal
    # The generic message for get the status of a goal.
    from action_msgs.msg._goal_status_array import GoalStatusArray
    GoalStatusMessage: TypeAlias = GoalStatusArray


class FollowPath(rosidl_pycommon.interface_base_classes.BaseAction[
    FollowPath_Goal,
    FollowPath_Result,
    FollowPath_Feedback,
    _FollowPath_Impl
], metaclass=Metaclass_FollowPath):

    # The goal message defined in the action definition.
    Goal: TypeAlias = FollowPath_Goal
    # The result message defined in the action definition.
    Result: TypeAlias = FollowPath_Result
    # The feedback message defined in the action definition.
    Feedback: TypeAlias = FollowPath_Feedback

    Impl: TypeAlias = _FollowPath_Impl

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Action classes can not be instantiated')
