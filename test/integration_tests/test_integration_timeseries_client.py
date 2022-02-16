import uuid
from typing import List, Dict

import unittest

import pyrfc3339

from selfhost_client import SelfHostClient, TimeseriesType, TimeseriesDataPointType, TimeseriesDataType


class TestIntegrationTimeseriesClient(unittest.TestCase):
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
        cls.created_timeseries: TimeseriesType = cls.client.create_timeseries(
            name=cls.unique_name,
            si_unit='C',
            lower_bound=-50,
            upper_bound=50,
            tags=['test_tag']
        )
        cls.client.create_timeseries_data(cls.created_timeseries['uuid'], [{
            'v': 3.14,
            'ts': pyrfc3339.parse('2022-02-14T11:16:40.005Z')
        }])

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_timeseries_data(
            cls.created_timeseries['uuid'],
            start=pyrfc3339.parse('2022-02-13T11:16:40.005Z'),
            end=pyrfc3339.parse('2022-02-15T11:16:40.005Z')
        )
        cls.client.delete_timeseries(cls.created_timeseries['uuid'])

    def test_get_timeseries(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        timeseries: List[TimeseriesType] = self.client.get_timeseries(**params)
        self.assertIsNotNone(timeseries)

    def test_create_and_delete_timeseries(self) -> None:
        # Create and delete happens in setup and teardown methods.
        self.assertEqual(self.created_timeseries['name'], self.unique_name)

    def test_get_timeseries_by_uuid(self) -> None:
        fetched_timeseries: TimeseriesType = self.client.get_timeseries_by_uuid(self.created_timeseries['uuid'])
        self.assertEqual(fetched_timeseries['name'], self.created_timeseries['name'])

    def test_update_timeseries(self) -> None:
        self.client.update_timeseries(
            timeseries_uuid=self.created_timeseries['uuid'],
            name=f'{self.created_timeseries["name"]} Updated',
            si_unit='F',
            lower_bound=-100,
            upper_bound=100,
            tags=['updated']
        )
        fetched_timeseries: TimeseriesType = self.client.get_timeseries_by_uuid(self.created_timeseries['uuid'])
        self.assertEqual(fetched_timeseries['name'], f'{self.created_timeseries["name"]} Updated')
        self.assertEqual(fetched_timeseries['si_unit'], 'F')
        self.assertEqual(fetched_timeseries['lower_bound'], -100)
        self.assertEqual(fetched_timeseries['upper_bound'], 100)
        self.assertEqual(fetched_timeseries['tags'], ['updated'])

    def test_get_create_and_delete_timeseries_data(self) -> None:
        # Create and delete happens in the setup and teardown methods.
        fetched_timeseries_data: List[TimeseriesDataPointType] = self.client.get_timeseries_data(
            self.created_timeseries['uuid'],
            start=pyrfc3339.parse('2022-02-13T11:16:40.005Z'),
            end=pyrfc3339.parse('2022-02-15T11:16:40.005Z')
        )
        self.assertEqual(fetched_timeseries_data[0]['v'], 3.14)
        self.assertEqual(fetched_timeseries_data[0]['ts'], pyrfc3339.parse('2022-02-14T11:16:40.005Z'))

    def test_get_multiple_timeseries_data(self) -> None:
        fetched_timeseries_data: List[TimeseriesDataType] = self.client.get_multiple_timeseries_data(
            uuids=[self.created_timeseries['uuid']],
            start=pyrfc3339.parse('2022-02-13T11:16:40.005Z'),
            end=pyrfc3339.parse('2022-02-15T11:16:40.005Z')
        )
        self.assertEqual(fetched_timeseries_data[0]['uuid'], self.created_timeseries['uuid'])
        self.assertEqual(fetched_timeseries_data[0]['data'][0]['v'], 3.14)
        self.assertEqual(fetched_timeseries_data[0]['data'][0]['ts'], pyrfc3339.parse('2022-02-14T11:16:40.005Z'))
