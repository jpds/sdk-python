"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import temporalio.api.common.v1.message_pb2
import temporalio.api.enums.v1.workflow_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class ApplicationFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: builtins.int
    NON_RETRYABLE_FIELD_NUMBER: builtins.int
    DETAILS_FIELD_NUMBER: builtins.int
    type: typing.Text
    non_retryable: builtins.bool
    @property
    def details(self) -> temporalio.api.common.v1.message_pb2.Payloads: ...
    def __init__(
        self,
        *,
        type: typing.Text = ...,
        non_retryable: builtins.bool = ...,
        details: typing.Optional[temporalio.api.common.v1.message_pb2.Payloads] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["details", b"details"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "details", b"details", "non_retryable", b"non_retryable", "type", b"type"
        ],
    ) -> None: ...

global___ApplicationFailureInfo = ApplicationFailureInfo

class TimeoutFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TIMEOUT_TYPE_FIELD_NUMBER: builtins.int
    LAST_HEARTBEAT_DETAILS_FIELD_NUMBER: builtins.int
    timeout_type: temporalio.api.enums.v1.workflow_pb2.TimeoutType.ValueType
    @property
    def last_heartbeat_details(
        self,
    ) -> temporalio.api.common.v1.message_pb2.Payloads: ...
    def __init__(
        self,
        *,
        timeout_type: temporalio.api.enums.v1.workflow_pb2.TimeoutType.ValueType = ...,
        last_heartbeat_details: typing.Optional[
            temporalio.api.common.v1.message_pb2.Payloads
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "last_heartbeat_details", b"last_heartbeat_details"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "last_heartbeat_details",
            b"last_heartbeat_details",
            "timeout_type",
            b"timeout_type",
        ],
    ) -> None: ...

global___TimeoutFailureInfo = TimeoutFailureInfo

class CanceledFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DETAILS_FIELD_NUMBER: builtins.int
    @property
    def details(self) -> temporalio.api.common.v1.message_pb2.Payloads: ...
    def __init__(
        self,
        *,
        details: typing.Optional[temporalio.api.common.v1.message_pb2.Payloads] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["details", b"details"]
    ) -> builtins.bool: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["details", b"details"]
    ) -> None: ...

global___CanceledFailureInfo = CanceledFailureInfo

class TerminatedFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(
        self,
    ) -> None: ...

global___TerminatedFailureInfo = TerminatedFailureInfo

class ServerFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NON_RETRYABLE_FIELD_NUMBER: builtins.int
    non_retryable: builtins.bool
    def __init__(
        self,
        *,
        non_retryable: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["non_retryable", b"non_retryable"]
    ) -> None: ...

global___ServerFailureInfo = ServerFailureInfo

class ResetWorkflowFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LAST_HEARTBEAT_DETAILS_FIELD_NUMBER: builtins.int
    @property
    def last_heartbeat_details(
        self,
    ) -> temporalio.api.common.v1.message_pb2.Payloads: ...
    def __init__(
        self,
        *,
        last_heartbeat_details: typing.Optional[
            temporalio.api.common.v1.message_pb2.Payloads
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "last_heartbeat_details", b"last_heartbeat_details"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "last_heartbeat_details", b"last_heartbeat_details"
        ],
    ) -> None: ...

global___ResetWorkflowFailureInfo = ResetWorkflowFailureInfo

class ActivityFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    SCHEDULED_EVENT_ID_FIELD_NUMBER: builtins.int
    STARTED_EVENT_ID_FIELD_NUMBER: builtins.int
    IDENTITY_FIELD_NUMBER: builtins.int
    ACTIVITY_TYPE_FIELD_NUMBER: builtins.int
    ACTIVITY_ID_FIELD_NUMBER: builtins.int
    RETRY_STATE_FIELD_NUMBER: builtins.int
    scheduled_event_id: builtins.int
    started_event_id: builtins.int
    identity: typing.Text
    @property
    def activity_type(self) -> temporalio.api.common.v1.message_pb2.ActivityType: ...
    activity_id: typing.Text
    retry_state: temporalio.api.enums.v1.workflow_pb2.RetryState.ValueType
    def __init__(
        self,
        *,
        scheduled_event_id: builtins.int = ...,
        started_event_id: builtins.int = ...,
        identity: typing.Text = ...,
        activity_type: typing.Optional[
            temporalio.api.common.v1.message_pb2.ActivityType
        ] = ...,
        activity_id: typing.Text = ...,
        retry_state: temporalio.api.enums.v1.workflow_pb2.RetryState.ValueType = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["activity_type", b"activity_type"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "activity_id",
            b"activity_id",
            "activity_type",
            b"activity_type",
            "identity",
            b"identity",
            "retry_state",
            b"retry_state",
            "scheduled_event_id",
            b"scheduled_event_id",
            "started_event_id",
            b"started_event_id",
        ],
    ) -> None: ...

global___ActivityFailureInfo = ActivityFailureInfo

class ChildWorkflowExecutionFailureInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAMESPACE_FIELD_NUMBER: builtins.int
    WORKFLOW_EXECUTION_FIELD_NUMBER: builtins.int
    WORKFLOW_TYPE_FIELD_NUMBER: builtins.int
    INITIATED_EVENT_ID_FIELD_NUMBER: builtins.int
    STARTED_EVENT_ID_FIELD_NUMBER: builtins.int
    RETRY_STATE_FIELD_NUMBER: builtins.int
    namespace: typing.Text
    @property
    def workflow_execution(
        self,
    ) -> temporalio.api.common.v1.message_pb2.WorkflowExecution: ...
    @property
    def workflow_type(self) -> temporalio.api.common.v1.message_pb2.WorkflowType: ...
    initiated_event_id: builtins.int
    started_event_id: builtins.int
    retry_state: temporalio.api.enums.v1.workflow_pb2.RetryState.ValueType
    def __init__(
        self,
        *,
        namespace: typing.Text = ...,
        workflow_execution: typing.Optional[
            temporalio.api.common.v1.message_pb2.WorkflowExecution
        ] = ...,
        workflow_type: typing.Optional[
            temporalio.api.common.v1.message_pb2.WorkflowType
        ] = ...,
        initiated_event_id: builtins.int = ...,
        started_event_id: builtins.int = ...,
        retry_state: temporalio.api.enums.v1.workflow_pb2.RetryState.ValueType = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "workflow_execution",
            b"workflow_execution",
            "workflow_type",
            b"workflow_type",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "initiated_event_id",
            b"initiated_event_id",
            "namespace",
            b"namespace",
            "retry_state",
            b"retry_state",
            "started_event_id",
            b"started_event_id",
            "workflow_execution",
            b"workflow_execution",
            "workflow_type",
            b"workflow_type",
        ],
    ) -> None: ...

global___ChildWorkflowExecutionFailureInfo = ChildWorkflowExecutionFailureInfo

class Failure(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MESSAGE_FIELD_NUMBER: builtins.int
    SOURCE_FIELD_NUMBER: builtins.int
    STACK_TRACE_FIELD_NUMBER: builtins.int
    CAUSE_FIELD_NUMBER: builtins.int
    APPLICATION_FAILURE_INFO_FIELD_NUMBER: builtins.int
    TIMEOUT_FAILURE_INFO_FIELD_NUMBER: builtins.int
    CANCELED_FAILURE_INFO_FIELD_NUMBER: builtins.int
    TERMINATED_FAILURE_INFO_FIELD_NUMBER: builtins.int
    SERVER_FAILURE_INFO_FIELD_NUMBER: builtins.int
    RESET_WORKFLOW_FAILURE_INFO_FIELD_NUMBER: builtins.int
    ACTIVITY_FAILURE_INFO_FIELD_NUMBER: builtins.int
    CHILD_WORKFLOW_EXECUTION_FAILURE_INFO_FIELD_NUMBER: builtins.int
    message: typing.Text
    source: typing.Text
    stack_trace: typing.Text
    @property
    def cause(self) -> global___Failure: ...
    @property
    def application_failure_info(self) -> global___ApplicationFailureInfo: ...
    @property
    def timeout_failure_info(self) -> global___TimeoutFailureInfo: ...
    @property
    def canceled_failure_info(self) -> global___CanceledFailureInfo: ...
    @property
    def terminated_failure_info(self) -> global___TerminatedFailureInfo: ...
    @property
    def server_failure_info(self) -> global___ServerFailureInfo: ...
    @property
    def reset_workflow_failure_info(self) -> global___ResetWorkflowFailureInfo: ...
    @property
    def activity_failure_info(self) -> global___ActivityFailureInfo: ...
    @property
    def child_workflow_execution_failure_info(
        self,
    ) -> global___ChildWorkflowExecutionFailureInfo: ...
    def __init__(
        self,
        *,
        message: typing.Text = ...,
        source: typing.Text = ...,
        stack_trace: typing.Text = ...,
        cause: typing.Optional[global___Failure] = ...,
        application_failure_info: typing.Optional[
            global___ApplicationFailureInfo
        ] = ...,
        timeout_failure_info: typing.Optional[global___TimeoutFailureInfo] = ...,
        canceled_failure_info: typing.Optional[global___CanceledFailureInfo] = ...,
        terminated_failure_info: typing.Optional[global___TerminatedFailureInfo] = ...,
        server_failure_info: typing.Optional[global___ServerFailureInfo] = ...,
        reset_workflow_failure_info: typing.Optional[
            global___ResetWorkflowFailureInfo
        ] = ...,
        activity_failure_info: typing.Optional[global___ActivityFailureInfo] = ...,
        child_workflow_execution_failure_info: typing.Optional[
            global___ChildWorkflowExecutionFailureInfo
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "activity_failure_info",
            b"activity_failure_info",
            "application_failure_info",
            b"application_failure_info",
            "canceled_failure_info",
            b"canceled_failure_info",
            "cause",
            b"cause",
            "child_workflow_execution_failure_info",
            b"child_workflow_execution_failure_info",
            "failure_info",
            b"failure_info",
            "reset_workflow_failure_info",
            b"reset_workflow_failure_info",
            "server_failure_info",
            b"server_failure_info",
            "terminated_failure_info",
            b"terminated_failure_info",
            "timeout_failure_info",
            b"timeout_failure_info",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "activity_failure_info",
            b"activity_failure_info",
            "application_failure_info",
            b"application_failure_info",
            "canceled_failure_info",
            b"canceled_failure_info",
            "cause",
            b"cause",
            "child_workflow_execution_failure_info",
            b"child_workflow_execution_failure_info",
            "failure_info",
            b"failure_info",
            "message",
            b"message",
            "reset_workflow_failure_info",
            b"reset_workflow_failure_info",
            "server_failure_info",
            b"server_failure_info",
            "source",
            b"source",
            "stack_trace",
            b"stack_trace",
            "terminated_failure_info",
            b"terminated_failure_info",
            "timeout_failure_info",
            b"timeout_failure_info",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["failure_info", b"failure_info"]
    ) -> typing.Optional[
        typing_extensions.Literal[
            "application_failure_info",
            "timeout_failure_info",
            "canceled_failure_info",
            "terminated_failure_info",
            "server_failure_info",
            "reset_workflow_failure_info",
            "activity_failure_info",
            "child_workflow_execution_failure_info",
        ]
    ]: ...

global___Failure = Failure