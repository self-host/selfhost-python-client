import requests
from typing import List, Optional

from .base_client import BaseClient
from .types.group_types import GroupType
from .types.policy_types import PolicyType
from .utils import filter_none_values_from_dict

Response = requests.models.Response


class GroupsClient(BaseClient):
    """
    A client for handling the group section of NODA Self-host API.
    """

    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._groups_api_path = 'groups'

    def get_groups(self,
                   limit: Optional[int] = None,
                   offset: Optional[int] = None
                   ) -> List[GroupType]:
        """Fetches groups from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[int]): The number of items to skip before starting to collect the result set.

        Returns:
            List[:class:`.GroupType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._groups_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset
            })
        )
        return self._process_response(response)

    def create_group(self, name: str) -> GroupType:
        """Add a new group to the NODA Self-host API

        Args:
            name (str):The name of the group.

        Returns:
            :class:`.GroupType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._groups_api_path}',
            json={'name': name}
        )
        return self._process_response(response)

    def get_group(self, group_uuid: str) -> GroupType:
        """Fetches a specific group from NODA Self-host API by UUID

        Args:
            group_uuid (str): UUID of group to fetch.

        Returns:
            :class:`.GroupType`

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
            url=f'{self._base_url}/{self._api_version}/{self._groups_api_path}/{group_uuid}'
        )
        return self._process_response(response)

    def update_group(self, group_uuid: str, name: str) -> None:
        """Updates a group from NODA Self-host API

        Args:
            group_uuid (str): UUID of group to update.
            name (str): Update the name of the group.

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
            url=f'{self._base_url}/{self._api_version}/{self._groups_api_path}/{group_uuid}',
            json={'name': name}
        )
        return self._process_response(response)

    def delete_group(self, group_uuid: str) -> None:
        """Deletes a group from NODA Self-host API

        Args:
            group_uuid (str): UUID of group to delete.

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
            url=f'{self._base_url}/{self._api_version}/{self._groups_api_path}/{group_uuid}'
        )
        return self._process_response(response)

    def get_group_policies(self, group_uuid: str) -> List[PolicyType]:
        """Fetches a list of policies associated with the specified group from NODA Self-host API

        Args:
            group_uuid (str): UUID of the target group.

        Returns:
            List[:class:`.PolicyType`]

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
            url=f'{self._base_url}/{self._api_version}/{self._groups_api_path}/{group_uuid}/policies'
        )
        return self._process_response(response)
