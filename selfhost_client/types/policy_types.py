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
    """
    uuid: str
    group_uuid: str
    priority: int
    effect: str
    action: str
    resource: str
