try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class PolicyType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this policy.
        group_uuid: TODO
        priority: TODO
        effect: TODO
        action: TODO
        resource: TODO

    Example::

        {
            'uuid': '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'
            'group_uuid': '810d38bb-6a8e-4d36-b853-7350b67cb041',
            'priority': 10,
            'effect': 'allow',
            'action': 'read',
            'resource': 'timeseries/%',
        }

    """
    uuid: str
    group_uuid: str
    priority: int
    effect: str
    action: str
    resource: str
