import json
from typing import List, Dict

import responses
import unittest
import urllib

from selfhost_client import GroupsClient, GroupType, PolicyType


class TestGroupsClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: GroupsClient = GroupsClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_groups(self) -> None:
        mock_response: List[GroupType] = [
            {
                'name': 'Test group',
                'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
            }
        ]
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, int] = {
                'limit': 20,
                'offset': 0
            }
            res: List[GroupType] = self.client.get_groups(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}'
                f'?{urllib.parse.urlencode(params)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))

    @responses.activate
    def test_create_group(self) -> None:
        mock_response: GroupType = {
            'name': 'New group',
            'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, str] = {
                'name': 'New group',
            }
            res: GroupType = self.client.create_group(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_get_group(self) -> None:
        mock_response: GroupType = {
            'name': 'Test group',
            'uuid': '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        }
        group_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}',
                json=mock_response,
                status=200
            )

            res: GroupType = self.client.get_group(group_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}'
            )

    @responses.activate
    def test_update_group(self) -> None:
        group_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}',
                status=204
            )

            params: Dict[str, str] = {
                'name': 'Updated group name',
            }
            self.client.update_group(group_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_delete_group(self) -> None:
        group_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}',
                status=204
            )

            self.client.delete_group(group_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}'
            )

    @responses.activate
    def test_get_group_policies(self) -> None:
        mock_response: List[PolicyType] = [
            {
                'action': 'read',
                'effect': 'allow',
                'group_uuid': '810d38bb-6a8e-4d36-b853-7350b67cb041',
                'priority': 10,
                'resource': 'timeseries/%',
                'uuid': '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'
            }
        ]
        group_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}/policies',
                json=mock_response,
                status=200
            )

            res: List[PolicyType] = self.client.get_group_policies(group_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._groups_api_path}/{group_uuid}/policies'
            )
