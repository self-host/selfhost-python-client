import uuid
from typing import List, Dict

import unittest

from selfhost_client import SelfHostClient, GroupType, PolicyType


class TestIntegrationGroupsClient(unittest.TestCase):
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
        cls.created_group: GroupType = cls.client.create_group(name=cls.unique_name)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_group(cls.created_group['uuid'])

    def test_get_groups(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        groups: List[GroupType] = self.client.get_groups(**params)
        self.assertIsNotNone(groups)

    def test_create_and_delete_group(self) -> None:
        # Create and delete happens in setup and teardown methods.
        self.assertEqual(self.created_group['name'], self.unique_name)

    def test_get_group(self) -> None:
        fetched_group: GroupType = self.client.get_group(self.created_group['uuid'])
        self.assertEqual(fetched_group['name'], self.created_group['name'])

    def test_update_group(self) -> None:
        self.client.update_group(self.created_group['uuid'], name=f'{self.created_group["name"]} Updated')
        fetched_group = self.client.get_group(self.created_group['uuid'])
        self.assertEqual(fetched_group['name'], f'{self.created_group["name"]} Updated')

    def test_get_group_policies(self) -> None:
        policies: List[PolicyType] = self.client.get_group_policies(self.created_group['uuid'])
        self.assertIsNotNone(policies)
