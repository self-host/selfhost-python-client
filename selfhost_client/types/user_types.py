from typing import List

from ..types.group_types import GroupType

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class UserType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this user.
        name: The name of the user.
        groups: The groups connected to the user.
    """
    uuid: str
    name: str
    groups: List[GroupType]


class UserTokenType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this token.
        name: The name of the token.
        created: The datetime that the token was created. In the format: YYYY-MM-DDThh:mm:ss±hh:mm.
    """
    uuid: str
    name: str
    created: str


class CreatedUserTokenResponse(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this token.
        name: The name of the token.
        secret: The secret token generated.
    """
    uuid: str
    name: str
    secret: str
