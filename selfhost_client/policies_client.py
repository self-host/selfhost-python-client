from typing import List, Optional
from warnings import filterwarnings

import requests
from beartype import beartype
from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

from .base_client import BaseClient
from .types.policy_types import PolicyType
from .utils import filter_none_values_from_dict

filterwarnings("ignore", category=BeartypeDecorHintPep585DeprecationWarning)
Response = requests.models.Response


class PoliciesClient(BaseClient):
    """
    A client for handling the policy section of NODA Self-host API
    """

    @beartype
    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._policies_api_path = 'policies'

    @beartype
    def get_policies(self,
                     limit: Optional[int] = None,
                     offset: Optional[int] = None,
                     group_uuids: Optional[List[str]] = None
                     ) -> List[PolicyType]:
        """Fetches policies from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[Int]): The number of items to skip before starting to collect the result set.
            group_uuids (Optional[List[str]]): Group(s) to filter on.

        Returns:
             List[:class:`.PolicyType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._policies_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset,
                'group_uuids': group_uuids
            })
        )
        return self._process_response(response)

    @beartype
    def create_policy(self,
                      group_uuid: str,
                      priority: int,
                      effect: str,
                      action: str,
                      resource: str
                      ) -> PolicyType:
        """Add a new policy to the NODA Self-host API

        Args:
            group_uuid (str): The group to add the policy to.
            priority (int): Priority of the policy
            effect (str):

                -   allow

                -   deny

            action (str):

                -   create

                -   read

                -   update

                -   delete

            resource (str): The type of resource the policy is assigned to.

        Returns:
             :class:`.PolicyType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._policies_api_path}',
            json={
                'group_uuid': group_uuid,
                'priority': priority,
                'effect': effect,
                'action': action,
                'resource': resource
            }
        )
        return self._process_response(response)

    @beartype
    def get_policy(self, policy_uuid: str) -> PolicyType:
        """Returns a policy from NODA Self-host API by UUID

        Args:
            policy_uuid (str): UUID of policy to fetch.

        Returns:
            :class:`.PolicyType`

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
            url=f'{self._base_url}/{self._api_version}/{self._policies_api_path}/{policy_uuid}'
        )
        return self._process_response(response)

    @beartype
    def update_policy(self,
                      policy_uuid: str,
                      group_uuid: Optional[str] = None,
                      priority: Optional[int] = None,
                      effect: Optional[str] = None,
                      action: Optional[str] = None,
                      resource: Optional[str] = None
                      ) -> None:
        """Updates a policy from NODA Self-host API

        Args:
            policy_uuid (str): UUID of policy to update.
            group_uuid (Optional[str]): The group to add the policy to.
            priority (Optional[int]): Priority of the policy
            effect (Optional[str]):

                -   allow

                -   deny

            action (Optional[str]):

                -   create

                -   read

                -   update

                -   delete

            resource (Optional[str]): The type of resource the policy is assigned to.

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
            url=f'{self._base_url}/{self._api_version}/{self._policies_api_path}/{policy_uuid}',
            json=filter_none_values_from_dict({
                'group_uuid': group_uuid,
                'priority': priority,
                'effect': effect,
                'action': action,
                'resource': resource
            })
        )
        return self._process_response(response)

    @beartype
    def delete_policy(self, policy_uuid: str) -> None:
        """Deletes a policy from NODA Self-host API

        Args:
            policy_uuid (str): UUID of policy to delete.

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
            url=f'{self._base_url}/{self._api_version}/{self._policies_api_path}/{policy_uuid}'
        )
        return self._process_response(response)
