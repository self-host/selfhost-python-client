try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class GroupType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this group.
        name: The name of the group.

    Example::

        {
            'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
            'name': 'My group',
        }

    """
    uuid: str
    name: str
