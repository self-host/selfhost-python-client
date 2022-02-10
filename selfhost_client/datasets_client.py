from typing import List, Any, Optional

import requests

from .base_client import BaseClient
from .types.dataset_types import DatasetType
from .utils import filter_none_values_from_dict

Response = requests.models.Response


class DatasetsClient(BaseClient):
    """
        A client for handling the dataset section of NODA Self-host API
        """

    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._datasets_api_path = 'datasets'

    def get_datasets(self,
                     limit: Optional[int] = None,
                     offset: Optional[int] = None
                     ) -> List[DatasetType]:
        """Fetches datasets from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[int]): The number of items to skip before starting to collect the result set.

        Returns:
            List[:class:`.DatasetType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._datasets_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset
            })
        )
        return self._process_response(response)

    def create_dataset(self,
                       name: str,
                       dataset_format: str,
                       content: str,
                       thing_uuid: Optional[str] = None,
                       tags: Optional[str] = None
                       ) -> DatasetType:
        """Add a new dataset to the NODA Self-host API

        Args:
            name (str): The name of the dataset.
            dataset_format (str): File format of the data set.
            content (str): The content of the resource.
            thing_uuid (Optional[str]): A UUID reference to a Thing as a way to track data-sets to things.
            tags (Optional[List[str]]): A list of tags pinned on the dataset.

        Returns:
            :class:`.DatasetType`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._datasets_api_path}',
            json=filter_none_values_from_dict({
                'name': name,
                'format': dataset_format,
                'content': content,
                'thing_uuid': thing_uuid,
                'tags': tags
            })
        )
        return self._process_response(response)

    def get_dataset(self, dataset_uuid: str) -> DatasetType:
        """Returns a dataset from NODA Self-host API by UUID

        Args:
            dataset_uuid (str): UUID of user to fetch.

        Returns:
            :class:`.DatasetType`

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
            url=f'{self._base_url}/{self._api_version}/{self._datasets_api_path}/{dataset_uuid}'
        )
        return self._process_response(response)

    def update_dataset(self,
                       dataset_uuid: str,
                       name: Optional[str] = None,
                       dataset_format: Optional[str] = None,
                       content: Optional[str] = None,
                       thing_uuid: Optional[str] = None,
                       tags: Optional[List[str]] = None
                       ) -> None:
        """Updates a dataset from NODA Self-host API

        Args:
            dataset_uuid (str): UUID of dataset to update.
            name (Optional[str]): The name of the dataset.
            dataset_format (Optional[str]): File format of the data set.
            content (Optional[str]): The content of the resource.
            thing_uuid (Optional[str]): A UUID reference to a Thing as a way to track data-sets to things.
            tags (Optional[List[str]]): A list of tags pinned on the dataset.

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostMethodNotAllowedException`: The server knows the request method
                                          but the target resource doesn't support this method.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented
                it from fulfilling the request.
        """
        response: Response = self._session.put(
            url=f'{self._base_url}/{self._api_version}/{self._datasets_api_path}/{dataset_uuid}',
            json=filter_none_values_from_dict({
                'name': name,
                'format': dataset_format,
                'content': content,
                'thing_uuid': thing_uuid,
                'tags': tags
            })
        )
        return self._process_response(response)

    def delete_dataset(self, dataset_uuid: str) -> None:
        """Deletes a dataset from NODA Self-host API

        Args:
            dataset_uuid (str): UUID of dataset to delete.

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
            url=f'{self._base_url}/{self._api_version}/{self._datasets_api_path}/{dataset_uuid}'
        )
        return self._process_response(response)

    def get_dataset_raw_content(self, dataset_uuid: str) -> Any:
        """Returns the raw content from a dataset from NODA Self-host API by UUID

        Args:
            dataset_uuid (str): UUID of user to fetch.

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
            url=f'{self._base_url}/{self._api_version}/{self._datasets_api_path}/{dataset_uuid}/raw'
        )
        return self._process_response(response)
