from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class CreatedAlertResponse(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for the created alert
    """
    uuid: str


class AlertType(TypedDict):
    """
    Attributes:
        uuid: TODO
        resource: TODO
        environment: TODO
        event: TODO
        severity: TODO
        status: TODO
        service: TODO
        string: TODO
        value: TODO
        description: TODO
        origin: TODO
        tags: TODO
        created: TODO
        timeout: TODO
        rawdata: TODO
        duplicate: TODO
        previous_severity: TODO
        last_receive_time: TODO
    """
    uuid: str
    resource: str
    environment: str
    event: str
    severity: str
    status: str
    service: List[str]
    string: str
    value: str
    description: str
    origin: str
    tags: List[str]
    created: str
    timeout: int
    rawdata: str
    duplicate: int
    previous_severity: str
    last_receive_time: str
