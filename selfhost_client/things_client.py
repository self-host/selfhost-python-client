from typing import List, Optional
from warnings import filterwarnings

import requests
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from .base_client import BaseClient
from .types.dataset_types import DatasetType
from .types.thing_types import ThingType
from .types.timeseries_types import TimeseriesType
from .utils import filter_none_values_from_dict

filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)
Response = requests.models.Response


class ThingsClient(BaseClient):
    """
    A client for handling the things section of NODA Self-host API
    """

    @beartype
    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._things_api_path = 'things'

    @beartype
    def get_things(self,
                   limit: Optional[int] = None,
                   offset: Optional[int] = None,
                   tags: Optional[List[str]] = None
                   ) -> List[ThingType]:
        """Fetches things from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[int]): The number of items to skip before starting to collect the result set.
            tags (Optional[List[str]]): List of tags to match on.

        Returns:
            List[:class:`.ThingType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._things_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset,
                'tags': tags
            })
        )
        return self._process_response(response)

    @beartype
    def create_thing(self,
                     name: str,
                     thing_type: Optional[str] = None,
                     tags: Optional[List[str]] = None
                     ) -> ThingType:
        """Add a new thing to the NODA Self-host API

        Args:
            name (str): The name of the thing
            thing_type (Optional[str]): Type of the thing
            tags (Optional[List[str]]): Tags pinned on the thing

        Returns:
            :class:`.ThingType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._things_api_path}',
            json=filter_none_values_from_dict({
                'name': name,
                'type': thing_type,
                'tags': tags
            })
        )
        return self._process_response(response)

    @beartype
    def get_thing(self, thing_uuid: str) -> ThingType:
        """Returns a thing from NODA Self-host API by UUID

        Args:
            thing_uuid (str): UUID of thing to fetch.

        Returns:
            :class:`.ThingType`

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
            url=f'{self._base_url}/{self._api_version}/{self._things_api_path}/{thing_uuid}'
        )
        return self._process_response(response)

    @beartype
    def update_thing(self,
                     thing_uuid: str,
                     name: Optional[str] = None,
                     state: Optional[str] = None,
                     thing_type: Optional[str] = None,
                     tags: Optional[List[str]] = None
                     ) -> None:
        """Updates a thing from NODA Self-host API

        Args:
            thing_uuid (str): UUID of thing to update.
            name (Optional[str]): The name of the thing
            state (Optional[str]): The state of the thing.

                -   active

                -   inactive

                -   passive

                -   archived

            thing_type (Optional[str]): Thing type declaration
            tags (Optional[List[str]]): Tags pinned on the thing

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
            url=f'{self._base_url}/{self._api_version}/{self._things_api_path}/{thing_uuid}',
            json=filter_none_values_from_dict({
                'name': name,
                'state': state,
                'type': thing_type,
                'tags': tags
            })
        )
        return self._process_response(response)

    @beartype
    def delete_thing(self, thing_uuid: str) -> None:
        """Deletes a thing from NODA Self-host API

        Args:
            thing_uuid (str): UUID of thing to delete.

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
            url=f'{self._base_url}/{self._api_version}/{self._things_api_path}/{thing_uuid}'
        )
        return self._process_response(response)

    @beartype
    def get_thing_datasets(self, thing_uuid: str) -> List[DatasetType]:
        """Returns a list of datasets associated with the specified thing from NODA Self-host API

        Args:
            thing_uuid (str): UUID of the target user.

        Returns:
            List[:class:`.DatasetType`]

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
            url=f'{self._base_url}/{self._api_version}/{self._things_api_path}/{thing_uuid}/datasets'
        )
        return self._process_response(response)

    @beartype
    def get_thing_timeseries(self, thing_uuid: str) -> List[TimeseriesType]:
        """Returns a list of timeseries associated with the specified thing from NODA Self-host API

        Args:
            thing_uuid (str): UUID of the target user.

        Returns:
            List[:class:`.TimeseriesType`]

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
            url=f'{self._base_url}/{self._api_version}/{self._things_api_path}/{thing_uuid}/timeseries'
        )
        return self._process_response(response)
