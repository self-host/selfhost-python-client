import uuid
from typing import List, Dict

import unittest

from selfhost_client import SelfHostClient, ThingType, DatasetType, TimeseriesType


class TestIntegrationThingsClient(unittest.TestCase):
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
        cls.created_thing: ThingType = cls.client.create_thing(
            name=cls.unique_name,
            thing_type='thing',
            tags=['test_tag']
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_thing(cls.created_thing['uuid'])

    def test_get_things(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        things: List[ThingType] = self.client.get_things(**params)
        self.assertIsNotNone(things)

    def test_create_and_delete_thing(self) -> None:
        # Create and delete happens in setup and teardown methods.
        self.assertEqual(self.created_thing['name'], self.unique_name)

    def test_get_thing(self) -> None:
        fetched_thing: ThingType = self.client.get_thing(self.created_thing['uuid'])
        self.assertEqual(fetched_thing['name'], self.created_thing['name'])

    def test_update_thing(self) -> None:
        self.client.update_thing(
            thing_uuid=self.created_thing['uuid'],
            name=f'{self.created_thing["name"]} Updated',
            state='passive',
            thing_type=f'{self.created_thing["type"]} Updated',
            tags=['updated']
        )
        fetched_thing = self.client.get_thing(self.created_thing['uuid'])
        self.assertEqual(fetched_thing['name'], f'{self.created_thing["name"]} Updated')
        self.assertEqual(fetched_thing['state'], 'passive')
        self.assertEqual(fetched_thing['type'], f'{self.created_thing["type"]} Updated')
        self.assertEqual(fetched_thing['tags'], ['updated'])

    def test_get_thing_datasets(self) -> None:
        datasets: List[DatasetType] = self.client.get_thing_datasets(self.created_thing['uuid'])
        self.assertIsNotNone(datasets)

    def test_get_thing_timeseries(self) -> None:
        timeseries: List[TimeseriesType] = self.client.get_thing_timeseries(self.created_thing['uuid'])
        self.assertIsNotNone(timeseries)
