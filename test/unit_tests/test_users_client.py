import json
from typing import List, Dict, Union

import pyrfc3339
import responses
import unittest
import urllib

from selfhost_client import UsersClient, PolicyType, UserType, UserTokenType, CreatedUserTokenResponse
from selfhost_client.types.user_types import UserTokenResponse


class TestUsersClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: UsersClient = UsersClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_users(self) -> None:
        mock_response: List[UserType] = [
            {
                'groups': [
                    {
                        'name': 'John Doe',
                        'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
                    }
                ],
                'name': 'John Doe',
                'uuid': '5ecb8dbc-9b7f-4eae-97b2-7c286ec97d86'
            }
        ]
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, int] = {
                'limit': 20,
                'offset': 0
            }
            res: List[UserType] = self.client.get_users(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}'
                f'?{urllib.parse.urlencode(params)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))

    @responses.activate
    def test_create_user(self) -> None:
        mock_response: UserType = {
            'groups': [
                {
                    'name': 'John Doe',
                    'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
                }
            ],
            'name': 'John Doe',
            'uuid': '5ecb8dbc-9b7f-4eae-97b2-7c286ec97d86'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, str] = {
                'name': 'John Doe',
            }
            res: UserType = self.client.create_user(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_get_my_user(self) -> None:
        mock_response: UserType = {
            'groups': [
                {
                    'name': 'John Doe',
                    'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
                }
            ],
            'name': 'John Doe',
            'uuid': '5ecb8dbc-9b7f-4eae-97b2-7c286ec97d86'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/me',
                json=mock_response,
                status=200
            )

            res: UserType = self.client.get_my_user()

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/me'
            )

    @responses.activate
    def test_get_user(self) -> None:
        mock_response: UserType = {
            'groups': [
                {
                    'name': 'John Doe',
                    'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
                }
            ],
            'name': 'John Doe',
            'uuid': '5ecb8dbc-9b7f-4eae-97b2-7c286ec97d86'
        }
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}',
                json=mock_response,
                status=200
            )

            res: UserType = self.client.get_user(user_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}'
            )

    @responses.activate
    def test_update_user(self) -> None:
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}',
                status=204
            )

            params: Dict[str, Union[str, List[str]]] = {
                'name': 'John Doe',
                'groups': ['2e7823cc-44fa-403d-853f-d5ce48a002e4']
            }
            self.client.update_user(user_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_delete_user(self) -> None:
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}',
                status=204
            )

            self.client.delete_user(user_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}'
            )

    @responses.activate
    def test_get_user_policies(self) -> None:
        mock_response: List[PolicyType] = [
            {
                'action': 'read',
                'effect': 'allow',
                'group_uuid': '810d38bb-6a8e-4d36-b853-7350b67cb041',
                'priority': 10,
                'resource': 'timeseries/%',
                'uuid': '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'
            }
        ]
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/policies',
                json=mock_response,
                status=200
            )

            res: List[PolicyType] = self.client.get_user_policies(user_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/policies'
            )

    @responses.activate
    def test_update_user_rate(self) -> None:
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/rate',
                status=204
            )

            self.client.update_user_rate(user_uuid, 1000)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/rate'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), {'rate': 1000})

    @responses.activate
    def test_get_user_tokens(self) -> None:
        mock_response: List[UserTokenResponse] = [
            {
                'created': '2020-03-09T09:48:30.035+02:00',
                'name': 'My first secret token',
                'uuid': '1740f1e4-d2c6-4943-9976-9ff10eab90b2'
            }
        ]
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/tokens',
                json=mock_response,
                status=200
            )

            res: List[UserTokenType] = self.client.get_user_tokens(user_uuid)

            self.assertEqual(len(responses.calls), 1)
            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/tokens'
            )
            self.assertEqual(res[0]['uuid'], mock_response[0]['uuid'])
            self.assertEqual(res[0]['name'], mock_response[0]['name'])
            self.assertEqual(
                res[0]['created'],
                pyrfc3339.parse('2020-03-09T09:48:30.035+02:00')
            )

    @responses.activate
    def test_create_user_token(self) -> None:
        mock_response: CreatedUserTokenResponse = {
            'name': 'My new token',
            'secret': 'secret-token.Ya4bd4za6GzDaaT43dplq',
            'uuid': '1740f1e4-d2c6-4943-9976-9ff10eab90b2'
        }
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/tokens',
                json=mock_response,
                status=201
            )

            params: Dict[str, str] = {
                'token_name': 'My new token',
            }
            res: CreatedUserTokenResponse = self.client.create_user_token(user_uuid, **params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}/tokens'
            )
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['name'],
                params['token_name']
            )

    @responses.activate
    def test_delete_user_token(self) -> None:
        user_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        token_uuid: str = '9e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}'
                f'/tokens/{token_uuid}',
                status=201
            )

            self.client.delete_user_token(user_uuid, token_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._users_api_path}/{user_uuid}'
                f'/tokens/{token_uuid}'
            )
