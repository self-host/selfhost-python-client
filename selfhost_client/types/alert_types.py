from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class CreatedAlertResponse(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for the created alert

    Example::

        {
            'uuid': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55'
        }

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

    Example::

        {
            'uuid': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55',
            'resource': 'string',
            'environment': 'string',
            'event': 'string',
            'severity': 'critical',
            'status': 'open',
            'service': [
                'service1',
                'service2'
            ],
            'value': 'string'
            'description': 'new alert',
            'origin': 'string',
            'tags': [
                'tag1',
                'tag2'
            ],
            'created': '2017-07-21T17:32:28+02:00',
            'timeout': 0,
            'rawdata': 'string',
            'duplicate': 0,
            'previous_severity': 'critical',
            'last_receive_time': '2017-07-21T17:32:28+02:00',
        }

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
