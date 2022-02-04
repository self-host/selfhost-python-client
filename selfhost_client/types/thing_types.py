from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class ThingType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this thing.
        name: The name of the thing.
        state: TODO
        type: TODO
        created_by: The uuid of the user who created the thing.
        tags: TODO
    """
    uuid: str
    name: str
    state: str
    type: str
    created_by: str
    tags: List[str]
