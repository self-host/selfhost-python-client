from typing import List, Optional
from warnings import filterwarnings

import pyrfc3339
import requests
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from .base_client import BaseClient
from .types.policy_types import PolicyType
from .types.user_types import UserType, UserTokenType, CreatedUserTokenResponse, UserTokenResponse
from .utils import filter_none_values_from_dict

filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)
Response = requests.models.Response


class UsersClient(BaseClient):
    """
    A client for handling the user section of NODA Self-host API
    """

    @beartype
    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._users_api_path = 'users'

    @beartype
    def get_users(self,
                  limit: Optional[int] = None,
                  offset: Optional[int] = None
                  ) -> List[UserType]:
        """Fetches users from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[int]): The number of items to skip before starting to collect the result set.

        Returns:
            List[:class:`.UserType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset
            })
        )
        return self._process_response(response)

    @beartype
    def create_user(self, name: str) -> UserType:
        """Add a new user to the NODA Self-host API

        Args:
            name (str): The name of the user

        Returns:
            :class:`.UserType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}',
            json={'name': name}
        )
        return self._process_response(response)

    @beartype
    def get_my_user(self) -> UserType:
        """Returns the current user (you) from NODA Self-host API

        Returns:
            :class:`.UserType`

        Raises:
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/me'
        )
        return self._process_response(response)

    @beartype
    def get_user(self, user_uuid: str) -> UserType:
        """Returns a user from NODA Self-host API by UUID

        Args:
            user_uuid (str): UUID of user to fetch.

        Returns:
            :class:`.UserType`

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
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}'
        )
        return self._process_response(response)

    @beartype
    def update_user(self,
                    user_uuid: str,
                    name: Optional[str] = None,
                    groups: Optional[List[str]] = None,
                    groups_add: Optional[List[str]] = None,
                    groups_remove: Optional[List[str]] = None
                    ) -> None:
        """Updates a user from NODA Self-host API

        Either groups by itself or groups_add and/or groups_remove are required.

        Args:
            user_uuid (str): UUID of user to update.
            name (Optional[str]): Update the name of the user.
            groups (Optional[List[str]]): list of groups that should override current list of groups on user.
            groups_add (Optional[List[str]]): List of groups to add to target user.
            groups_remove (Optional[List[str]]): List of groups to remove from target user.

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostMethodNotAllowedException`: The server knows the request method
                but the target resource doesn't support this method.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.put(
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}',
            json=filter_none_values_from_dict({
                'name': name,
                'groups': groups,
                'groups_add': groups_add,
                'groups_remove': groups_remove
            })
        )
        return self._process_response(response)

    @beartype
    def delete_user(self, user_uuid: str) -> None:
        """Deletes a user from NODA Self-host API

        Args:
            user_uuid (str): UUID of user to delete.

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
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}'
        )
        return self._process_response(response)

    @beartype
    def get_user_policies(self, user_uuid: str) -> List[PolicyType]:
        """Fetches a list of policies associated with the specified user from NODA Self-host API

        Args:
            user_uuid (str): UUID of the target user.

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
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}/policies'
        )
        return self._process_response(response)

    @beartype
    def update_user_rate(self, user_uuid: str, rate: int) -> None:
        """Change the allowed request rate for a user from NODA Self-host API

        Args:
            user_uuid (str): UUID of the target user.
            rate (int): The allowed request rate of the user.

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
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}/rate',
            json={'rate': rate}
        )
        return self._process_response(response)

    @beartype
    def get_user_tokens(self, user_uuid: str) -> List[UserTokenType]:
        """Fetches a list of all secret tokens associated with a specified user from NODA Self-host API

        Args:
            user_uuid (str): UUID of the target user.

        Returns:
            List[:class:`.UserTokenType`]

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
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}/tokens'
        )
        user_tokens: List[UserTokenResponse] = self._process_response(response)
        return [{
            'uuid': token.get('uuid'),
            'name': token.get('name'),
            'created': pyrfc3339.parse(token.get('created'))
        } for token in user_tokens]

    @beartype
    def create_user_token(self, user_uuid: str, token_name: str) -> CreatedUserTokenResponse:
        """Generate and add a new secret token to a specified user from NODA Self-host API

        Args:
            user_uuid (str): UUID of the target user.
            token_name (str): Name of the secret token.

        Returns:
            :class:`.CreatedUserTokenResponse`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}/tokens',
            json={'name': token_name}
        )
        return self._process_response(response)

    @beartype
    def delete_user_token(self, user_uuid: str, token_uuid: str) -> None:
        """Delete a secret token for a specified user from NODA Self-host API

        Args:
            user_uuid (str): UUID of the target user.
            token_uuid (str): UUID of the secret token to delete.

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
            url=f'{self._base_url}/{self._api_version}/{self._users_api_path}/{user_uuid}/tokens/{token_uuid}'
        )
        return self._process_response(response)
