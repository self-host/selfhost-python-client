import datetime
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

    Example::

        {
            'uuid': '5ecb8dbc-9b7f-4eae-97b2-7c286ec97d86'
            'name': 'John Doe',
            'groups': [
                {
                    'name': 'John Doe',
                    'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
                }
            ],
        }

    """
    uuid: str
    name: str
    groups: List[GroupType]


class UserTokenType(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this token.
        name: The name of the token.
        created: The datetime (RFC 3339, section 5.6) when the token was created.

    Example::

        {
            'uuid': '1740f1e4-d2c6-4943-9976-9ff10eab90b2'
            'name': 'My token',
            'created': datetime.datetime(2020, 1, 1, 0, 15, tzinfo=<UTC+01:00>)
        }

    """
    uuid: str
    name: str
    created: datetime.datetime


class UserTokenResponse(TypedDict):
    """
    Attributes:
        uuid: The unique identifier for this token.
        name: The name of the token.
        created: Date string of when the token was created.

    Example::

        {
            'uuid': '1740f1e4-d2c6-4943-9976-9ff10eab90b2'
            'name': 'My token',
            'created': datetime.datetime(2020, 1, 1, 0, 15, tzinfo=<UTC+01:00>)
        }

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

    Example::

        {
            'uuid': '1740f1e4-d2c6-4943-9976-9ff10eab90b2'
            'name': 'My token',
            'secret': 'secret-token.Ya4bd4za6GzDaaT43dplq',
        }

    """
    uuid: str
    name: str
    secret: str
