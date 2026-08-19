# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/CostmapMetaData.idl
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


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_CostmapMetaData(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'CostmapMetaData'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class CostmapMetaDataConstants(typing.TypedDict):
        pass

    __constants: CostmapMetaDataConstants = {
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
                'nav2_msgs.msg.CostmapMetaData')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__costmap_meta_data
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__costmap_meta_data
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__costmap_meta_data
            cls._TYPE_SUPPORT = module.type_support_msg__msg__costmap_meta_data
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__costmap_meta_data

            from builtin_interfaces.msg import Time
            if Time._TYPE_SUPPORT is None:
                Time.__import_type_support__()

            from geometry_msgs.msg import Pose
            if Pose._TYPE_SUPPORT is None:
                Pose.__import_type_support__()

    @classmethod
    def __prepare__(metacls, name: str, bases: tuple[type[typing.Any], ...], /, **kwds: typing.Any) -> collections.abc.MutableMapping[str, object]:
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class CostmapMetaData(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_CostmapMetaData):
    """Message class 'CostmapMetaData'."""

    __slots__ = [
        '_map_load_time',
        '_update_time',
        '_layer',
        '_resolution',
        '_size_x',
        '_size_y',
        '_origin',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'map_load_time': 'builtin_interfaces/Time',
        'update_time': 'builtin_interfaces/Time',
        'layer': 'string',
        'resolution': 'float',
        'size_x': 'uint32',
        'size_y': 'uint32',
        'origin': 'geometry_msgs/Pose',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['builtin_interfaces', 'msg'], 'Time'),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Pose'),  # noqa: E501
    )

    def __init__(self, *,
                 map_load_time: typing.Optional[builtin_interfaces.msg.Time] = None,  # noqa: E501
                 update_time: typing.Optional[builtin_interfaces.msg.Time] = None,  # noqa: E501
                 layer: typing.Optional[str] = None,  # noqa: E501
                 resolution: typing.Optional[float] = None,  # noqa: E501
                 size_x: typing.Optional[int] = None,  # noqa: E501
                 size_y: typing.Optional[int] = None,  # noqa: E501
                 origin: typing.Optional[geometry_msgs.msg.Pose] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from builtin_interfaces.msg import Time
        self.map_load_time = map_load_time if map_load_time is not None else Time()
        from builtin_interfaces.msg import Time
        self.update_time = update_time if update_time is not None else Time()
        self.layer = layer if layer is not None else str()
        self.resolution = resolution if resolution is not None else float()
        self.size_x = size_x if size_x is not None else int()
        self.size_y = size_y if size_y is not None else int()
        from geometry_msgs.msg import Pose
        self.origin = origin if origin is not None else Pose()

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
        if not isinstance(other, CostmapMetaData):
            return False
        if self.map_load_time != other.map_load_time:
            return False
        if self.update_time != other.update_time:
            return False
        if self.layer != other.layer:
            return False
        if self.resolution != other.resolution:
            return False
        if self.size_x != other.size_x:
            return False
        if self.size_y != other.size_y:
            return False
        if self.origin != other.origin:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls) -> dict[str, str]:
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def map_load_time(self) -> builtin_interfaces.msg.Time:
        """Message field 'map_load_time'."""
        return self._map_load_time

    @map_load_time.setter
    def map_load_time(self, value: builtin_interfaces.msg.Time) -> None:
        from builtin_interfaces.msg import Time

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Time), \
                    "The 'map_load_time' field must be a sub message of type 'Time'"

        self._map_load_time = value

    @builtins.property
    def update_time(self) -> builtin_interfaces.msg.Time:
        """Message field 'update_time'."""
        return self._update_time

    @update_time.setter
    def update_time(self, value: builtin_interfaces.msg.Time) -> None:
        from builtin_interfaces.msg import Time

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Time), \
                    "The 'update_time' field must be a sub message of type 'Time'"

        self._update_time = value

    @builtins.property
    def layer(self) -> str:
        """Message field 'layer'."""
        return self._layer

    @layer.setter
    def layer(self, value: str) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, str), \
                    "The 'layer' field must be of type 'str'"

        self._layer = value

    @builtins.property
    def resolution(self) -> float:
        """Message field 'resolution'."""
        return self._resolution

    @resolution.setter
    def resolution(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'resolution' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'resolution' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._resolution = value

    @builtins.property
    def size_x(self) -> int:
        """Message field 'size_x'."""
        return self._size_x

    @size_x.setter
    def size_x(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'size_x' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'size_x' field must be an unsigned integer in [0, 4294967295]"

        self._size_x = value

    @builtins.property
    def size_y(self) -> int:
        """Message field 'size_y'."""
        return self._size_y

    @size_y.setter
    def size_y(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'size_y' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'size_y' field must be an unsigned integer in [0, 4294967295]"

        self._size_y = value

    @builtins.property
    def origin(self) -> geometry_msgs.msg.Pose:
        """Message field 'origin'."""
        return self._origin

    @origin.setter
    def origin(self, value: geometry_msgs.msg.Pose) -> None:
        from geometry_msgs.msg import Pose

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Pose), \
                    "The 'origin' field must be a sub message of type 'Pose'"

        self._origin = value
