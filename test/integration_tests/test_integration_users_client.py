import uuid
from typing import List, Dict

import unittest

from selfhost_client import SelfHostClient, UserType, PolicyType, UserTokenType, CreatedUserTokenResponse


class TestIntegrationUsersClient(unittest.TestCase):
    """
    Run these tests individually because Self-Host will return HTTP 429 Too Many Requests otherwise.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.client: SelfHostClient = SelfHostClient(
            base_url='http://127.0.0.1:8080',
            username='test',
            password='root'
        )
        cls.unique_name: str = str(uuid.uuid4())
        cls.created_user: UserType = cls.client.create_user(name=cls.unique_name)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_user(cls.created_user['uuid'])

    def test_get_users(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        users: List[UserType] = self.client.get_users(**params)
        self.assertIsNotNone(users)

    def test_create_and_delete_user(self) -> None:
        # Create and delete happens in setup and teardown methods.
        self.assertEqual(self.created_user['name'], self.unique_name)

    def test_get_my_user(self) -> None:
        my_user: UserType = self.client.get_my_user()
        self.assertEqual(my_user['uuid'], '00000000-0000-1000-8000-000000000000')

    def test_get_user(self) -> None:
        fetched_user: UserType = self.client.get_user(self.created_user['uuid'])
        self.assertEqual(fetched_user['name'], self.created_user['name'])

    def test_update_user(self) -> None:
        self.client.update_user(self.created_user['uuid'], name=f'{self.created_user["name"]} Updated')
        fetched_user = self.client.get_user(self.created_user['uuid'])
        self.assertEqual(fetched_user['name'], f'{self.created_user["name"]} Updated')

    def test_get_user_policies(self) -> None:
        policies: List[PolicyType] = self.client.get_user_policies(self.created_user['uuid'])
        self.assertIsNotNone(policies)

    def test_update_user_rate(self) -> None:
        self.client.update_user_rate(self.created_user['uuid'], 1000)

    def test_create_get_and_delete_user_token(self) -> None:
        # Create
        created_user_token: CreatedUserTokenResponse = self.client.create_user_token(
            self.created_user['uuid'],
            'My new token'
        )
        self.assertEqual(created_user_token['name'], 'My new token')

        # Get
        user_tokens: List[UserTokenType] = self.client.get_user_tokens(self.created_user['uuid'])
        self.assertIsNotNone(user_tokens)

        # Delete
        self.client.delete_user_token(self.created_user['uuid'], created_user_token['uuid'])
