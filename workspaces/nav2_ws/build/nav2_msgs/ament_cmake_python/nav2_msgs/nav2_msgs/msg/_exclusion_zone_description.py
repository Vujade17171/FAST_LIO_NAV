# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/ExclusionZoneDescription.idl
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


class Metaclass_ExclusionZoneDescription(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'ExclusionZoneDescription'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class ExclusionZoneDescriptionConstants(typing.TypedDict):
        pass

    __constants: ExclusionZoneDescriptionConstants = {
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
                'nav2_msgs.msg.ExclusionZoneDescription')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__exclusion_zone_description
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__exclusion_zone_description
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__exclusion_zone_description
            cls._TYPE_SUPPORT = module.type_support_msg__msg__exclusion_zone_description
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__exclusion_zone_description

            from geometry_msgs.msg import Point32
            if Point32._TYPE_SUPPORT is None:
                Point32.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
            'RADIUS__DEFAULT': 0.0,
            'MIN_HEIGHT__DEFAULT': -1.7976931348623157e+308,
            'MAX_HEIGHT__DEFAULT': 1.7976931348623157e+308,
            'ENABLED__DEFAULT': True,
            'VISUALIZE__DEFAULT': False,
            'FRAME_HOLD_TIMEOUT__DEFAULT': 0.0,
        }

    @property
    def RADIUS__DEFAULT(cls) -> float:
        """Return default value for message field 'radius'."""
        return 0.0

    @property
    def MIN_HEIGHT__DEFAULT(cls) -> float:
        """Return default value for message field 'min_height'."""
        return -1.7976931348623157e+308

    @property
    def MAX_HEIGHT__DEFAULT(cls) -> float:
        """Return default value for message field 'max_height'."""
        return 1.7976931348623157e+308

    @property
    def ENABLED__DEFAULT(cls) -> typing.Literal[True]:
        """Return default value for message field 'enabled'."""
        return True

    @property
    def VISUALIZE__DEFAULT(cls) -> typing.Literal[False]:
        """Return default value for message field 'visualize'."""
        return False

    @property
    def FRAME_HOLD_TIMEOUT__DEFAULT(cls) -> float:
        """Return default value for message field 'frame_hold_timeout'."""
        return 0.0


class ExclusionZoneDescription(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_ExclusionZoneDescription):
    """Message class 'ExclusionZoneDescription'."""

    __slots__ = [
        '_zone_name',
        '_type',
        '_frame_id',
        '_points',
        '_radius',
        '_min_height',
        '_max_height',
        '_enabled',
        '_visualize',
        '_frame_hold_timeout',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'zone_name': 'string',
        'type': 'string',
        'frame_id': 'string',
        'points': 'sequence<geometry_msgs/Point32>',
        'radius': 'double',
        'min_height': 'double',
        'max_height': 'double',
        'enabled': 'boolean',
        'visualize': 'boolean',
        'frame_hold_timeout': 'double',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point32')),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, *,
                 zone_name: typing.Optional[str] = None,  # noqa: E501
                 type: typing.Optional[str] = None,  # noqa: E501, A002
                 frame_id: typing.Optional[str] = None,  # noqa: E501
                 points: typing.Optional[collections.abc.Sequence[geometry_msgs.msg.Point32]] = None,  # noqa: E501
                 radius: typing.Optional[float] = None,  # noqa: E501
                 min_height: typing.Optional[float] = None,  # noqa: E501
                 max_height: typing.Optional[float] = None,  # noqa: E501
                 enabled: typing.Optional[bool] = None,  # noqa: E501
                 visualize: typing.Optional[bool] = None,  # noqa: E501
                 frame_hold_timeout: typing.Optional[float] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        self.zone_name = zone_name if zone_name is not None else str()
        self.type = type if type is not None else str()
        self.frame_id = frame_id if frame_id is not None else str()
        self.points = points if points is not None else []
        self.radius = radius if radius is not None else ExclusionZoneDescription.RADIUS__DEFAULT
        self.min_height = min_height if min_height is not None else ExclusionZoneDescription.MIN_HEIGHT__DEFAULT
        self.max_height = max_height if max_height is not None else ExclusionZoneDescription.MAX_HEIGHT__DEFAULT
        self.enabled = enabled if enabled is not None else ExclusionZoneDescription.ENABLED__DEFAULT
        self.visualize = visualize if visualize is not None else ExclusionZoneDescription.VISUALIZE__DEFAULT
        self.frame_hold_timeout = frame_hold_timeout if frame_hold_timeout is not None else ExclusionZoneDescription.FRAME_HOLD_TIMEOUT__DEFAULT

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
        if not isinstance(other, ExclusionZoneDescription):
            return False
        if self.zone_name != other.zone_name:
            return False
        if self.type != other.type:
            return False
        if self.frame_id != other.frame_id:
            return False
        if self.points != other.points:
            return False
        if self.radius != other.radius:
            return False
        if self.min_height != other.min_height:
            return False
        if self.max_height != other.max_height:
            return False
        if self.enabled != other.enabled:
            return False
        if self.visualize != other.visualize:
            return False
        if self.frame_hold_timeout != other.frame_hold_timeout:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def zone_name(self) -> str:
        """Message field 'zone_name'."""
        return self._zone_name

    @zone_name.setter
    def zone_name(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'zone_name' field must be of type 'str'"

        self._zone_name = value

    @builtins.property  # noqa: A003
    def type(self) -> str:  # noqa: A003
        """Message field 'type'."""
        return self._type

    @type.setter  # noqa: A003
    def type(self, value: str) -> None:  # noqa: A003

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'type' field must be of type 'str'"

        self._type = value

    @builtins.property
    def frame_id(self) -> str:
        """Message field 'frame_id'."""
        return self._frame_id

    @frame_id.setter
    def frame_id(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'frame_id' field must be of type 'str'"

        self._frame_id = value

    @builtins.property
    def points(self) -> typing.Annotated[typing.Any, list[geometry_msgs.msg.Point32]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'points'."""
        return self._points

    @points.setter
    def points(self, value: collections.abc.Sequence[geometry_msgs.msg.Point32]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from geometry_msgs.msg import Point32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, Point32) for v in value) and
                     True), \
                    "The 'points' field must be sequence and each value of type 'Point32'"

        if isinstance(value, list):
            self._points = value
            return
        self._points = list(value)

    @builtins.property
    def radius(self) -> float:
        """Message field 'radius'."""
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'radius' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'radius' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._radius = value

    @builtins.property
    def min_height(self) -> float:
        """Message field 'min_height'."""
        return self._min_height

    @min_height.setter
    def min_height(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'min_height' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'min_height' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._min_height = value

    @builtins.property
    def max_height(self) -> float:
        """Message field 'max_height'."""
        return self._max_height

    @max_height.setter
    def max_height(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'max_height' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'max_height' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._max_height = value

    @builtins.property
    def enabled(self) -> bool:
        """Message field 'enabled'."""
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'enabled' field must be of type 'bool'"

        self._enabled = value

    @builtins.property
    def visualize(self) -> bool:
        """Message field 'visualize'."""
        return self._visualize

    @visualize.setter
    def visualize(self, value: bool) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, bool), \
                    "The 'visualize' field must be of type 'bool'"

        self._visualize = value

    @builtins.property
    def frame_hold_timeout(self) -> float:
        """Message field 'frame_hold_timeout'."""
        return self._frame_hold_timeout

    @frame_hold_timeout.setter
    def frame_hold_timeout(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'frame_hold_timeout' field must be of type 'float'"
                assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                    "The 'frame_hold_timeout' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"

        self._frame_hold_timeout = value
