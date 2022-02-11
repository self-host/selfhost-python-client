import json
from typing import List, Dict, Union

import responses
import unittest
import urllib

from selfhost_client import TimeseriesClient, TimeseriesType, TimeseriesDataPointType, TimeseriesDataType


class TestPCTTimeseriesClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: TimeseriesClient = TimeseriesClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_timeseries(self) -> None:
        mock_response: List[TimeseriesType] = [
            {
                'created_by': '1740f1e4-d2c6-4943-9976-9ff10eab90b2',
                'lower_bound': 0,
                'name': 'new timeseries',
                'si_unit': 'C',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'thing_uuid': 'e21ae595-15a5-4f11-8992-9d33600cc1ee',
                'upper_bound': 0,
                'uuid': 'a21ae595-15a5-4f11-8992-9d33600cc1ee'
            }
        ]
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, Union[int, List[str]]] = {
                'limit': 20,
                'offset': 0,
                'tags': ['tag', 'tag2']
            }
            res: List[TimeseriesType] = self.client.get_timeseries(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}'
                f'?{urllib.parse.urlencode(params, doseq=True)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))
            self.assertEqual(responses.calls[0].request.params.get('tags'), params['tags'])

    @responses.activate
    def test_create_timeseries(self) -> None:
        mock_response: TimeseriesType = {
            'created_by': '1740f1e4-d2c6-4943-9976-9ff10eab90b2',
            'lower_bound': 0,
            'name': 'new timeseries',
            'si_unit': 'C',
            'tags': [
                'tag1',
                'tag2'
            ],
            'thing_uuid': 'e21ae595-15a5-4f11-8992-9d33600cc1ee',
            'upper_bound': 0,
            'uuid': 'a21ae595-15a5-4f11-8992-9d33600cc1ee'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, Union[int, str, List[str]]] = {
                'name': 'new timeseries',
                'si_unit': 'C',
                'thing_uuid': 'e21ae595-15a5-4f11-8992-9d33600cc1ee',
                'lower_bound': 0,
                'upper_bound': 0,
                'tags': [
                    'tag1',
                    'tag2'
                ]
            }
            res: TimeseriesType = self.client.create_timeseries(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_get_timeseries_by_uuid(self) -> None:
        mock_response: TimeseriesType = {
            'created_by': '1740f1e4-d2c6-4943-9976-9ff10eab90b2',
            'lower_bound': 0,
            'name': 'new timeseries',
            'si_unit': 'C',
            'tags': [
                'tag1',
                'tag2'
            ],
            'thing_uuid': 'e21ae595-15a5-4f11-8992-9d33600cc1ee',
            'upper_bound': 0,
            'uuid': 'a21ae595-15a5-4f11-8992-9d33600cc1ee'
        }
        timeseries_uuid: str = '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}',
                json=mock_response,
                status=200
            )

            res: TimeseriesType = self.client.get_timeseries_by_uuid(timeseries_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}'
            )

    @responses.activate
    def test_update_timeseries(self) -> None:
        timeseries_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}',
                status=204
            )

            params: Dict[str, Union[int, str, List[str]]] = {
                'name': 'updated timeseries',
                'si_unit': 'C',
                'thing_uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4',
                'lower_bound': 0,
                'upper_bound': 0,
                'tags': [
                    'tag1',
                    'tag2'
                ]
            }
            self.client.update_timeseries(timeseries_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_delete_timeseries(self) -> None:
        timeseries_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}',
                status=204
            )

            self.client.delete_timeseries(timeseries_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}'
            )

    @responses.activate
    def test_get_timeseries_data(self) -> None:
        mock_response: List[TimeseriesDataPointType] = [
            {
                'ts': '2022-01-14T12:43:44.147Z',
                'v': 3.14
            }
        ]
        timeseries_uuid: str = 'Ze7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}'
                    f'/data',
                json=mock_response,
                status=200
            )

            params: Dict[str, Union[str, int]] = {
                'start': '2022-01-14T12:43:44.147Z',
                'end': '2022-01-14T12:43:44.147Z',
                'unit': 'C',
                'ge': 0,
                'le': 0,
                'precision': 'second',
                'aggregate': 'avg',
                'timezone': 'UTC'
            }

            res: List[TimeseriesDataPointType] = self.client.get_timeseries_data(timeseries_uuid, **params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}/data'
                f'?{urllib.parse.urlencode(params)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('start'), params['start'])
            self.assertEqual(responses.calls[0].request.params.get('end'), params['end'])
            self.assertEqual(responses.calls[0].request.params.get('unit'), params['unit'])
            self.assertEqual(responses.calls[0].request.params.get('ge'), str(params['ge']))
            self.assertEqual(responses.calls[0].request.params.get('le'), str(params['le']))
            self.assertEqual(responses.calls[0].request.params.get('precision'), params['precision'])
            self.assertEqual(responses.calls[0].request.params.get('aggregate'), params['aggregate'])
            self.assertEqual(responses.calls[0].request.params.get('timezone'), params['timezone'])

    @responses.activate
    def test_create_timeseries_data(self) -> None:
        mock_response: TimeseriesDataPointType = {
            'ts': '2022-01-14T12:43:44.147Z',
            'v': 3.14
        }
        timeseries_uuid: str = 'Ze7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}'
                    f'/data',
                json=mock_response,
                status=201
            )

            unit: str = 'C'

            body: List[TimeseriesDataPointType] = [
                {'ts': '2022-01-14T12:52:04.147Z', 'v': 3.01},
                {'ts': '2022-01-14T12:52:04.147Z', 'v': 3.99}
            ]

            self.client.create_timeseries_data(timeseries_uuid, body, unit)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}/data'
                f'?{urllib.parse.urlencode({"unit": unit})}'
            )
            self.assertEqual(responses.calls[0].request.params.get('unit'), unit)
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), body)

    @responses.activate
    def test_delete_timeseries_data(self) -> None:
        timeseries_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}'
                    f'/data',
                status=204
            )

            params: Dict[str, Union[str, int]] = {
                'start': '2022-01-14T12:52:04.147Z',
                'end': '2022-01-14T12:52:04.147Z',
                'ge': 0,
                'le': 0
            }

            self.client.delete_timeseries_data(timeseries_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._timeseries_api_path}/{timeseries_uuid}/data'
                f'?{urllib.parse.urlencode(params)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('start'), params['start'])
            self.assertEqual(responses.calls[0].request.params.get('end'), params['end'])
            self.assertEqual(responses.calls[0].request.params.get('ge'), str(params['ge']))
            self.assertEqual(responses.calls[0].request.params.get('le'), str(params['le']))

    @responses.activate
    def test_get_multiple_timeseries_data(self) -> None:
        mock_response: List[TimeseriesDataType] = [
            {
                'data': [{
                    'ts': '2022-01-14T12:43:44.147Z',
                    'v': 3.14
                }],
                'uuid': 'ze7823cc-44fa-403d-853f-d5ce48a002e4'
            }
        ]
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/tsquery',
                json=mock_response,
                status=200
            )

            params: Dict[str, Union[str, int, List[str]]] = {
                'uuids': ['be7823cc-44fa-403d-853f-d5ce48a002e4', 'ze7823cc-44fa-403d-853f-d5ce48a002e4'],
                'start': '2022-01-14T12:43:44.147Z',
                'end': '2022-01-14T12:43:44.147Z',
                'unit': 'C',
                'ge': 0,
                'le': 0,
                'precision': 'second',
                'aggregate': 'avg',
                'timezone': 'UTC'
            }

            res: List[TimeseriesDataType] = self.client.get_multiple_timeseries_data(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/tsquery'
                f'?{urllib.parse.urlencode(params, doseq=True)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('uuids'), params['uuids'])
            self.assertEqual(responses.calls[0].request.params.get('start'), params['start'])
            self.assertEqual(responses.calls[0].request.params.get('end'), params['end'])
            self.assertEqual(responses.calls[0].request.params.get('unit'), params['unit'])
            self.assertEqual(responses.calls[0].request.params.get('ge'), str(params['ge']))
            self.assertEqual(responses.calls[0].request.params.get('le'), str(params['le']))
            self.assertEqual(responses.calls[0].request.params.get('precision'), params['precision'])
            self.assertEqual(responses.calls[0].request.params.get('aggregate'), params['aggregate'])
            self.assertEqual(responses.calls[0].request.params.get('timezone'), params['timezone'])
