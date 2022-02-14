import unittest

import responses

from selfhost_client import SelfHostClient


class TestSelfHostClient(unittest.TestCase):
    """
    This class only contains simple tests for initializing SelfHostClient.
    In-depth testing of the functionality can be found in the test files for
    the client classes that SelfHostClient inherits from.
    """
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'

    def test_credentials_from_input_params(self) -> None:
        client: SelfHostClient = SelfHostClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )
        self.assertEqual(client._base_url, self.base_url)
        self.assertEqual(client._session.auth, (self.username, self.password))

    @responses.activate
    def test_api_paths(self) -> None:
        client: SelfHostClient = SelfHostClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

        with self.subTest('Check that request url contains alerts api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._alerts_api_path}',
                json=[],
                status=200
            )
            client.get_alerts()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._alerts_api_path}'
            )

        with self.subTest('Check that request url contains datasets api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._datasets_api_path}',
                json=[],
                status=200
            )
            client.get_datasets()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._datasets_api_path}'
            )

        with self.subTest('Check that request url contains groups api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._groups_api_path}',
                json=[],
                status=200
            )
            client.get_groups()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._groups_api_path}'
            )

        with self.subTest('Check that request url contains policies api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._policies_api_path}',
                json=[],
                status=200
            )
            client.get_policies()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._policies_api_path}'
            )

        with self.subTest('Check that request url contains programs api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._programs_api_path}',
                json=[],
                status=200
            )
            client.get_programs()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._programs_api_path}'
            )

        with self.subTest('Check that request url contains things api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._things_api_path}',
                json=[],
                status=200
            )
            client.get_things()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._things_api_path}'
            )

        with self.subTest('Check that request url contains timeseries api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._timeseries_api_path}',
                json=[],
                status=200
            )
            client.get_timeseries()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._timeseries_api_path}'
            )

        with self.subTest('Check that request url contains users api path'):
            responses.add(
                responses.GET,
                url=f'{client._base_url}/{client._api_version}/{client._users_api_path}',
                json=[],
                status=200
            )
            client.get_users()
            self.assertEqual(
                responses.calls[len(responses.calls) - 1].request.url,
                f'{client._base_url}/{client._api_version}/{client._users_api_path}'
            )
