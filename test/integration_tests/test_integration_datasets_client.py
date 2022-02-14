import uuid
from typing import List, Dict, Any

import unittest

from selfhost_client import SelfHostClient, DatasetType


class TestIntegrationDatasetsClient(unittest.TestCase):
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
        cls.created_dataset: DatasetType = cls.client.create_dataset(
            name=cls.unique_name,
            dataset_format='ini',
            content='aGVsbG8sIHdvcmxkIQ==',
            tags=['test_tag']
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_dataset(cls.created_dataset['uuid'])

    def test_get_datasets(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        datasets: List[DatasetType] = self.client.get_datasets(**params)
        self.assertIsNotNone(datasets)

    def test_create_and_delete_dataset(self) -> None:
        # Create and delete happens in setup and teardown methods.
        self.assertEqual(self.created_dataset['name'], self.unique_name)

    def test_get_dataset(self) -> None:
        fetched_dataset: DatasetType = self.client.get_dataset(self.created_dataset['uuid'])
        self.assertEqual(fetched_dataset['name'], self.created_dataset['name'])

    def test_update_dataset(self) -> None:
        self.client.update_dataset(
            dataset_uuid=self.created_dataset['uuid'],
            name=f'{self.created_dataset["name"]} Updated',
            dataset_format='json',
            tags=['updated']
        )
        fetched_dataset: DatasetType = self.client.get_dataset(self.created_dataset['uuid'])
        self.assertEqual(fetched_dataset['name'], f'{self.created_dataset["name"]} Updated')
        self.assertEqual(fetched_dataset['format'], 'json')
        self.assertEqual(fetched_dataset['tags'], ['updated'])

    def test_get_dataset_raw_content(self):
        fetched_content: Any = self.client.get_dataset_raw_content(self.created_dataset['uuid'])
        self.assertIsNotNone(fetched_content)
