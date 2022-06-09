"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _NamespaceState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _NamespaceStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _NamespaceState.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NAMESPACE_STATE_UNSPECIFIED: _NamespaceState.ValueType  # 0
    NAMESPACE_STATE_REGISTERED: _NamespaceState.ValueType  # 1
    NAMESPACE_STATE_DEPRECATED: _NamespaceState.ValueType  # 2
    NAMESPACE_STATE_DELETED: _NamespaceState.ValueType  # 3

class NamespaceState(_NamespaceState, metaclass=_NamespaceStateEnumTypeWrapper):
    pass

NAMESPACE_STATE_UNSPECIFIED: NamespaceState.ValueType  # 0
NAMESPACE_STATE_REGISTERED: NamespaceState.ValueType  # 1
NAMESPACE_STATE_DEPRECATED: NamespaceState.ValueType  # 2
NAMESPACE_STATE_DELETED: NamespaceState.ValueType  # 3
global___NamespaceState = NamespaceState

class _ArchivalState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ArchivalStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ArchivalState.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    ARCHIVAL_STATE_UNSPECIFIED: _ArchivalState.ValueType  # 0
    ARCHIVAL_STATE_DISABLED: _ArchivalState.ValueType  # 1
    ARCHIVAL_STATE_ENABLED: _ArchivalState.ValueType  # 2

class ArchivalState(_ArchivalState, metaclass=_ArchivalStateEnumTypeWrapper):
    pass

ARCHIVAL_STATE_UNSPECIFIED: ArchivalState.ValueType  # 0
ARCHIVAL_STATE_DISABLED: ArchivalState.ValueType  # 1
ARCHIVAL_STATE_ENABLED: ArchivalState.ValueType  # 2
global___ArchivalState = ArchivalState

class _ReplicationState:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ReplicationStateEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
        _ReplicationState.ValueType
    ],
    builtins.type,
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    REPLICATION_STATE_UNSPECIFIED: _ReplicationState.ValueType  # 0
    REPLICATION_STATE_NORMAL: _ReplicationState.ValueType  # 1
    REPLICATION_STATE_HANDOVER: _ReplicationState.ValueType  # 2

class ReplicationState(_ReplicationState, metaclass=_ReplicationStateEnumTypeWrapper):
    pass

REPLICATION_STATE_UNSPECIFIED: ReplicationState.ValueType  # 0
REPLICATION_STATE_NORMAL: ReplicationState.ValueType  # 1
REPLICATION_STATE_HANDOVER: ReplicationState.ValueType  # 2
global___ReplicationState = ReplicationState
