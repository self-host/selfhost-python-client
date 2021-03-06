from typing import List, Optional
from warnings import filterwarnings

import requests
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from .base_client import BaseClient
from .types.program_types import ProgramType
from .utils import filter_none_values_from_dict

filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)
Response = requests.models.Response


class ProgramsClient(BaseClient):
    """
    A client for handling the program section of NODA Self-host API
    """

    @beartype
    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._programs_api_path = 'programs'

    @beartype
    def get_programs(self,
                     limit: Optional[int] = None,
                     offset: Optional[int] = None,
                     tags: Optional[List[str]] = None
                     ) -> List[ProgramType]:
        """Fetches programs from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[int]): The number of items to skip before starting to collect the result set.
            tags (Optional[List[str]]): List of tags to match on.

        Returns:
            List[:class:`.ProgramType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._programs_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset,
                'tags': tags
            })
        )
        return self._process_response(response)

    @beartype
    def create_program(self,
                       name: str,
                       program_type: str,
                       state: Optional[str] = None,
                       schedule: Optional[str] = None,
                       deadline: Optional[int] = None,
                       language: Optional[str] = None,
                       tags: Optional[List[str]] = None
                       ) -> ProgramType:
        """Add a new program to the NODA Self-host API

        Args:
            name (str): The name of the program
            program_type (str):

                -   module: Modules are used by Routines and Webhooks to extend their functionality.

                -   routine: Routines are executed at an interval.

                -   webhook: Webhooks are called using the REST API.

            state (Optional[str]): The state of the program.

                -   active

                -   inactive

                -   failed

            schedule (Optional[str]): A CRON schedule on the typical CRON format, yet with support for seconds.
                Ignored for Modules and Webhooks.
            deadline (Optional[int]): An duration (in milliseconds) after which a Program (routine, webhook)
                shall terminate, to avoid long running programs. Ignored for Modules.
            language (Optional[str]):

                -   tengo

            tags (Optional[List[str]]): A list of tags pinned to the program

        Returns:
            :class:`.ProgramType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._programs_api_path}',
            json=filter_none_values_from_dict({
                'name': name,
                'type': program_type,
                'state': state,
                'schedule': schedule,
                'deadline': deadline,
                'language': language,
                'tags': tags
            })
        )
        return self._process_response(response)

    @beartype
    def get_program(self, program_uuid: str) -> ProgramType:
        """Returns a program from NODA Self-host API by UUID

        Args:
            program_uuid (str): UUID of program to fetch.

        Returns:
            :class:`.ProgramType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._programs_api_path}/{program_uuid}'
        )
        return self._process_response(response)

    @beartype
    def update_program(self,
                       program_uuid: str,
                       name: Optional[str] = None,
                       program_type: Optional[str] = None,
                       state: Optional[str] = None,
                       schedule: Optional[str] = None,
                       deadline: Optional[int] = None,
                       language: Optional[str] = None,
                       tags: Optional[List[str]] = None
                       ) -> None:
        """Updates a program from NODA Self-host API

        Args:
            program_uuid (str): UUID of program to update.
            name (Optional[str]): The name of the program
            program_type (Optional[str]):

                -   module: Modules are used by Routines and Webhooks to extend their functionality.

                -   routine: Routines are executed at an interval.

                -   webhook: Webhooks are called using the REST API.

            state (Optional[str]): The state of the program.

                -   active

                -   inactive

                -   failed

            schedule (Optional[str]): A CRON schedule on the typical CRON format, yet with support for seconds.
                Ignored for Modules and Webhooks.
            deadline (Optional[int]): An duration (in milliseconds) after which a Program (routine, webhook)
                shall terminate, to avoid long running programs. Ignored for Modules.
            language (Optional[str]):

                -   tengo

            tags (Optional[List[str]]): A list of tags pinned to the program

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.put(
            url=f'{self._base_url}/{self._api_version}/{self._programs_api_path}/{program_uuid}',
            json=filter_none_values_from_dict({
                'name': name,
                'type': program_type,
                'state': state,
                'schedule': schedule,
                'deadline': deadline,
                'language': language,
                'tags': tags
            })
        )
        return self._process_response(response)

    @beartype
    def delete_program(self, program_uuid) -> None:
        """Deletes a program from NODA Self-host API

        Args:
            program_uuid (str): UUID of program to delete.

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.delete(
            url=f'{self._base_url}/{self._api_version}/{self._programs_api_path}/{program_uuid}'
        )
        return self._process_response(response)
