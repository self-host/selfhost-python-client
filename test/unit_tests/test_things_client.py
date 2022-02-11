import json
from typing import List, Union, Dict

import responses
import unittest
import urllib
from selfhost_client import ThingsClient, DatasetType, ThingType, TimeseriesType


class TestThingsClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: ThingsClient = ThingsClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_things(self) -> None:
        mock_response: List[ThingType] = [
            {
                'created_by': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55',
                'name': 'My Thing',
                'state': 'active',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'type': 'office/building',
                'uuid': 'd2538949-90e9-4127-8251-764a4a7426cf'
            }
        ]
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, Union[int, List[str]]] = {
                'limit': 20,
                'offset': 0,
                'tags': ['tag', 'tag2']
            }
            res: List[ThingType] = self.client.get_things(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}'
                f'?{urllib.parse.urlencode(params, doseq=True)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))
            self.assertEqual(responses.calls[0].request.params.get('tags'), params['tags'])

    @responses.activate
    def test_create_thing(self) -> None:
        mock_response: ThingType = {
            'created_by': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55',
            'name': 'My Thing',
            'state': 'active',
            'tags': [
                'tag1',
                'tag2'
            ],
            'type': 'office/building',
            'uuid': 'd2538949-90e9-4127-8251-764a4a7426cf'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, Union[str, List[str]]] = {
                'name': 'My Thing',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'thing_type': 'office/building',
            }
            res: ThingType = self.client.create_thing(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['name'], params['name'])
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['tags'], params['tags'])
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['type'], params['thing_type'])

    @responses.activate
    def test_get_thing(self) -> None:
        mock_response: ThingType = {
            'created_by': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55',
            'name': 'My Thing',
            'state': 'active',
            'tags': [
                'tag1',
                'tag2'
            ],
            'type': 'office/building',
            'uuid': 'd2538949-90e9-4127-8251-764a4a7426cf'
        }
        thing_uuid: str = '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}',
                json=mock_response,
                status=200
            )

            res: ThingType = self.client.get_thing(thing_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}'
            )

    @responses.activate
    def test_update_thing(self) -> None:
        thing_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}',
                status=204
            )

            params: Dict[str, Union[str, List[str]]] = {
                'name': 'My Thing',
                'state': 'active',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'thing_type': 'office/building',
            }
            self.client.update_thing(thing_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['name'], params['name'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['state'],
                params['state']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['tags'], params['tags'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['type'],
                params['thing_type']
            )

    @responses.activate
    def test_delete_thing(self) -> None:
        thing_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}',
                status=204
            )

            self.client.delete_thing(thing_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}'
            )

    @responses.activate
    def test_get_thing_datasets(self) -> None:
        mock_response: List[DatasetType] = [
            {
                'checksum': '853ff93762a06ddbf722c4ebe9ddd66d8f63ddaea97f521c3ecc20da7c976020',
                'created': '2017-07-21T17:32:28+02:00',
                'created_by': 'f36834fb-8d96-4c01-b0e4-0bd85906bc25',
                'format': 'ini',
                'name': 'ML model yTgvX7z',
                'size': 0,
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'thing_uuid': 'f36834fb-8d96-4c01-b0e4-0bd85906bc25',
                'updated': '2017-07-21T17:32:28+02:00',
                'updated_by': 'A36834fb-8d96-4c01-b0e4-0bd85906bc25',
                'uuid': '5e029cdf-4fee-42d2-9196-afbdfbdb9d8f'
            }
        ]
        thing_uuid: str = 'Ze7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}/datasets',
                json=mock_response,
                status=200
            )

            res: List[DatasetType] = self.client.get_thing_datasets(thing_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}/datasets'
            )

    @responses.activate
    def test_get_thing_timeseries(self) -> None:
        mock_response: List[TimeseriesType] = [
            {
                'created_by': '736834fb-8d96-4c01-b0e4-0bd85906bc25',
                'lower_bound': 0,
                'name': 'New timeseries',
                'si_unit': 'string',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'thing_uuid': 'A36834fb-8d96-4c01-b0e4-0bd85906bc25',
                'upper_bound': 0,
                'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
            }
        ]
        thing_uuid: str = 'Ze7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}'
                    f'/timeseries',
                json=mock_response,
                status=200
            )

            res: List[TimeseriesType] = self.client.get_thing_timeseries(thing_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._things_api_path}/{thing_uuid}/timeseries'
            )
