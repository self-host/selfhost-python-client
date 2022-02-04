from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class TimeseriesType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this timeseries.
        thing_uuid: TODO
        created_by: TODO
        name: TODO
        si_unit: TODO
        lower_bound: TODO
        upper_bound: TODO
        tags: TODO

    Example::

        {
            'uuid': 'a21ae595-15a5-4f11-8992-9d33600cc1ee'
            'thing_uuid': 'e21ae595-15a5-4f11-8992-9d33600cc1ee',
            'created_by': '1740f1e4-d2c6-4943-9976-9ff10eab90b2',
            'name': 'new timeseries',
            'si_unit': 'C',
            'lower_bound': 0,
            'upper_bound': 0,
            'tags': [
                'tag1',
                'tag2'
            ],
        }

    """
    uuid: str
    thing_uuid: str
    created_by: str
    name: str
    si_unit: str
    lower_bound: int
    upper_bound: int
    tags: List[str]


class TimeseriesDataPointType(TypedDict):
    """
    Attributes:
        v: TODO
        ts: TODO

    Example::

        {
            'v': 3.14,
            'ts': 2022-02-04T13:50:54.672Z
        }

    """
    v: float
    ts: str


class TimeseriesDataType(TypedDict):
    """
    Attributes:
        uuid: A unique identifier for this timeseries data
        data: A list of timeseries data points

    Example::

        {
            'uuid': 'e21ae595-15a5-4f11-8992-9d33600cc1ee',
            'data': [{
                'v': 3.14,
                'ts': '2022-02-04T13:50:54.672Z'
            }]
        }

    """
    uuid: str
    data: List[TimeseriesDataPointType]
