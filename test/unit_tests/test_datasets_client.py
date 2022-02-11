import json
from typing import List, Dict, Union

import responses
import unittest
import urllib

from selfhost_client import DatasetsClient, DatasetType


class TestDatasetsClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: DatasetsClient = DatasetsClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_datasets(self) -> None:
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
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, int] = {
                'limit': 20,
                'offset': 0,
            }
            res: List[DatasetType] = self.client.get_datasets(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}'
                f'?{urllib.parse.urlencode(params)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))

    @responses.activate
    def test_create_dataset(self) -> None:
        mock_response: DatasetType = {
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

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, Union[str, List[str]]] = {
                'name': 'ML model yTgvX7z',
                'dataset_format': 'ini',
                'content': 'aGVsbG8sIHdvcmxkIQ==',
                'thing_uuid': 'f36834fb-8d96-4c01-b0e4-0bd85906bc25',
                'tags': [
                    'tag1',
                    'tag2'
                ],
            }
            res: DatasetType = self.client.create_dataset(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['name'], params['name'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['format'],
                params['dataset_format']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['content'], params['content'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['thing_uuid'],
                params['thing_uuid']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['tags'], params['tags'])

    @responses.activate
    def test_get_dataset(self) -> None:
        mock_response: DatasetType = {
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
        dataset_uuid: str = '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}',
                json=mock_response,
                status=200
            )

            res: DatasetType = self.client.get_dataset(dataset_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}'
            )

    @responses.activate
    def test_update_dataset(self) -> None:
        dataset_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}',
                status=204
            )

            params: Dict[str, Union[str, List[str]]] = {
                'name': 'ML model yTgvX7z',
                'dataset_format': 'ini',
                'content': 'aGVsbG8sIHdvcmxkIQ==',
                'thing_uuid': 'f36834fb-8d96-4c01-b0e4-0bd85906bc25',
                'tags': [
                    'tag1',
                    'tag2'
                ],
            }
            self.client.update_dataset(dataset_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['name'], params['name'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['format'],
                params['dataset_format']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['content'], params['content'])
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['tags'], params['tags'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['thing_uuid'],
                params['thing_uuid']
            )

    @responses.activate
    def test_delete_dataset(self) -> None:
        dataset_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}',
                status=204
            )

            self.client.delete_dataset(dataset_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}'
            )

    @responses.activate
    def test_get_dataset_raw_content(self) -> None:
        mock_response: str = 'content'
        dataset_uuid: str = 'Ze7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}/raw',
                json=mock_response,
                status=200
            )

            res: str = self.client.get_dataset_raw_content(dataset_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._datasets_api_path}/{dataset_uuid}/raw'
            )
