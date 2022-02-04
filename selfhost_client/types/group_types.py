try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class GroupType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this group.
        name: The name of the group.
    """
    uuid: str
    name: str
