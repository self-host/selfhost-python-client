from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class ProgramType(TypedDict):
    """
    Attributes:
        uuid: TODO
        name: TODO
        type: TODO
        state: TODO
        schedule: TODO
        deadline: TODO
        language: TODO
        tags: TODO

    Example::

        {
            'uuid': '47daa6eb-bd1c-49de-9782-1e9422a206f5'
            'name': 'My program',
            'type': 'routine',
            'state': 'active',
            'schedule': '0 45 23 * * 6',
            'deadline': 500,
            'language': 'string',
            'tags': [
                'tag1',
                'tag2'
            ],
        }

    """
    uuid: str
    name: str
    type: str
    state: str
    schedule: str
    deadline: int
    language: str
    tags: List[str]
