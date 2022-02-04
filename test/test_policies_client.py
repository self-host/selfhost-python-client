import json
from typing import List, Union, Dict

import responses
import unittest
import urllib

from selfhost_client import PoliciesClient, PolicyType


class TestPoliciesClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: PoliciesClient = PoliciesClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_policies(self) -> None:
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
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, Union[int, List[str]]] = {
                'limit': 20,
                'offset': 0,
                'group_uuids': ['5ce5d3cd-ff99-4342-a19e-fdb1b5805178', '5ce5d3cd-ff99-4342-a19e-fdb1b5805178']
            }
            res: List[PolicyType] = self.client.get_policies(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}'
                f'?{urllib.parse.urlencode(params, doseq=True)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))
            self.assertEqual(responses.calls[0].request.params.get('group_uuids'), params['group_uuids'])

    @responses.activate
    def test_create_policy(self):
        mock_response: PolicyType = {
            'action': 'read',
            'effect': 'allow',
            'group_uuid': '810d38bb-6a8e-4d36-b853-7350b67cb041',
            'priority': 10,
            'resource': 'timeseries/%',
            'uuid': '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, Union[str, int]] = {
                'action': 'read',
                'effect': 'allow',
                'group_uuid': '810d38bb-6a8e-4d36-b853-7350b67cb041',
                'priority': 10,
                'resource': 'timeseries/%',
            }
            res: PolicyType = self.client.create_policy(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_get_policy(self) -> None:
        mock_response: PolicyType = {
            'action': 'read',
            'effect': 'allow',
            'group_uuid': '810d38bb-6a8e-4d36-b853-7350b67cb041',
            'priority': 10,
            'resource': 'timeseries/%',
            'uuid': '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'
        }
        policy_uuid: str = '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}/{policy_uuid}',
                json=mock_response,
                status=200
            )

            res: PolicyType = self.client.get_policy(policy_uuid)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}/{policy_uuid}'
            )

    @responses.activate
    def test_update_policy(self) -> None:
        policy_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}/{policy_uuid}',
                status=204
            )

            params: Dict[str, Union[str, int]] = {
                'action': 'read',
                'effect': 'allow',
                'group_uuid': '810d38bb-6a8e-4d36-b853-7350b67cb041',
                'priority': 10,
                'resource': 'timeseries/%',
            }

            self.client.update_policy(policy_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}/{policy_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_delete_policy(self) -> None:
        policy_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}/{policy_uuid}',
                status=204
            )

            self.client.delete_policy(policy_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._policies_api_path}/{policy_uuid}'
            )
