import json.decoder
import os
import logging
from typing import Type, Dict, Optional, Any

import requests

from .exceptions import (
    SelfHostBadRequestException,
    SelfHostUnauthorizedException,
    SelfHostForbiddenException,
    SelfHostNotFoundException,
    SelfHostConflictException,
    SelfHostTooManyRequestsException,
    SelfHostInternalServerException,
    SelfHostFatalErrorException,
    SelfHostMethodNotAllowedException
)

logger = logging.getLogger(__name__)
Response = requests.models.Response
Session = requests.sessions.Session


class BaseClient:
    """
    A base class for clients that should make requests to NODA Self-host API

    Should only be used as an abstract class.
    """

    def __init__(self,
                 base_url: str = None,
                 username: str = None,
                 password: str = None
                 ) -> None:
        """BaseClient constructor

        Sets the base url for the NODA Self-host API and authentication credentials in a new requests session.
        Will look for the following environment variables if parameters are omitted:

        SELF_HOST_BASE_URL

        SELF_HOST_USERNAME

        SELF_HOST_PASSWORD

        Args:
            base_url (Optional[str]): Base url to the NODA Self-host API.
            username (Optional[str]): Username for the NODA Self-host API.
                The domain name is the username in this case.
            password (Optional[str]): Password for the NODA Self-host API.
                The access key is the password in this case.

        Raises:
            :class:`.SelfHostFatalErrorException`: The client could not find auth credentials and a
                base url for the NODA Self-host API
        """
        self._api_version: str = 'v2'
        if base_url:
            self._base_url = base_url
        elif os.environ.get('SELF_HOST_BASE_URL'):
            self._base_url = os.environ.get('SELF_HOST_BASE_URL')
        else:
            raise SelfHostFatalErrorException('No base_url provided to client')

        self._session: Session = requests.Session()
        if username and password:
            self._session.auth = (username, password)
        elif os.environ.get('SELF_HOST_USERNAME') and os.environ.get('SELF_HOST_PASSWORD'):
            self._session.auth = (os.environ.get('SELF_HOST_USERNAME'), os.environ.get('SELF_HOST_PASSWORD'))
        else:
            raise SelfHostFatalErrorException('No credentials provided to client')

    def _process_response(self, response: Response) -> Optional[Any]:
        """Process the response from EnergyView API

        Returns:
            Will return the json encoded content if there is any content, else None will be returned.

        Args:
            response: requests.model.Response object

        Raises:
            :class:`.SelfHostBadRequestException`: Sent request had insufficient data or invalid options.
            :class:`.SelfHostUnauthorizedException`: Request was refused due to lacking authentication credentials.
            :class:`.SelfHostForbiddenException`: Server understands the request but refuses to authorize it.
            :class:`.SelfHostNotFoundException`: The requested resource was not found.
            :class:`.SelfHostMethodNotAllowedException`: The server knows the request method
                but the target resource doesn't support this method.
            :class:`.SelfHostConflictException`: The request conflicts with the current state of the target resource.
            :class:`.SelfHostTooManyRequestsException`: Sent too many requests in a given amount of time.
            :class:`.SelfHostInternalServerException`: Server encountered an unexpected condition that prevented it
                from fulfilling the request.
        """
        logger.debug(
            f'API Request sent:\n'
            f'Url: {response.request.url}\n'
            f'Body: {response.request.body}\n'
            f'Status Code: {response.status_code}'
        )
        responses: Dict[int, Type[Exception]] = {
            400: SelfHostBadRequestException,
            401: SelfHostUnauthorizedException,
            403: SelfHostForbiddenException,
            404: SelfHostNotFoundException,
            405: SelfHostMethodNotAllowedException,
            409: SelfHostConflictException,
            429: SelfHostTooManyRequestsException,
        }
        if response.status_code < 400:
            try:
                return response.json()
            except json.decoder.JSONDecodeError:
                return response.content or None
        elif 400 <= response.status_code < 500:
            raise responses[response.status_code]
        else:
            raise SelfHostInternalServerException
