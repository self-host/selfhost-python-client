from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class DatasetType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this dataset.
        name: TODO
        format: TODO
        checksum: TODO
        size: TODO
        thing_uuid: TODO
        created: TODO
        created_by: TODO
        updated: TODO
        updated_by: TODO
        tags: TODO
    """
    uuid: str
    name: str
    format: str
    checksum: str
    size: int
    thing_uuid: str
    created: str
    created_by: str
    updated: str
    updated_by: str
    tags: List[str]
