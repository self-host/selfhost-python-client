from typing import List, Optional

import requests

from .base_client import BaseClient
from .types.alert_types import AlertType, CreatedAlertResponse
from .utils import filter_none_values_from_dict

Response = requests.models.Response


class AlertsClient(BaseClient):
    """
    A client for handling the alert section of NODA Self-host API
    """

    def __init__(self,
                 base_url: Optional[str] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None
                 ) -> None:
        super().__init__(base_url, username, password)
        self._alerts_api_path = 'alerts'

    def get_alerts(self,
                   limit: Optional[int] = None,
                   offset: Optional[int] = None,
                   resource: Optional[str] = None,
                   environment: Optional[str] = None,
                   event: Optional[str] = None,
                   origin: Optional[str] = None,
                   status: Optional[str] = None,
                   severity_le: Optional[str] = None,
                   severity_ge: Optional[str] = None,
                   severity: Optional[str] = None,
                   tags: Optional[List[str]] = None,
                   service: Optional[List[str]] = None
                   ) -> List[AlertType]:
        """Fetches alerts from NODA Self-host API

        Args:
            limit (Optional[int]): The numbers of items to return.
            offset (Optional[int]): The number of items to skip before starting to collect the result set.
            resource (Optional[str]): Alert resource
            environment (Optional[str]): Alert environment
            event (Optional[str]): Alert event
            origin (Optional[str]): Alert origin
            status (Optional[str]): Alert status

                -   open

                -   close

                -   expire

                -   shelve

                -   acknowledge

                -   unknown

            severity_le (Optional[str]): Alert severity LessOrEqual to.
                Available values : security, critical, major, minor, warning, informational, debug, trace, indeterminate
            severity_ge (Optional[str]): Alert severity GreaterOrEqual to.
                Available values : security, critical, major, minor, warning, informational, debug, trace, indeterminate
            severity (Optional[str]): The severity of the alert.

                -   security

                -   critical

                -   major

                -   minor

                -   warning

                -   informational

                -   debug

                -   trace

                -   indeterminate

            tags (Optional[List[str]]): List of tags pinned to the alert.
            service (Optional[List[str]]): Array of services to match on.

        Returns:
            List[:class:`.AlertType`]

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.get(
            url=f'{self._base_url}/{self._api_version}/{self._alerts_api_path}',
            params=filter_none_values_from_dict({
                'limit': limit,
                'offset': offset,
                'resource': resource,
                'environment': environment,
                'event': event,
                'origin': origin,
                'status': status,
                'severity_le': severity_le,
                'severity_ge': severity_ge,
                'severity': severity,
                'tags': tags,
                'service': service
            })
        )
        return self._process_response(response)

    def create_alert(self,
                     resource: str,
                     environment: str,
                     event: str,
                     value: str,
                     description: str,
                     origin: str,
                     severity: str,
                     status: Optional[str] = None,
                     service: Optional[List[str]] = None,
                     tags: Optional[List[str]] = None,
                     timeout: Optional[int] = None,
                     rawdata: Optional[str] = None
                     ) -> CreatedAlertResponse:
        """Add a new alert to the NODA Self-host API

        Args:
            resource (str): Alert resource
            environment (str): Alert environment
            event (str): Alert event
            value (str): TODO
            description (str): TODO
            origin (str): Alert origin
            severity (str): The severity of the alert.

                -   security

                -   critical

                -   major

                -   minor

                -   warning

                -   informational

                -   debug

                -   trace

                -   indeterminate

            status (Optional[str]): Alert status

                -   open

                -   close

                -   expire

                -   shelve

                -   acknowledge

                -   unknown

            service (Optional[List[str]]): TODO
            tags (Optional[List[str]]): List of tags pinned on the alert.
            timeout (Optional[int]): TODO
            rawdata (Optional[str]): Base64 encoded

        Returns:
            :class:`.CreatedAlertResponse`

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        response: Response = self._session.post(
            url=f'{self._base_url}/{self._api_version}/{self._alerts_api_path}',
            json=filter_none_values_from_dict({
                'resource': resource,
                'environment': environment,
                'event': event,
                'value': value,
                'description': description,
                'origin': origin,
                'severity': severity,
                'status': status,
                'service': service,
                'tags': tags,
                'timeout': timeout,
                'rawdata': rawdata
            })
        )
        return self._process_response(response)

    def get_alert(self, alert_uuid: str) -> AlertType:
        """Returns an alert from NODA Self-host API by UUID

        Args:
            alert_uuid (str): UUID of alert to fetch.

        Returns:
            :class:`.AlertType`

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
            url=f'{self._base_url}/{self._api_version}/{self._alerts_api_path}/{alert_uuid}'
        )
        return self._process_response(response)

    def update_alert(self,
                     alert_uuid: str,
                     resource: Optional[str] = None,
                     environment: Optional[str] = None,
                     event: Optional[str] = None,
                     value: Optional[str] = None,
                     description: Optional[str] = None,
                     origin: Optional[str] = None,
                     severity: Optional[str] = None,
                     status: Optional[str] = None,
                     service: Optional[List[str]] = None,
                     tags: Optional[List[str]] = None,
                     timeout: Optional[int] = None,
                     rawdata: Optional[str] = None
                     ) -> None:
        """Updates an alert from NODA Self-host API

        Args:
            alert_uuid (str): UUID of alert to update.
            resource (Optional[str]): Alert resource
            environment (Optional[str]): Alert environment
            event (Optional[str]): Alert event
            value (Optional[str]): TODO
            description (Optional[str]): TODO
            origin (Optional[str]): Alert origin
            severity (Optional[str]): The severity of the alert.

                -   security

                -   critical

                -   major

                -   minor

                -   warning

                -   informational

                -   debug

                -   trace

                -   indeterminate

            status (Optional[str]): Alert status

                -   open

                -   close

                -   expire

                -   shelve

                -   acknowledge

                -   unknown

            service (Optional[List[str]]): TODO
            tags (Optional[List[str]]): List of tags pinned on the alert.
            timeout (Optional[int]): TODO
            rawdata (Optional[str]): Base64 encoded

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
            url=f'{self._base_url}/{self._api_version}/{self._alerts_api_path}/{alert_uuid}',
            json=filter_none_values_from_dict({
                'resource': resource,
                'environment': environment,
                'event': event,
                'value': value,
                'description': description,
                'origin': origin,
                'severity': severity,
                'status': status,
                'service': service,
                'tags': tags,
                'timeout': timeout,
                'rawdata': rawdata
            })
        )
        return self._process_response(response)

    def delete_alert(self, alert_uuid: str) -> None:
        """Deletes an alert from NODA Self-host API

        Args:
            alert_uuid (str): UUID of alert to delete.

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
            url=f'{self._base_url}/{self._api_version}/{self._alerts_api_path}/{alert_uuid}'
        )
        return self._process_response(response)
