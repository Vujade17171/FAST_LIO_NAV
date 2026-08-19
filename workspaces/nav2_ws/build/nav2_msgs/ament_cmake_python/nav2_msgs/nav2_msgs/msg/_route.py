# generated from rosidl_generator_py/resource/_idl.py.em
# with input from nav2_msgs:msg/Route.idl
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
    import nav2_msgs.msg  # noqa: E402, I100, I201, I300
    import std_msgs.msg  # noqa: E402, I100, I201, I300


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Route(rosidl_pycommon.interface_base_classes.MessageTypeSupportMeta):
    """Metaclass of message 'Route'."""

    _CREATE_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_FROM_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _CONVERT_TO_PY: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _DESTROY_ROS_MESSAGE: typing.ClassVar[typing.Optional[PyCapsule]] = None
    _TYPE_SUPPORT: typing.ClassVar[typing.Optional[PyCapsule]] = None

    class RouteConstants(typing.TypedDict):
        pass

    __constants: RouteConstants = {
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
                'nav2_msgs.msg.Route')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__route
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__route
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__route
            cls._TYPE_SUPPORT = module.type_support_msg__msg__route
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__route

            from nav2_msgs.msg import RouteEdge
            if RouteEdge._TYPE_SUPPORT is None:
                RouteEdge.__import_type_support__()

            from nav2_msgs.msg import RouteNode
            if RouteNode._TYPE_SUPPORT is None:
                RouteNode.__import_type_support__()

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


class Route(rosidl_pycommon.interface_base_classes.BaseMessage, metaclass=Metaclass_Route):
    """Message class 'Route'."""

    __slots__ = [
        '_header',
        '_route_cost',
        '_nodes',
        '_edges',
        '_check_fields',
    ]

    _fields_and_field_types: dict[str, str] = {
        'header': 'std_msgs/Header',
        'route_cost': 'float',
        'nodes': 'sequence<nav2_msgs/RouteNode>',
        'edges': 'sequence<nav2_msgs/RouteEdge>',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES: tuple[rosidl_parser.definition.AbstractType, ...] = (
        rosidl_parser.definition.NamespacedType(['std_msgs', 'msg'], 'Header'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'msg'], 'RouteNode')),  # noqa: E501
        rosidl_parser.definition.UnboundedSequence(rosidl_parser.definition.NamespacedType(['nav2_msgs', 'msg'], 'RouteEdge')),  # noqa: E501
    )

    def __init__(self, *,
                 header: typing.Optional[std_msgs.msg.Header] = None,  # noqa: E501
                 route_cost: typing.Optional[float] = None,  # noqa: E501
                 nodes: typing.Optional[collections.abc.Sequence[nav2_msgs.msg.RouteNode]] = None,  # noqa: E501
                 edges: typing.Optional[collections.abc.Sequence[nav2_msgs.msg.RouteEdge]] = None,  # noqa: E501
                 check_fields: typing.Optional[bool] = None) -> None:
        if check_fields is not None:
            self._check_fields = check_fields
        else:
            self._check_fields = ros_python_check_fields == '1'
        from std_msgs.msg import Header
        self.header = header if header is not None else Header()
        self.route_cost = route_cost if route_cost is not None else float()
        self.nodes = nodes if nodes is not None else []
        self.edges = edges if edges is not None else []

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
        if not isinstance(other, Route):
            return False
        if self.header != other.header:
            return False
        if self.route_cost != other.route_cost:
            return False
        if self.nodes != other.nodes:
            return False
        if self.edges != other.edges:
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
    def route_cost(self) -> float:
        """Message field 'route_cost'."""
        return self._route_cost

    @route_cost.setter
    def route_cost(self, value: float) -> None:

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    isinstance(value, float), \
                    "The 'route_cost' field must be of type 'float'"
                assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                    "The 'route_cost' field must be a float in [-3.402823466e+38, 3.402823466e+38]"

        self._route_cost = value

    @builtins.property
    def nodes(self) -> typing.Annotated[typing.Any, list[nav2_msgs.msg.RouteNode]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'nodes'."""
        return self._nodes

    @nodes.setter
    def nodes(self, value: collections.abc.Sequence[nav2_msgs.msg.RouteNode]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.msg import RouteNode

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, RouteNode) for v in value) and
                     True), \
                    "The 'nodes' field must be sequence and each value of type 'RouteNode'"

        if isinstance(value, list):
            self._nodes = value
            return
        self._nodes = list(value)

    @builtins.property
    def edges(self) -> typing.Annotated[typing.Any, list[nav2_msgs.msg.RouteEdge]]:   # typing.Annotated can be remove after mypy 1.16+ see mypy#3004
        """Message field 'edges'."""
        return self._edges

    @edges.setter
    def edges(self, value: collections.abc.Sequence[nav2_msgs.msg.RouteEdge]) -> None:
        if isinstance(value, collections.abc.Set):
            import warnings
            warnings.warn(
                'Using set or subclass of set is deprecated,'
                ' please use a subclass of collections.abc.Sequence like list',
                DeprecationWarning)
        from nav2_msgs.msg import RouteEdge

        if self._check_fields:
            if False:  # Done for templating alignment
                pass
            else:
                assert \
                    ((isinstance(value, collections.abc.Sequence) or
                     isinstance(value, collections.abc.Set)) and
                     not isinstance(value, str) and
                     not isinstance(value, collections.UserString) and
                     all(isinstance(v, RouteEdge) for v in value) and
                     True), \
                    "The 'edges' field must be sequence and each value of type 'RouteEdge'"

        if isinstance(value, list):
            self._edges = value
            return
        self._edges = list(value)
