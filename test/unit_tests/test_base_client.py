import base64
import os
import unittest

import requests
import responses
from selfhost_client import (
    BaseClient,
    SelfHostBadRequestException,
    SelfHostConflictException,
    SelfHostFatalErrorException,
    SelfHostForbiddenException,
    SelfHostInternalServerException,
    SelfHostMethodNotAllowedException,
    SelfHostNotFoundException,
    SelfHostTooManyRequestsException,
    SelfHostUnauthorizedException,
)

Response = requests.models.Response


class TestBaseClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = "http://example.com"
        self.username: str = "test"
        self.password: str = "test"

    def test_credentials_from_input_params(self) -> None:
        client: BaseClient = BaseClient(
            base_url=self.base_url, username=self.username, password=self.password
        )
        self.assertEqual(client._base_url, self.base_url)
        self.assertEqual(client._session.auth, (self.username, self.password))

    @unittest.mock.patch.dict(
        os.environ,
        {
            "SELF_HOST_BASE_URL": "http://example.com",
            "SELF_HOST_USERNAME": "test",
            "SELF_HOST_PASSWORD": "test",
        },
    )
    def test_credentials_from_env_vars(self) -> None:
        client: BaseClient = BaseClient()
        self.assertEqual(client._base_url, "http://example.com")
        self.assertEqual(client._session.auth, ("test", "test"))

    @unittest.mock.patch.dict(
        os.environ, {"SELF_HOST_USERNAME": "test", "SELF_HOST_PASSWORD": "test"}
    )
    def test_credentials_from_env_vars_no_base_url(self) -> None:
        self.assertRaises(SelfHostFatalErrorException, BaseClient)

    @unittest.mock.patch.dict(
        os.environ,
        {
            "SELF_HOST_BASE_URL": "http://example.com",
        },
    )
    def test_credentials_from_env_vars_no_credentials(self) -> None:
        self.assertRaises(SelfHostFatalErrorException, BaseClient)

    @responses.activate
    def test_request_auth_header_is_set(self) -> None:
        """
        Makes a mocked request and makes sure that the Authorization header is set correctly by manually calculating
        the header and comparing to the sent request header.
        """
        client: BaseClient = BaseClient(
            base_url=self.base_url, username=self.username, password=self.password
        )

        responses.add(responses.GET, url=self.base_url, json={}, status=200)
        client._session.get(self.base_url)

        auth_header: str = f"{self.username}:{self.password}"
        auth_header_bytes: bytes = auth_header.encode("ascii")
        auth_header_base64_bytes: bytes = base64.b64encode(auth_header_bytes)
        base64_auth_header: str = auth_header_base64_bytes.decode("ascii")

        self.assertEqual(
            responses.calls[0].request.headers.get("Authorization"),
            f"Basic {base64_auth_header}",
        )

    @responses.activate
    def test_process_response(self) -> None:
        client: BaseClient = BaseClient(
            base_url=self.base_url, username=self.username, password=self.password
        )

        with self.subTest("OK status code and returns valid json"):
            responses.add(
                responses.GET,
                url=self.base_url,
                json={},
                status=200,
            )
            response = requests.get(self.base_url)
            self.assertEqual(client._process_response(response), {})

        with self.subTest("OK status code and returns None"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=200,
            )
            response = requests.get(self.base_url)
            self.assertIsNone(client._process_response(response))

        with self.subTest("OK status code and returns content in bytes"):
            responses.add(
                responses.GET,
                url=client._base_url,
                body="not json, but valid body",
                status=200,
            )
            response: Response = requests.get(client._base_url)
            self.assertEqual(
                client._process_response(response).decode("utf-8"),
                "not json, but valid body",
            )

        with self.subTest("Created status code and returns None"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=201,
            )
            response = requests.get(self.base_url)
            self.assertIsNone(client._process_response(response))

        with self.subTest("Should raise SelfHostBadRequestException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=400,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostBadRequestException, client._process_response, response
            )

        with self.subTest("Should raise SelfHostUnauthorizedException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=401,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostUnauthorizedException, client._process_response, response
            )

        with self.subTest("Should raise SelfHostForbiddenException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=403,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostForbiddenException, client._process_response, response
            )

        with self.subTest("Should raise SelfHostNotFoundException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=404,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostNotFoundException, client._process_response, response
            )

        with self.subTest("Should raise SelfHostMethodNotAllowedException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=405,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostMethodNotAllowedException, client._process_response, response
            )

        with self.subTest("Should raise SelfHostConflictException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=409,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostConflictException, client._process_response, response
            )

        with self.subTest("Should raise SelfHostTooManyRequestsException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=429,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostTooManyRequestsException, client._process_response, response
            )

        with self.subTest("Should raise SelfHostInternalServerException"):
            responses.add(
                responses.GET,
                url=self.base_url,
                status=500,
            )
            response: Response = requests.get(self.base_url)
            self.assertRaises(
                SelfHostInternalServerException, client._process_response, response
            )

        with self.subTest("request is logged successfully"):
            responses.add(
                responses.GET,
                url=self.base_url,
                body="Example body",
                status=200,
            )

            with self.assertLogs("selfhost_client", level="DEBUG") as cm:
                response: Response = requests.get(self.base_url)
                client._process_response(response)
                self.assertEqual(
                    cm.output[0],
                    (
                        "DEBUG:selfhost_client.base_client:"
                        "API Request sent:\n"
                        f"Url: {response.request.url}\n"
                        f"Body: {response.request.body}\n"
                        f"Status Code: {response.status_code}"
                    ),
                )
