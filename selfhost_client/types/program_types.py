from typing import List

try:
    from typing import TypedDict
except ImportError:
    from typing_extensions import TypedDict


class ProgramType(TypedDict):
    """
    Attributes:
        uuid: Unique identifier of the program.
        name: The name of the program.
        type:

            -   module: Modules are used by Routines and Webhooks to extend their functionality.

            -   routine: Routines are executed at an interval.

            -   webhook: Webhooks are called using the REST API.

        state: The state of the program.

            -   active

            -   inactive

            -   failed

        schedule: A CRON schedule on the typical CRON format, yet with support for seconds.
            Ignored for Modules and Webhooks.
        deadline: An duration (in milliseconds) after which a Program (routine, webhook)
            shall terminate, to avoid long running programs. Ignored for Modules.
        language:

            -   tengo

        tags: A list of tags pinned to the program.

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
