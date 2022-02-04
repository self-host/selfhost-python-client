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
    """
    uuid: str
    name: str
    type: str
    state: str
    schedule: str
    deadline: int
    language: str
    tags: List[str]
