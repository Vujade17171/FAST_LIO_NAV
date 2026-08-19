# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:srv/IsPathValid.idl
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

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_IsPathValid_Request(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'IsPathValid_Request'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class IsPathValid_RequestConstants(typing.TypedDict):
        pass

    __constants: IsPathValid_RequestConstants = {
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
                'nav2_msgs.srv.IsPathValid_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__is_path_valid__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__is_path_valid__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__is_path_valid__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__is_path_valid__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__is_path_valid__request

            from nav_msgs.msg import Path
            if Path._TYPE_SUPPORT is None:
                Path.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'MAX_COST__DEFAULT': 254,
            'CONSIDER_UNKNOWN_AS_OBSTACLE__DEFAULT': False,
            'LAYER_NAME__DEFAULT': '',
            'FOOTPRINT__DEFAULT': '',
            'STOP_AT_FIRST_COLLISION__DEFAULT': True,
            'MAX_LOOKAHEAD_DISTANCE__DEFAULT': -1.0,
        }

    @property
    def MAX_COST__DEFAULT(cls) -> typing.Literal[254]:
        """Return default value for message field 'max_cost'."""
        return 254

    @property
    def CONSIDER_UNKNOWN_AS_OBSTACLE__DEFAULT(cls) -> typing.Literal[False]:
        """Return default value for message field 'consider_unknown_as_obstacle'."""
        return False

    @property
    def LAYER_NAME__DEFAULT(cls) -> typing.Literal['']:
        """Return default value for message field 'layer_name'."""
        return ''

    @property
    def FOOTPRINT__DEFAULT(cls) -> typing.Literal['']:
        """Return default value for message field 'footprint'."""
        return ''

    @property
    def STOP_AT_FIRST_COLLISION__DEFAULT(cls) -> typing.Literal[True]:
        """Return default value for message field 'stop_at_first_collision'."""
        return True

    @property
    def MAX_LOOKAHEAD_DISTANCE__DEFAULT(cls) -> float:
        """Return default value for message field 'max_lookahead_distance'."""
        return -1.0


class IsPathValid_Request(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_IsPathValid_Request):
    """Message class 'IsPathValid_Request'."""

    __slots__ = [
        '_path',
        '_max_cost',
        '_consider_unknown_as_obstacle',
        '_layer_name',
        '_footprint',
        '_stop_at_first_collision',
        '_max_lookahead_distance',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'path': 'nav_msgs/Path',
        'max_cost': 'uint8',
        'consider_unknown_as_obstacle': 'boolean',
        'layer_name': 'string',
        'footprint': 'string',
        'stop_at_first_collision': 'boolean',
        'max_lookahead_distance': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['nav_msgs', 'msg'], 'Path'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint8'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, *,
                 path: typing.Optional[nav_msgs.msg.Path] = None,  # noqa: E501
                 max_cost: typing.Optional[int] = None,  # noqa: E501
                 consider_unknown_as_obstacle: typing.Optional[bool] = None,  # noqa: E501
                 layer_name: typing.Optional[str] = None,  # noqa: E501
                 footprint: typing.Optional[str] = None,  # noqa: E501
                 stop_at_first_collision: typing.Optional[bool] = None,  # noqa: E501
                 max_lookahead_distance: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from nav_msgs.msg import Path
        self.path = path if path is not None else Path()
        self.max_cost = max_cost if max_cost is not None else IsPathValid_Request.MAX_COST__DEFAULT
        self.consider_unknown_as_obstacle = consider_unknown_as_obstacle if consider_unknown_as_obstacle is not None else IsPathValid_Request.CONSIDER_UNKNOWN_AS_OBSTACLE__DEFAULT
        self.layer_name = layer_name if layer_name is not None else IsPathValid_Request.LAYER_NAME__DEFAULT
        self.footprint = footprint if footprint is not None else IsPathValid_Request.FOOTPRINT__DEFAULT
        self.stop_at_first_collision = stop_at_first_collision if stop_at_first_collision is not None else IsPathValid_Request.STOP_AT_FIRST_COLLISION__DEFAULT
        self.max_lookahead_distance = max_lookahead_distance if max_lookahead_distance is not None else IsPathValid_Request.MAX_LOOKAHEAD_DISTANCE__DEFAULT

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
        if not isinstance(other, IsPathValid_Request):
            return False
        if self.path != other.path:
            return False
        if self.max_cost != other.max_cost:
            return False
        if self.consider_unknown_as_obstacle != other.consider_unknown_as_obstacle:
            return False
        if self.layer_name != other.layer_name:
            return False
        if self.footprint != other.footprint:
            return False
        if self.stop_at_first_collision != other.stop_at_first_collision:
            return False
        if self.max_lookahead_distance != other.max_lookahead_distance:
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
    def max_cost(self) -> int:
        """Message field 'max_cost'."""
        return self._max_cost

    @max_cost.setter
    def max_cost(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'max_cost' field must be of type 'int'"
                assert value >= 0 and value < 256, \
                    "The 'max_cost' field must be an unsigned integer in [0, 255]"

        self._max_cost = value

    @builtins.property
    def consider_unknown_as_obstacle(self) -> bool:
        """Message field 'consider_unknown_as_obstacle'."""
        return self._consider_unknown_as_obstacle

    @consider_unknown_as_obstacle.setter
    def consider_unknown_as_obstacle(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'consider_unknown_as_obstacle' field must be of type 'bool'"

        self._consider_unknown_as_obstacle = value

    @builtins.property
    def layer_name(self) -> str:
        """Message field 'layer_name'."""
        return self._layer_name

    @layer_name.setter
    def layer_name(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'layer_name' field must be of type 'str'"

        self._layer_name = value

    @builtins.property
    def footprint(self) -> str:
        """Message field 'footprint'."""
        return self._footprint

    @footprint.setter
    def footprint(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'footprint' field must be of type 'str'"

        self._footprint = value

    @builtins.property
    def stop_at_first_collision(self) -> bool:
        """Message field 'stop_at_first_collision'."""
        return self._stop_at_first_collision

    @stop_at_first_collision.setter
    def stop_at_first_collision(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'stop_at_first_collision' field must be of type 'bool'"

        self._stop_at_first_collision = value

    @builtins.property
    def max_lookahead_distance(self) -> float:
        """Message field 'max_lookahead_distance'."""
        return self._max_lookahead_distance

    @max_lookahead_distance.setter
    def max_lookahead_distance(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'max_lookahead_distance' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'max_lookahead_distance' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._max_lookahead_distance = value


# Import statements for member types

# Member 'invalid_pose_indices'
import array  # noqa: E402, I100

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_IsPathValid_Response(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'IsPathValid_Response'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class IsPathValid_ResponseConstants(typing.TypedDict):
        pass

    __constants: IsPathValid_ResponseConstants = {
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
                'nav2_msgs.srv.IsPathValid_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__is_path_valid__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__is_path_valid__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__is_path_valid__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__is_path_valid__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__is_path_valid__response

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class IsPathValid_Response(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_IsPathValid_Response):
    """Message class 'IsPathValid_Response'."""

    __slots__ = [
        '_success',
        '_is_valid',
        '_invalid_pose_indices',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'success': 'boolean',
        'is_valid': 'boolean',
        'invalid_pose_indices': 'sequence<int32>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('int32')),  # noqa: E501
    )

    def __init__(self, *,
                 success: typing.Optional[bool] = None,  # noqa: E501
                 is_valid: typing.Optional[bool] = None,  # noqa: E501
                 invalid_pose_indices: typing.Optional[collections.abc.Sequence[int]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.success = success if success is not None else bool()
        self.is_valid = is_valid if is_valid is not None else bool()
        self.invalid_pose_indices = invalid_pose_indices if invalid_pose_indices is not None else array.array('i', [])

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
        if not isinstance(other, IsPathValid_Response):
            return False
        if self.success != other.success:
            return False
        if self.is_valid != other.is_valid:
            return False
        if self.invalid_pose_indices != other.invalid_pose_indices:
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
    def is_valid(self) -> bool:
        """Message field 'is_valid'."""
        return self._is_valid

    @is_valid.setter
    def is_valid(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'is_valid' field must be of type 'bool'"

        self._is_valid = value

    @builtins.property
    def invalid_pose_indices(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'invalid_pose_indices'."""
        return self._invalid_pose_indices

    @invalid_pose_indices.setter
    def invalid_pose_indices(self, value: collections.abc.Sequence[int]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)

        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'i', \
                    "The 'invalid_pose_indices' array.array() must have the type code of 'i'"
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, int) for v in value) and
                     all(val >= -2147483648 and val < 2147483648 for val in value)), \
                    "The 'invalid_pose_indices' field must be sequence and each value of type 'int' and each integer in [-2147483648, 2147483647]"

        if isinstance(value, array.array):
            self._invalid_pose_indices = value
            return
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._invalid_pose_indices = array.array('i', value)  # type: ignore[assignment]


if typing.TYPE_CHECKING:
    import nav2_msgs.srv  # noqa: E402, I100, I201, I300
    import service_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_IsPathValid_Event(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'IsPathValid_Event'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class IsPathValid_EventConstants(typing.TypedDict):
        pass

    __constants: IsPathValid_EventConstants = {
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
                'nav2_msgs.srv.IsPathValid_Event')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__is_path_valid__event
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__is_path_valid__event
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__is_path_valid__event
            cls._TYPE_SUPPORT = module.type_support_msg__srv__is_path_valid__event
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__is_path_valid__event

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


class IsPathValid_Event(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_IsPathValid_Event):
    """Message class 'IsPathValid_Event'."""

    __slots__ = [
        '_info',
        '_request',
        '_response',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'info': 'service_msgs/ServiceEventInfo',
        'request': 'sequence<nav2_msgs/IsPathValid_Request, 1>',
        'response': 'sequence<nav2_msgs/IsPathValid_Response, 1>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['service_msgs', 'msg'], 'ServiceEventInfo'),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'srv'], 'IsPathValid_Request'), 1),  # noqa: E501
        rosidl_parser.definition.BoundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'srv'], 'IsPathValid_Response'), 1),  # noqa: E501
    )

    def __init__(self, *,
                 info: typing.Optional[service_msgs.msg.ServiceEventInfo] = None,  # noqa: E501
                 request: typing.Optional[collections.abc.Sequence[nav2_msgs.srv.IsPathValid_Request]] = None,  # noqa: E501
                 response: typing.Optional[collections.abc.Sequence[nav2_msgs.srv.IsPathValid_Response]] = None,  # noqa: E501
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
        if not isinstance(other, IsPathValid_Event):
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
    def request(self) -> typing.Annotated[typing.Any, list[nav2_msgs.srv.IsPathValid_Request]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'request'."""
        return self._request

    @request.setter
    def request(self, value: collections.abc.Sequence[nav2_msgs.srv.IsPathValid_Request]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.srv import IsPathValid_Request

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
                     all(isinstance(v, IsPathValid_Request) for v in value) and
                     True), \
                    "The 'request' field must be sequence with length <= 1 and each value of type 'IsPathValid_Request'"

        if isinstance(value, list):
            self._request = value
            return
        self._request = list(value)

    @builtins.property
    def response(self) -> typing.Annotated[typing.Any, list[nav2_msgs.srv.IsPathValid_Response]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'response'."""
        return self._response

    @response.setter
    def response(self, value: collections.abc.Sequence[nav2_msgs.srv.IsPathValid_Response]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.srv import IsPathValid_Response

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
                     all(isinstance(v, IsPathValid_Response) for v in value) and
                     True), \
                    "The 'response' field must be sequence with length <= 1 and each value of type 'IsPathValid_Response'"

        if isinstance(value, list):
            self._response = value
            return
        self._response = list(value)


if typing.TYPE_CHECKING:
    from typing_extensions import TypeAlias  # noqa: I100, I300


class Metaclass_IsPathValid(rosidl_pycommon.interface_base_classes.ServiceTypeSupportMeta):
    """Metaclass of service 'IsPathValid'."""

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
                'nav2_msgs.srv.IsPathValid')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__is_path_valid

            from nav2_msgs.srv import _is_path_valid
            if _is_path_valid.Metaclass_IsPathValid_Request._TYPE_SUPPORT is None:
                _is_path_valid.Metaclass_IsPathValid_Request.__import_type_support__()
            if _is_path_valid.Metaclass_IsPathValid_Response._TYPE_SUPPORT is None:
                _is_path_valid.Metaclass_IsPathValid_Response.__import_type_support__()
            if _is_path_valid.Metaclass_IsPathValid_Event._TYPE_SUPPORT is None:
                _is_path_valid.Metaclass_IsPathValid_Event.__import_type_support__()


class IsPathValid(rosidl_pycommon.interface_base_classes.BaseService[
    IsPathValid_Request,
    IsPathValid_Response
], metaclass=Metaclass_IsPathValid):
    Request: TypeAlias = IsPathValid_Request
    Response: TypeAlias = IsPathValid_Response
    Event: TypeAlias = IsPathValid_Event

    # Should eventually be typing.NoReturn. See mypy#14044
    def __init__(self) -> None:
        raise NotImplementedError('Service classes can not be instantiated')
