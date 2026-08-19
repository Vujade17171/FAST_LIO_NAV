# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:action/DockRobot.idl
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

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_DockRobot_Goal(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_Goal'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_GoalConstants(typing.TypedDict):
        pass

    __constants: DockRobot_GoalConstants = {
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
                'nav2_msgs.action.DockRobot_Goal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__goal
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__goal
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__goal
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__goal
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__goal

            from geometry_msgs.msg import PoseStamped
            if PoseStamped._TYPE_SUPPORT is None:
                PoseStamped.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'USE_DOCK_ID__DEFAULT': True,
            'MAX_STAGING_TIME__DEFAULT': 1000.0,
            'NAVIGATE_TO_STAGING_POSE__DEFAULT': True,
        }

    @property
    def USE_DOCK_ID__DEFAULT(cls) -> typing.Literal[True]:
        """Return default value for message field 'use_dock_id'."""
        return True

    @property
    def MAX_STAGING_TIME__DEFAULT(cls) -> float:
        """Return default value for message field 'max_staging_time'."""
        return 1000.0

    @property
    def NAVIGATE_TO_STAGING_POSE__DEFAULT(cls) -> typing.Literal[True]:
        """Return default value for message field 'navigate_to_staging_pose'."""
        return True


class DockRobot_Goal(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_Goal):
    """Message class 'DockRobot_Goal'."""

    __slots__ = [
        '_use_dock_id',
        '_dock_id',
        '_dock_pose',
        '_dock_type',
        '_max_staging_time',
        '_navigate_to_staging_pose',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'use_dock_id': 'boolean',
        'dock_id': 'string',
        'dock_pose': 'geometry_msgs/PoseStamped',
        'dock_type': 'string',
        'max_staging_time': 'float',
        'navigate_to_staging_pose': 'boolean',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'PoseStamped'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, *,
                 use_dock_id: typing.Optional[bool] = None,  # noqa: E501
                 dock_id: typing.Optional[str] = None,  # noqa: E501
                 dock_pose: typing.Optional[geometry_msgs.msg.PoseStamped] = None,  # noqa: E501
                 dock_type: typing.Optional[str] = None,  # noqa: E501
                 max_staging_time: typing.Optional[float] = None,  # noqa: E501
                 navigate_to_staging_pose: typing.Optional[bool] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.use_dock_id = use_dock_id if use_dock_id is not None else DockRobot_Goal.USE_DOCK_ID__DEFAULT
        self.dock_id = dock_id if dock_id is not None else str()
        from geometry_msgs.msg import PoseStamped
        self.dock_pose = dock_pose if dock_pose is not None else PoseStamped()
        self.dock_type = dock_type if dock_type is not None else str()
        self.max_staging_time = max_staging_time if max_staging_time is not None else DockRobot_Goal.MAX_STAGING_TIME__DEFAULT
        self.navigate_to_staging_pose = navigate_to_staging_pose if navigate_to_staging_pose is not None else DockRobot_Goal.NAVIGATE_TO_STAGING_POSE__DEFAULT

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
        if not isinstance(other, DockRobot_Goal):
            return False
        if self.use_dock_id != other.use_dock_id:
            return False
        if self.dock_id != other.dock_id:
            return False
        if self.dock_pose != other.dock_pose:
            return False
        if self.dock_type != other.dock_type:
            return False
        if self.max_staging_time != other.max_staging_time:
            return False
        if self.navigate_to_staging_pose != other.navigate_to_staging_pose:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def use_dock_id(self) -> bool:
        """Message field 'use_dock_id'."""
        return self._use_dock_id

    @use_dock_id.setter
    def use_dock_id(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'use_dock_id' field must be of type 'bool'"

        self._use_dock_id = value

    @builtins.property
    def dock_id(self) -> str:
        """Message field 'dock_id'."""
        return self._dock_id

    @dock_id.setter
    def dock_id(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'dock_id' field must be of type 'str'"

        self._dock_id = value

    @builtins.property
    def dock_pose(self) -> geometry_msgs.msg.PoseStamped:
        """Message field 'dock_pose'."""
        return self._dock_pose

    @dock_pose.setter
    def dock_pose(self, value: geometry_msgs.msg.PoseStamped) -> None:
        from geometry_msgs.msg import PoseStamped

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, PoseStamped), \
                    "The 'dock_pose' field must be a sub message of type 'PoseStamped'"

        self._dock_pose = value

    @builtins.property
    def dock_type(self) -> str:
        """Message field 'dock_type'."""
        return self._dock_type

    @dock_type.setter
    def dock_type(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'dock_type' field must be of type 'str'"

        self._dock_type = value

    @builtins.property
    def max_staging_time(self) -> float:
        """Message field 'max_staging_time'."""
        return self._max_staging_time

    @max_staging_time.setter
    def max_staging_time(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'max_staging_time' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'max_staging_time' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._max_staging_time = value

    @builtins.property
    def navigate_to_staging_pose(self) -> bool:
        """Message field 'navigate_to_staging_pose'."""
        return self._navigate_to_staging_pose

    @navigate_to_staging_pose.setter
    def navigate_to_staging_pose(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'navigate_to_staging_pose' field must be of type 'bool'"

        self._navigate_to_staging_pose = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockRobot_Result(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_Result'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_ResultConstants(typing.TypedDict):
        NONE: typing.Literal[0]
        GOAL_REJECTED: typing.Literal[1]
        SEND_GOAL_FAILURE: typing.Literal[2]
        DOCK_NOT_IN_DB: typing.Literal[901]
        DOCK_NOT_VALID: typing.Literal[902]
        FAILED_TO_STAGE: typing.Literal[903]
        FAILED_TO_DETECT_DOCK: typing.Literal[904]
        FAILED_TO_CONTROL: typing.Literal[905]
        FAILED_TO_CHARGE: typing.Literal[906]
        TIMEOUT: typing.Literal[907]
        UNKNOWN: typing.Literal[999]

    __constants: DockRobot_ResultConstants = {
        'NONE': 0,
        'GOAL_REJECTED': 1,
        'SEND_GOAL_FAILURE': 2,
        'DOCK_NOT_IN_DB': 901,
        'DOCK_NOT_VALID': 902,
        'FAILED_TO_STAGE': 903,
        'FAILED_TO_DETECT_DOCK': 904,
        'FAILED_TO_CONTROL': 905,
        'FAILED_TO_CHARGE': 906,
        'TIMEOUT': 907,
        'UNKNOWN': 999,
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
                'nav2_msgs.action.DockRobot_Result')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__result
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__result
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__result
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__result
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__result

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'NONE': metacls.__constants['NONE'],
            'GOAL_REJECTED': metacls.__constants['GOAL_REJECTED'],
            'SEND_GOAL_FAILURE': metacls.__constants['SEND_GOAL_FAILURE'],
            'DOCK_NOT_IN_DB': metacls.__constants['DOCK_NOT_IN_DB'],
            'DOCK_NOT_VALID': metacls.__constants['DOCK_NOT_VALID'],
            'FAILED_TO_STAGE': metacls.__constants['FAILED_TO_STAGE'],
            'FAILED_TO_DETECT_DOCK': metacls.__constants['FAILED_TO_DETECT_DOCK'],
            'FAILED_TO_CONTROL': metacls.__constants['FAILED_TO_CONTROL'],
            'FAILED_TO_CHARGE': metacls.__constants['FAILED_TO_CHARGE'],
            'TIMEOUT': metacls.__constants['TIMEOUT'],
            'UNKNOWN': metacls.__constants['UNKNOWN'],
            'SUCCESS__DEFAULT': True,
            'ERROR_CODE__DEFAULT': 0,
            'NUM_RETRIES__DEFAULT': 0,
        }

    @property
    def NONE(self) -> typing.Literal[0]:
        """Message constant 'NONE'."""
        return Metaclass_DockRobot_Result.__constants['NONE']

    @property
    def GOAL_REJECTED(self) -> typing.Literal[1]:
        """Message constant 'GOAL_REJECTED'."""
        return Metaclass_DockRobot_Result.__constants['GOAL_REJECTED']

    @property
    def SEND_GOAL_FAILURE(self) -> typing.Literal[2]:
        """Message constant 'SEND_GOAL_FAILURE'."""
        return Metaclass_DockRobot_Result.__constants['SEND_GOAL_FAILURE']

    @property
    def DOCK_NOT_IN_DB(self) -> typing.Literal[901]:
        """Message constant 'DOCK_NOT_IN_DB'."""
        return Metaclass_DockRobot_Result.__constants['DOCK_NOT_IN_DB']

    @property
    def DOCK_NOT_VALID(self) -> typing.Literal[902]:
        """Message constant 'DOCK_NOT_VALID'."""
        return Metaclass_DockRobot_Result.__constants['DOCK_NOT_VALID']

    @property
    def FAILED_TO_STAGE(self) -> typing.Literal[903]:
        """Message constant 'FAILED_TO_STAGE'."""
        return Metaclass_DockRobot_Result.__constants['FAILED_TO_STAGE']

    @property
    def FAILED_TO_DETECT_DOCK(self) -> typing.Literal[904]:
        """Message constant 'FAILED_TO_DETECT_DOCK'."""
        return Metaclass_DockRobot_Result.__constants['FAILED_TO_DETECT_DOCK']

    @property
    def FAILED_TO_CONTROL(self) -> typing.Literal[905]:
        """Message constant 'FAILED_TO_CONTROL'."""
        return Metaclass_DockRobot_Result.__constants['FAILED_TO_CONTROL']

    @property
    def FAILED_TO_CHARGE(self) -> typing.Literal[906]:
        """Message constant 'FAILED_TO_CHARGE'."""
        return Metaclass_DockRobot_Result.__constants['FAILED_TO_CHARGE']

    @property
    def TIMEOUT(self) -> typing.Literal[907]:
        """Message constant 'TIMEOUT'."""
        return Metaclass_DockRobot_Result.__constants['TIMEOUT']

    @property
    def UNKNOWN(self) -> typing.Literal[999]:
        """Message constant 'UNKNOWN'."""
        return Metaclass_DockRobot_Result.__constants['UNKNOWN']

    @property
    def SUCCESS__DEFAULT(cls) -> typing.Literal[True]:
        """Return default value for message field 'success'."""
        return True

    @property
    def ERROR_CODE__DEFAULT(cls) -> typing.Literal[0]:
        """Return default value for message field 'error_code'."""
        return 0

    @property
    def NUM_RETRIES__DEFAULT(cls) -> typing.Literal[0]:
        """Return default value for message field 'num_retries'."""
        return 0


class DockRobot_Result(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_Result):
    """
    Message class 'DockRobot_Result'.

    Constants:
      NONE
      GOAL_REJECTED
      SEND_GOAL_FAILURE
      DOCK_NOT_IN_DB
      DOCK_NOT_VALID
      FAILED_TO_STAGE
      FAILED_TO_DETECT_DOCK
      FAILED_TO_CONTROL
      FAILED_TO_CHARGE
      TIMEOUT
      UNKNOWN
    """

    __slots__ = [
        '_success',
        '_error_code',
        '_num_retries',
        '_error_msg',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'success': 'boolean',
        'error_code': 'uint16',
        'num_retries': 'uint16',
        'error_msg': 'string',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
    )

    def __init__(self, *,
                 success: typing.Optional[bool] = None,  # noqa: E501
                 error_code: typing.Optional[int] = None,  # noqa: E501
                 num_retries: typing.Optional[int] = None,  # noqa: E501
                 error_msg: typing.Optional[str] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.success = success if success is not None else DockRobot_Result.SUCCESS__DEFAULT
        self.error_code = error_code if error_code is not None else DockRobot_Result.ERROR_CODE__DEFAULT
        self.num_retries = num_retries if num_retries is not None else DockRobot_Result.NUM_RETRIES__DEFAULT
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
        if not isinstance(other, DockRobot_Result):
            return False
        if self.success != other.success:
            return False
        if self.error_code != other.error_code:
            return False
        if self.num_retries != other.num_retries:
            return False
        if self.error_msg != other.error_msg:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self) -> bool:
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'success' field must be of type 'bool'"

        self._success = value

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
    def num_retries(self) -> int:
        """Message field 'num_retries'."""
        return self._num_retries

    @num_retries.setter
    def num_retries(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'num_retries' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'num_retries' field must be an unsigned integer in [0, 65535]"

        self._num_retries = value

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
    import builtin_interfaces.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockRobot_Feedback(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_Feedback'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_FeedbackConstants(typing.TypedDict):
        NONE: typing.Literal[0]
        NAV_TO_STAGING_POSE: typing.Literal[1]
        INITIAL_PERCEPTION: typing.Literal[2]
        CONTROLLING: typing.Literal[3]
        WAIT_FOR_CHARGE: typing.Literal[4]
        RETRY: typing.Literal[5]

    __constants: DockRobot_FeedbackConstants = {
        'NONE': 0,
        'NAV_TO_STAGING_POSE': 1,
        'INITIAL_PERCEPTION': 2,
        'CONTROLLING': 3,
        'WAIT_FOR_CHARGE': 4,
        'RETRY': 5,
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
                'nav2_msgs.action.DockRobot_Feedback')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__feedback
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__feedback
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__feedback
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__feedback
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__feedback

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
            'NAV_TO_STAGING_POSE': metacls.__constants['NAV_TO_STAGING_POSE'],
            'INITIAL_PERCEPTION': metacls.__constants['INITIAL_PERCEPTION'],
            'CONTROLLING': metacls.__constants['CONTROLLING'],
            'WAIT_FOR_CHARGE': metacls.__constants['WAIT_FOR_CHARGE'],
            'RETRY': metacls.__constants['RETRY'],
            'NUM_RETRIES__DEFAULT': 0,
        }

    @property
    def NONE(self) -> typing.Literal[0]:
        """Message constant 'NONE'."""
        return Metaclass_DockRobot_Feedback.__constants['NONE']

    @property
    def NAV_TO_STAGING_POSE(self) -> typing.Literal[1]:
        """Message constant 'NAV_TO_STAGING_POSE'."""
        return Metaclass_DockRobot_Feedback.__constants['NAV_TO_STAGING_POSE']

    @property
    def INITIAL_PERCEPTION(self) -> typing.Literal[2]:
        """Message constant 'INITIAL_PERCEPTION'."""
        return Metaclass_DockRobot_Feedback.__constants['INITIAL_PERCEPTION']

    @property
    def CONTROLLING(self) -> typing.Literal[3]:
        """Message constant 'CONTROLLING'."""
        return Metaclass_DockRobot_Feedback.__constants['CONTROLLING']

    @property
    def WAIT_FOR_CHARGE(self) -> typing.Literal[4]:
        """Message constant 'WAIT_FOR_CHARGE'."""
        return Metaclass_DockRobot_Feedback.__constants['WAIT_FOR_CHARGE']

    @property
    def RETRY(self) -> typing.Literal[5]:
        """Message constant 'RETRY'."""
        return Metaclass_DockRobot_Feedback.__constants['RETRY']

    @property
    def NUM_RETRIES__DEFAULT(cls) -> typing.Literal[0]:
        """Return default value for message field 'num_retries'."""
        return 0


class DockRobot_Feedback(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_Feedback):
    """
    Message class 'DockRobot_Feedback'.

    Constants:
      NONE
      NAV_TO_STAGING_POSE
      INITIAL_PERCEPTION
      CONTROLLING
      WAIT_FOR_CHARGE
      RETRY
    """

    __slots__ = [
        '_state',
        '_docking_time',
        '_num_retries',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'state': 'uint16',
        'docking_time': 'builtin_interfaces/Duration',
        'num_retries': 'uint16',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Duration'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint16'),  # noqa: E501
    )

    def __init__(self, *,
                 state: typing.Optional[int] = None,  # noqa: E501
                 docking_time: typing.Optional[builtin_interfaces.msg.Duration] = None,  # noqa: E501
                 num_retries: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.state = state if state is not None else int()
        from builtin_interfaces.msg import Duration
        self.docking_time = docking_time if docking_time is not None else Duration()
        self.num_retries = num_retries if num_retries is not None else DockRobot_Feedback.NUM_RETRIES__DEFAULT

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
        if not isinstance(other, DockRobot_Feedback):
            return False
        if self.state != other.state:
            return False
        if self.docking_time != other.docking_time:
            return False
        if self.num_retries != other.num_retries:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def state(self) -> int:
        """Message field 'state'."""
        return self._state

    @state.setter
    def state(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'state' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'state' field must be an unsigned integer in [0, 65535]"

        self._state = value

    @builtins.property
    def docking_time(self) -> builtin_interfaces.msg.Duration:
        """Message field 'docking_time'."""
        return self._docking_time

    @docking_time.setter
    def docking_time(self, value: builtin_interfaces.msg.Duration) -> None:
        from builtin_interfaces.msg import Duration

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Duration), \
                    "The 'docking_time' field must be a sub message of type 'Duration'"

        self._docking_time = value

    @builtins.property
    def num_retries(self) -> int:
        """Message field 'num_retries'."""
        return self._num_retries

    @num_retries.setter
    def num_retries(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'num_retries' field must be of type 'int'"
                assert value >= 0 and value < 65536, \
                    "The 'num_retries' field must be an unsigned integer in [0, 65535]"

        self._num_retries = value


if typing.TYPE_CHECKING:
    import nav2_msgs.action._dock_robot  # noqa: E402, I100, I201, I300
    import unique_identifier_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockRobot_SendGoal_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_SendGoal_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_SendGoal_RequestConstants(typing.TypedDict):
        pass

    __constants: DockRobot_SendGoal_RequestConstants = {
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
                'nav2_msgs.action.DockRobot_SendGoal_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__send_goal__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__send_goal__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__send_goal__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__send_goal__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__send_goal__request

            from nav2_msgs.action import DockRobot
            if DockRobot.Goal._TYPE_SUPPORT is None:
                DockRobot.Goal.__import_type_support__()

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


class DockRobot_SendGoal_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_SendGoal_Request):
    """Message class 'DockRobot_SendGoal_Request'."""

    __slots__ = [
        '_goal_id',
        '_goal',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'goal': 'nav2_msgs/DockRobot_Goal',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'DockRobot_Goal'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 goal: typing.Optional[nav2_msgs.action._dock_robot.DockRobot_Goal] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._dock_robot import DockRobot_Goal
        self.goal = goal if goal is not None else DockRobot_Goal()

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
        if not isinstance(other, DockRobot_SendGoal_Request):
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
    def goal(self) -> nav2_msgs.action._dock_robot.DockRobot_Goal:
        """Message field 'goal'."""
        return self._goal

    @goal.setter
    def goal(self, value: nav2_msgs.action._dock_robot.DockRobot_Goal) -> None:
        from nav2_msgs.action._dock_robot import DockRobot_Goal

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, DockRobot_Goal), \
                    "The 'goal' field must be a sub message of type 'DockRobot_Goal'"

        self._goal = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockRobot_SendGoal_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_SendGoal_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_SendGoal_ResponseConstants(typing.TypedDict):
        pass

    __constants: DockRobot_SendGoal_ResponseConstants = {
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
                'nav2_msgs.action.DockRobot_SendGoal_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__send_goal__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__send_goal__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__send_goal__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__send_goal__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__send_goal__response

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


class DockRobot_SendGoal_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_SendGoal_Response):
    """Message class 'DockRobot_SendGoal_Response'."""

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
        if not isinstance(other, DockRobot_SendGoal_Response):
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


class Metaclass_DockRobot_SendGoal_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_SendGoal_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_SendGoal_EventConstants(typing.TypedDict):
        pass

    __constants: DockRobot_SendGoal_EventConstants = {
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
                'nav2_msgs.action.DockRobot_SendGoal_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__send_goal__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__send_goal__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__send_goal__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__send_goal__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__send_goal__event

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


class DockRobot_SendGoal_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_SendGoal_Event):
    """Message class 'DockRobot_SendGoal_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/DockRobot_SendGoal_Request, 1>',
        'response': 'sequence<nav2_msgs/DockRobot_SendGoal_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'DockRobot_SendGoal_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'DockRobot_SendGoal_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.DockRobot_SendGoal_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.DockRobot_SendGoal_Response]] = None,  # noqa: E501
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
        if not isinstance(other, DockRobot_SendGoal_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.DockRobot_SendGoal_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.DockRobot_SendGoal_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import DockRobot_SendGoal_Request

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
                     all(isinstance(v, DockRobot_SendGoal_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'DockRobot_SendGoal_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.DockRobot_SendGoal_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.DockRobot_SendGoal_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import DockRobot_SendGoal_Response

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
                     all(isinstance(v, DockRobot_SendGoal_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'DockRobot_SendGoal_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias  # noqa: I100, I300


class Metaclass_DockRobot_SendGoal(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'DockRobot_SendGoal'."""

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
                'nav2_msgs.action.DockRobot_SendGoal')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__dock_robot__send_goal

            from nav2_msgs.action import _dock_robot
            if _dock_robot.Metaclass_DockRobot_SendGoal_Request._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_SendGoal_Request.__import_type_support__()
            if _dock_robot.Metaclass_DockRobot_SendGoal_Response._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_SendGoal_Response.__import_type_support__()
            if _dock_robot.Metaclass_DockRobot_SendGoal_Event._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_SendGoal_Event.__import_type_support__()


class DockRobot_SendGoal(rosidl_pycommon.interface_base_classes.BaseService[
    DockRobot_SendGoal_Request,
    DockRobot_SendGoal_Response
], metaclass=Metaclass_DockRobot_SendGoal):
    Request: TypeAlias = DockRobot_SendGoal_Request
    Response: TypeAlias = DockRobot_SendGoal_Response
    Event: TypeAlias = DockRobot_SendGoal_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockRobot_GetResult_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_GetResult_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_GetResult_RequestConstants(typing.TypedDict):
        pass

    __constants: DockRobot_GetResult_RequestConstants = {
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
                'nav2_msgs.action.DockRobot_GetResult_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__get_result__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__get_result__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__get_result__request
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__get_result__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__get_result__request

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


class DockRobot_GetResult_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_GetResult_Request):
    """Message class 'DockRobot_GetResult_Request'."""

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
        if not isinstance(other, DockRobot_GetResult_Request):
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


class Metaclass_DockRobot_GetResult_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_GetResult_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_GetResult_ResponseConstants(typing.TypedDict):
        pass

    __constants: DockRobot_GetResult_ResponseConstants = {
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
                'nav2_msgs.action.DockRobot_GetResult_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__get_result__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__get_result__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__get_result__response
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__get_result__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__get_result__response

            from nav2_msgs.action import DockRobot
            if DockRobot.Result._TYPE_SUPPORT is None:
                DockRobot.Result.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class DockRobot_GetResult_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_GetResult_Response):
    """Message class 'DockRobot_GetResult_Response'."""

    __slots__ = [
        '_status',
        '_result',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'status': 'int8',
        'result': 'nav2_msgs/DockRobot_Result',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'DockRobot_Result'),  # noqa: E501
    )

    def __init__(self, *,
                 status: typing.Optional[int] = None,  # noqa: E501
                 result: typing.Optional[nav2_msgs.action._dock_robot.DockRobot_Result] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.status = status if status is not None else int()
        from nav2_msgs.action._dock_robot import DockRobot_Result
        self.result = result if result is not None else DockRobot_Result()

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
        if not isinstance(other, DockRobot_GetResult_Response):
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
    def result(self) -> nav2_msgs.action._dock_robot.DockRobot_Result:
        """Message field 'result'."""
        return self._result

    @result.setter
    def result(self, value: nav2_msgs.action._dock_robot.DockRobot_Result) -> None:
        from nav2_msgs.action._dock_robot import DockRobot_Result

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, DockRobot_Result), \
                    "The 'result' field must be a sub message of type 'DockRobot_Result'"

        self._result = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockRobot_GetResult_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_GetResult_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_GetResult_EventConstants(typing.TypedDict):
        pass

    __constants: DockRobot_GetResult_EventConstants = {
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
                'nav2_msgs.action.DockRobot_GetResult_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__get_result__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__get_result__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__get_result__event
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__get_result__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__get_result__event

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


class DockRobot_GetResult_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_GetResult_Event):
    """Message class 'DockRobot_GetResult_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/DockRobot_GetResult_Request, 1>',
        'response': 'sequence<nav2_msgs/DockRobot_GetResult_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'DockRobot_GetResult_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'DockRobot_GetResult_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.action.DockRobot_GetResult_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.action.DockRobot_GetResult_Response]] = None,  # noqa: E501
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
        if not isinstance(other, DockRobot_GetResult_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.DockRobot_GetResult_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.action.DockRobot_GetResult_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import DockRobot_GetResult_Request

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
                     all(isinstance(v, DockRobot_GetResult_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'DockRobot_GetResult_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.action.DockRobot_GetResult_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.action.DockRobot_GetResult_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.action import DockRobot_GetResult_Response

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
                     all(isinstance(v, DockRobot_GetResult_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'DockRobot_GetResult_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


class Metaclass_DockRobot_GetResult(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'DockRobot_GetResult'."""

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
                'nav2_msgs.action.DockRobot_GetResult')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__action__dock_robot__get_result

            from nav2_msgs.action import _dock_robot
            if _dock_robot.Metaclass_DockRobot_GetResult_Request._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_GetResult_Request.__import_type_support__()
            if _dock_robot.Metaclass_DockRobot_GetResult_Response._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_GetResult_Response.__import_type_support__()
            if _dock_robot.Metaclass_DockRobot_GetResult_Event._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_GetResult_Event.__import_type_support__()


class DockRobot_GetResult(rosidl_pycommon.interface_base_classes.BaseService[
    DockRobot_GetResult_Request,
    DockRobot_GetResult_Response
], metaclass=Metaclass_DockRobot_GetResult):
    Request: TypeAlias = DockRobot_GetResult_Request
    Response: TypeAlias = DockRobot_GetResult_Response
    Event: TypeAlias = DockRobot_GetResult_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_DockRobot_FeedbackMessage(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'DockRobot_FeedbackMessage'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class DockRobot_FeedbackMessageConstants(typing.TypedDict):
        pass

    __constants: DockRobot_FeedbackMessageConstants = {
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
                'nav2_msgs.action.DockRobot_FeedbackMessage')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__action__dock_robot__feedback_message
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__action__dock_robot__feedback_message
            cls._CONVERT_TO_PY = module.convert_to_py_msg__action__dock_robot__feedback_message
            cls._TYPE_SUPPORT = module.type_support_msg__action__dock_robot__feedback_message
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__action__dock_robot__feedback_message

            from nav2_msgs.action import DockRobot
            if DockRobot.Feedback._TYPE_SUPPORT is None:
                DockRobot.Feedback.__import_type_support__()

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


class DockRobot_FeedbackMessage(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_DockRobot_FeedbackMessage):
    """Message class 'DockRobot_FeedbackMessage'."""

    __slots__ = [
        '_goal_id',
        '_feedback',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'goal_id': 'unique_identifier_msgs/UUID',
        'feedback': 'nav2_msgs/DockRobot_Feedback',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['unique_identifier_msgs', 'msg'], 'UUID'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['nav2_msgs', 'action'], 'DockRobot_Feedback'),  # noqa: E501
    )

    def __init__(self, *,
                 goal_id: typing.Optional[unique_identifier_msgs.msg.UUID] = None,  # noqa: E501
                 feedback: typing.Optional[nav2_msgs.action._dock_robot.DockRobot_Feedback] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from unique_identifier_msgs.msg import UUID
        self.goal_id = goal_id if goal_id is not None else UUID()
        from nav2_msgs.action._dock_robot import DockRobot_Feedback
        self.feedback = feedback if feedback is not None else DockRobot_Feedback()

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
        if not isinstance(other, DockRobot_FeedbackMessage):
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
    def feedback(self) -> nav2_msgs.action._dock_robot.DockRobot_Feedback:
        """Message field 'feedback'."""
        return self._feedback

    @feedback.setter
    def feedback(self, value: nav2_msgs.action._dock_robot.DockRobot_Feedback) -> None:
        from nav2_msgs.action._dock_robot import DockRobot_Feedback

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, DockRobot_Feedback), \
                    "The 'feedback' field must be a sub message of type 'DockRobot_Feedback'"

        self._feedback = value


class Metaclass_DockRobot(rosidl_pycommon.interface_base_classes.ActionTypeSupportMeta):
    """Metaclass of action 'DockRobot'."""

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
                'nav2_msgs.action.DockRobot')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_action__action__dock_robot

            from action_msgs.msg import _goal_status_array
            if _goal_status_array.Metaclass_GoalStatusArray._TYPE_SUPPORT is None:
                _goal_status_array.Metaclass_GoalStatusArray.__import_type_support__()
            from action_msgs.srv import _cancel_goal
            if _cancel_goal.Metaclass_CancelGoal._TYPE_SUPPORT is None:
                _cancel_goal.Metaclass_CancelGoal.__import_type_support__()

            from nav2_msgs.action import _dock_robot
            if _dock_robot.Metaclass_DockRobot_SendGoal._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_SendGoal.__import_type_support__()
            if _dock_robot.Metaclass_DockRobot_GetResult._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_GetResult.__import_type_support__()
            if _dock_robot.Metaclass_DockRobot_FeedbackMessage._TYPE_SUPPORT is None:
                _dock_robot.Metaclass_DockRobot_FeedbackMessage.__import_type_support__()


class _DockRobot_Impl(rosidl_pycommon.interface_base_classes.BaseImpl[
        DockRobot_SendGoal,
        DockRobot_GetResult,
        DockRobot_FeedbackMessage
]):

    # The send_goal service using a wrapped version of the goal message as a request.
    SendGoalService: TypeAlias = DockRobot_SendGoal
    # The get_result service using a wrapped version of the result message as a response.
    GetResultService: TypeAlias = DockRobot_GetResult
    # The feedback message with generic fields which wraps the feedback message.
    FeedbackMessage: TypeAlias = DockRobot_FeedbackMessage

    # The generic service to cancel a goal.
    from action_msgs.srv._cancel_goal import CancelGoal
    CancelGoalService: TypeAlias = CancelGoal
    # The generic message for get the status of a goal.
    from action_msgs.msg._goal_status_array import GoalStatusArray
    GoalStatusMessage: TypeAlias = GoalStatusArray


class DockRobot(rosidl_pycommon.interface_base_classes.BaseAction[
    DockRobot_Goal,
    DockRobot_Result,
    DockRobot_Feedback,
    _DockRobot_Impl
], metaclass=Metaclass_DockRobot):

    # The goal message defined in the action definition.
    Goal: TypeAlias = DockRobot_Goal
    # The result message defined in the action definition.
    Result: TypeAlias = DockRobot_Result
    # The feedback message defined in the action definition.
    Feedback: TypeAlias = DockRobot_Feedback

    Impl: TypeAlias = _DockRobot_Impl

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Action classes can not be instantiated')
