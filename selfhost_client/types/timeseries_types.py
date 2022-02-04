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
    """
    v: float
    ts: str


class TimeseriesDataType(TypedDict):
    """
    Attributes:
        uuid: A unique identifier for this timeseries data
        data: A list of timeseries data points
    """
    uuid: str
    data: List[TimeseriesDataPointType]
