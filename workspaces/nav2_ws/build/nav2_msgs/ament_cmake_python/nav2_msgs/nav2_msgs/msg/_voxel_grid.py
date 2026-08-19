# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/VoxelGrid.idl
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
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

# Member 'data'
import array  # noqa: E402, I100

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_VoxelGrid(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'VoxelGrid'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class VoxelGridConstants(typing.TypedDict):
        pass

    __constants: VoxelGridConstants = {
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
                'nav2_msgs.msg.VoxelGrid')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__voxel_grid
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__voxel_grid
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__voxel_grid
            cls._TYPE_SUPPORT = module.type_support_msg__msg__voxel_grid
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__voxel_grid

            from geometry_msgs.msg import Point32
            if Point32._TYPE_SUPPORT is None:
                Point32.__import_type_support__()

            from geometry_msgs.msg import Vector3
            if Vector3._TYPE_SUPPORT is None:
                Vector3.__import_type_support__()

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


class VoxelGrid(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_VoxelGrid):
    """Message class 'VoxelGrid'."""

    __slots__ = [
        '_header',
        '_data',
        '_origin',
        '_resolutions',
        '_size_x',
        '_size_y',
        '_size_z',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'data': 'sequence<uint32>',
        'origin': 'geometry_msgs/Point32',
        'resolutions': 'geometry_msgs/Vector3',
        'size_x': 'uint32',
        'size_y': 'uint32',
        'size_z': 'uint32',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.BasicType('uint32')),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Point32'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['geometry_msgs', 'msg'], 'Vector3'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
        rosidl_parser.definition.BasicType('uint32'),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 data: typing.Optional[collections.abc.Sequence[int]] = None,  # noqa: E501
                 origin: typing.Optional[geometry_msgs.msg.Point32] = None,  # noqa: E501
                 resolutions: typing.Optional[geometry_msgs.msg.Vector3] = None,  # noqa: E501
                 size_x: typing.Optional[int] = None,  # noqa: E501
                 size_y: typing.Optional[int] = None,  # noqa: E501
                 size_z: typing.Optional[int] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.data = data if data is not None else array.array('I', [])
        from geometry_msgs.msg import Point32
        self.origin = origin if origin is not None else Point32()
        from geometry_msgs.msg import Vector3
        self.resolutions = resolutions if resolutions is not None else Vector3()
        self.size_x = size_x if size_x is not None else int()
        self.size_y = size_y if size_y is not None else int()
        self.size_z = size_z if size_z is not None else int()

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
        if not isinstance(other, VoxelGrid):
            return False
        if self.header != other.header:
            return False
        if self.data != other.data:
            return False
        if self.origin != other.origin:
            return False
        if self.resolutions != other.resolutions:
            return False
        if self.size_x != other.size_x:
            return False
        if self.size_y != other.size_y:
            return False
        if self.size_z != other.size_z:
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
    def data(self) -> typing.Annotated[typing.Any, array.array[int]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'data'."""
        return self._data

    @data.setter
    def data(self, value: collections.abc.Sequence[int]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)

        if self._check_fields:
            if isinstance(value, array.array):
                assert value.typecode == 'I', \
                    "The 'data' array.array() must have the type code of 'I'"
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, int) for v in value) and
                     all(val >= 0 and val < 4294967296 for val in value)), \
                    "The 'data' field must be sequence and each value of type 'int' and each unsigned integer in [0, 4294967295]"

        if isinstance(value, array.array):
            self._data = value
            return
        # type ignore below fixed in mypy 1.17+ see mypy#19421
        self._data = array.array('I', value)  # type: ignore[assignment]

    @builtins.property
    def origin(self) -> geometry_msgs.msg.Point32:
        """Message field 'origin'."""
        return self._origin

    @origin.setter
    def origin(self, value: geometry_msgs.msg.Point32) -> None:
        from geometry_msgs.msg import Point32

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Point32), \
                    "The 'origin' field must be a sub message of type 'Point32'"

        self._origin = value

    @builtins.property
    def resolutions(self) -> geometry_msgs.msg.Vector3:
        """Message field 'resolutions'."""
        return self._resolutions

    @resolutions.setter
    def resolutions(self, value: geometry_msgs.msg.Vector3) -> None:
        from geometry_msgs.msg import Vector3

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, Vector3), \
                    "The 'resolutions' field must be a sub message of type 'Vector3'"

        self._resolutions = value

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
    def size_z(self) -> int:
        """Message field 'size_z'."""
        return self._size_z

    @size_z.setter
    def size_z(self, value: int) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, int), \
                    "The 'size_z' field must be of type 'int'"
                assert value >= 0 and value < 4294967296, \
                    "The 'size_z' field must be an unsigned integer in [0, 4294967295]"

        self._size_z = value
