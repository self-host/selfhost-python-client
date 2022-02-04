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

    Example::

        {
            'uuid': 'd2538949-90e9-4127-8251-764a4a7426cf'
            'name': 'My Thing',
            'state': 'active',
            'type': 'office/building',
            'created_by': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55',
            'tags': [
                'tag1',
                'tag2'
            ],
        }

    """
    uuid: str
    name: str
    state: str
    type: str
    created_by: str
    tags: List[str]
