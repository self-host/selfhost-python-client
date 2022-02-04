import json
from typing import List, Dict, Union

import responses
import unittest
import urllib

from selfhost_client import ProgramsClient, ProgramType


class TestProgramsClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: ProgramsClient = ProgramsClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_programs(self) -> None:
        mock_response: List[ProgramType] = [
            {
                'deadline': 500,
                'language': 'string',
                'name': 'My program',
                'schedule': '0 45 23 * * 6',
                'state': 'active',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'type': 'routine',
                'uuid': '47daa6eb-bd1c-49de-9782-1e9422a206f5'
            }
        ]
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, Union[str, List[str]]] = {
                'limit': 20,
                'offset': 0,
                'tags': ['tag', 'tag2']
            }
            res: List[ProgramType] = self.client.get_programs(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}'
                f'?{urllib.parse.urlencode(params, doseq=True)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))
            self.assertEqual(responses.calls[0].request.params.get('tags'), params['tags'])

    @responses.activate
    def test_create_program(self) -> None:
        mock_response: ProgramType = {
            'deadline': 500,
            'language': 'string',
            'name': 'My program',
            'schedule': '0 45 23 * * 6',
            'state': 'active',
            'tags': [
                'tag1',
                'tag2'
            ],
            'type': 'routine',
            'uuid': '47daa6eb-bd1c-49de-9782-1e9422a206f5'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, Union[str, int, List[str]]] = {
                'name': 'New program',
                'program_type': 'routine',
                'state': 'active',
                'schedule': '0 45 23 * * 6',
                'deadline': 500,
                'language': 'string',
                'tags': [
                    'tag1',
                    'tag2'
                ],
            }
            res: ProgramType = self.client.create_program(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['name'], params['name'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['type'],
                params['program_type']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['state'], params['state'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['schedule'],
                params['schedule']
            )
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['deadline'],
                params['deadline']
            )
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['language'],
                params['language']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['tags'], params['tags'])

    @responses.activate
    def test_get_program(self) -> None:
        mock_response: ProgramType = {
            'deadline': 500,
            'language': 'string',
            'name': 'My program',
            'schedule': '0 45 23 * * 6',
            'state': 'active',
            'tags': [
                'tag1',
                'tag2'
            ],
            'type': 'routine',
            'uuid': '47daa6eb-bd1c-49de-9782-1e9422a206f5'
        }
        program_uuid: str = '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}/{program_uuid}',
                json=mock_response,
                status=200
            )

            res: ProgramType = self.client.get_program(program_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}/{program_uuid}'
            )

    @responses.activate
    def test_update_program(self) -> None:
        program_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}/{program_uuid}',
                status=204
            )

            params: Dict[str, Union[str, int, List[str]]] = {
                'name': 'My program',
                'program_type': 'routine',
                'state': 'active',
                'schedule': '0 45 23 * * 6',
                'deadline': 500,
                'language': 'string',
                'tags': [
                    'tag1',
                    'tag2'
                ],
            }
            self.client.update_program(program_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}/{program_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['name'], params['name'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['type'],
                params['program_type']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['state'], params['state'])
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['schedule'],
                params['schedule']
            )
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['deadline'],
                params['deadline']
            )
            self.assertEqual(
                json.loads(responses.calls[0].request.body.decode('utf-8'))['language'],
                params['language']
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8'))['tags'], params['tags'])

    @responses.activate
    def test_delete_program(self):
        program_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}/{program_uuid}',
                status=204
            )

            self.client.delete_program(program_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._programs_api_path}/{program_uuid}'
            )
