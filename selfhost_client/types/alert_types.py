import datetime
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
        uuid: Unique identifier for the alert.
        resource: Alert resource
        environment: Alert environment
        event: Alert event
        severity: The severity of the alert.

            -   security

            -   critical

            -   major

            -   minor

            -   warning

            -   informational

            -   debug

            -   trace

            -   indeterminate

        status:

            -   open

            -   close

            -   expire

            -   shelve

            -   acknowledge

            -   unknown

        service: TODO
        value: TODO
        description: TODO
        origin: Alert origin
        tags: List of tags pinned to the alert.
        created: Date-time when created, as defined by RFC 3339, section 5.6.
        timeout: TODO
        rawdata: Base64 encoded
        duplicate: TODO
        previous_severity:

            -   security

            -   critical

            -   major

            -   minor

            -   warning

            -   informational

            -   debug

            -   trace

            -   indeterminate

        last_receive_time: Datetime, as defined by RFC 3339, section 5.6.

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
            'created': datetime.datetime(2020, 1, 1, 0, 15, tzinfo=<UTC+01:00>)
            'timeout': 0,
            'rawdata': 'string',
            'duplicate': 0,
            'previous_severity': 'critical',
            'last_receive_time': datetime.datetime(2020, 1, 1, 0, 15, tzinfo=<UTC+01:00>)
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
    created: datetime.datetime
    timeout: int
    rawdata: str
    duplicate: int
    previous_severity: str
    last_receive_time: datetime.datetime


class AlertResponse(TypedDict):
    """
    Attributes:
        uuid: Unique identifier for the alert.
        resource: Alert resource
        environment: Alert environment
        event: Alert event
        severity: The severity of the alert.

            -   security

            -   critical

            -   major

            -   minor

            -   warning

            -   informational

            -   debug

            -   trace

            -   indeterminate

        status:

            -   open

            -   close

            -   expire

            -   shelve

            -   acknowledge

            -   unknown

        service: TODO
        value: TODO
        description: TODO
        origin: Alert origin
        tags: List of tags pinned to the alert.
        created: Date string when created, as defined by RFC 3339, section 5.6.
        timeout: TODO
        rawdata: Base64 encoded
        duplicate: TODO
        previous_severity:

            -   security

            -   critical

            -   major

            -   minor

            -   warning

            -   informational

            -   debug

            -   trace

            -   indeterminate

        last_receive_time: Date string, as defined by RFC 3339, section 5.6.

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
