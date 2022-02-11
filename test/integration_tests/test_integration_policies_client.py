import uuid
from typing import List, Dict

import unittest

from selfhost_client import SelfHostClient, GroupType, PolicyType


class TestIntegrationPoliciesClient(unittest.TestCase):
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
        cls.created_policy: PolicyType = cls.client.create_policy(
            group_uuid=cls.created_group['uuid'],
            priority=10,
            effect='allow',
            action='read',
            resource='things'
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_group(cls.created_group['uuid'])

    def test_get_policies(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        policies: List[PolicyType] = self.client.get_policies(**params)
        self.assertIsNotNone(policies)

    def test_create_and_delete_policies(self) -> None:
        # Create and delete happens in setup and teardown methods.
        self.assertEqual(self.created_policy['group_uuid'], self.created_group['uuid'])

    def test_get_policy(self) -> None:
        fetched_policy: PolicyType = self.client.get_policy(self.created_policy['uuid'])
        self.assertEqual(fetched_policy['group_uuid'], self.created_group['uuid'])

    def test_update_policy(self) -> None:
        self.client.update_policy(
            policy_uuid=self.created_policy['uuid'],
            priority=self.created_policy['priority'] + 10,
            effect='deny',
            action='create',
            resource=f'{self.created_policy["resource"]} Updated'
        )
        fetched_policy: PolicyType = self.client.get_policy(self.created_policy['uuid'])
        self.assertEqual(fetched_policy['priority'], self.created_policy["priority"] + 10),
        self.assertEqual(fetched_policy['effect'], 'deny')
        self.assertEqual(fetched_policy['action'], 'create')
        self.assertEqual(fetched_policy['resource'], f'{self.created_policy["resource"]} Updated')
