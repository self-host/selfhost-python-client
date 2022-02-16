import json
from typing import List, Dict, Union

import pyrfc3339
import responses
import unittest
import urllib

from selfhost_client import AlertsClient, AlertType, CreatedAlertResponse


class TestThingsClient(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url: str = 'http://example.com'
        self.username: str = 'test'
        self.password: str = 'test'
        self.client: AlertsClient = AlertsClient(
            base_url=self.base_url,
            username=self.username,
            password=self.password
        )

    @responses.activate
    def test_get_alerts(self) -> None:
        mock_response: List[AlertType] = [
            {
                'created': '2020-03-09T09:48:30.035+02:00',
                'description': 'new alert',
                'duplicate': 0,
                'environment': 'string',
                'event': 'string',
                'last_receive_time': '2020-03-09T09:48:30.035+02:00',
                'origin': 'string',
                'previous_severity': 'critical',
                'rawdata': 'string',
                'resource': 'string',
                'service': [
                    'service1',
                    'service2'
                ],
                'severity': 'critical',
                'status': 'open',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'timeout': 0,
                'uuid': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55',
                'value': 'string'
            }
        ]
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}',
                json=mock_response,
                status=200
            )

            params: Dict[str, Union[str, int, List[str]]] = {
                'limit': 20,
                'offset': 0,
                'resource': 'string',
                'environment': 'string',
                'event': 'string',
                'origin': 'string',
                'status': 'open',
                'severity_le': 'critical',
                'severity_ge': 'critical',
                'severity': 'critical',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'service': [
                    'service1',
                    'service2'
                ],
            }
            res: List[AlertType] = self.client.get_alerts(**params)

            self.assertEqual(len(responses.calls), 1)
            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}'
                f'?{urllib.parse.urlencode(params, doseq=True)}'
            )
            self.assertEqual(responses.calls[0].request.params.get('limit'), str(params['limit']))
            self.assertEqual(responses.calls[0].request.params.get('offset'), str(params['offset']))
            self.assertEqual(responses.calls[0].request.params.get('resource'), params['resource'])
            self.assertEqual(responses.calls[0].request.params.get('environment'), params['environment'])
            self.assertEqual(responses.calls[0].request.params.get('event'), params['event'])
            self.assertEqual(responses.calls[0].request.params.get('origin'), params['origin'])
            self.assertEqual(responses.calls[0].request.params.get('status'), params['status'])
            self.assertEqual(responses.calls[0].request.params.get('severity_le'), params['severity_le'])
            self.assertEqual(responses.calls[0].request.params.get('severity_ge'), params['severity_ge'])
            self.assertEqual(responses.calls[0].request.params.get('severity'), params['severity'])
            self.assertEqual(responses.calls[0].request.params.get('tags'), params['tags'])
            self.assertEqual(responses.calls[0].request.params.get('service'), params['service'])

            self.assertEqual(res[0]['description'], mock_response[0]['description'])
            self.assertEqual(res[0]['duplicate'], mock_response[0]['duplicate'])
            self.assertEqual(res[0]['environment'], mock_response[0]['environment'])
            self.assertEqual(res[0]['event'], mock_response[0]['event'])
            self.assertEqual(res[0]['origin'], mock_response[0]['origin'])
            self.assertEqual(res[0]['previous_severity'], mock_response[0]['previous_severity'])
            self.assertEqual(res[0]['rawdata'], mock_response[0]['rawdata'])
            self.assertEqual(res[0]['resource'], mock_response[0]['resource'])
            self.assertEqual(res[0]['service'], mock_response[0]['service'])
            self.assertEqual(res[0]['severity'], mock_response[0]['severity'])
            self.assertEqual(res[0]['status'], mock_response[0]['status'])
            self.assertEqual(res[0]['tags'], mock_response[0]['tags'])
            self.assertEqual(res[0]['timeout'], mock_response[0]['timeout'])
            self.assertEqual(res[0]['uuid'], mock_response[0]['uuid'])
            self.assertEqual(res[0]['value'], mock_response[0]['value'])
            self.assertEqual(
                res[0]['created'],
                pyrfc3339.parse('2020-03-09T09:48:30.035+02:00')
            )
            self.assertEqual(
                res[0]['last_receive_time'],
                pyrfc3339.parse('2020-03-09T09:48:30.035+02:00')
            )

    @responses.activate
    def test_create_alert(self) -> None:
        mock_response: CreatedAlertResponse = {
            'uuid': 'a9214980-2c89-42e4-a08d-71689af86b67'
        }

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.POST,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}',
                json=mock_response,
                status=201
            )

            params: Dict[str, Union[str, int, List[str]]] = {
                'resource': 'string',
                'environment': 'string',
                'event': 'string',
                'value': 'string',
                'description': 'string',
                'origin': 'string',
                'severity': 'critical',
                'status': 'open',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'service': [
                    'service1',
                    'service2'
                ],
                'timeout': 1000,
                'rawdata': 'string'
            }
            res: CreatedAlertResponse = self.client.create_alert(**params)

            self.assertEqual(res, mock_response)
            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_get_alert(self) -> None:
        mock_response: AlertType = {
            'created': '2020-03-09T09:48:30.035+02:00',
            'description': 'new alert',
            'duplicate': 0,
            'environment': 'string',
            'event': 'string',
            'last_receive_time': '2020-03-09T09:48:30.035+02:00',
            'origin': 'string',
            'previous_severity': 'critical',
            'rawdata': 'string',
            'resource': 'string',
            'service': [
                'service1',
                'service2'
            ],
            'severity': 'critical',
            'status': 'open',
            'tags': [
                'tag1',
                'tag2'
            ],
            'timeout': 0,
            'uuid': '5d8c23d7-3a78-4159-aa40-e3ef3d9bfe55',
            'value': 'string'
        }
        alert_uuid: str = '5ce5d3cd-ff99-4342-a19e-fdb1b5805178'

        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.GET,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}/{alert_uuid}',
                json=mock_response,
                status=200
            )

            res: AlertType = self.client.get_alert(alert_uuid)

            self.assertEqual(len(responses.calls), 1)
            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}/{alert_uuid}'
            )

            self.assertEqual(res['description'], mock_response['description'])
            self.assertEqual(res['duplicate'], mock_response['duplicate'])
            self.assertEqual(res['environment'], mock_response['environment'])
            self.assertEqual(res['event'], mock_response['event'])
            self.assertEqual(res['origin'], mock_response['origin'])
            self.assertEqual(res['previous_severity'], mock_response['previous_severity'])
            self.assertEqual(res['rawdata'], mock_response['rawdata'])
            self.assertEqual(res['resource'], mock_response['resource'])
            self.assertEqual(res['service'], mock_response['service'])
            self.assertEqual(res['severity'], mock_response['severity'])
            self.assertEqual(res['status'], mock_response['status'])
            self.assertEqual(res['tags'], mock_response['tags'])
            self.assertEqual(res['timeout'], mock_response['timeout'])
            self.assertEqual(res['uuid'], mock_response['uuid'])
            self.assertEqual(res['value'], mock_response['value'])
            self.assertEqual(
                res['created'],
                pyrfc3339.parse('2020-03-09T09:48:30.035+02:00')
            )
            self.assertEqual(
                res['last_receive_time'],
                pyrfc3339.parse('2020-03-09T09:48:30.035+02:00')
            )

    @responses.activate
    def test_update_alert(self) -> None:
        alert_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.PUT,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}/{alert_uuid}',
                status=204
            )

            params: Dict[str, Union[str, int, List[str]]] = {
                'resource': 'string',
                'environment': 'string',
                'event': 'string',
                'value': 'string',
                'description': 'string',
                'origin': 'string',
                'severity': 'critical',
                'status': 'open',
                'tags': [
                    'tag1',
                    'tag2'
                ],
                'service': [
                    'service1',
                    'service2'
                ],
                'timeout': 1000,
                'rawdata': 'string'
            }
            self.client.update_alert(alert_uuid, **params)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}/{alert_uuid}'
            )
            self.assertEqual(json.loads(responses.calls[0].request.body.decode('utf-8')), params)

    @responses.activate
    def test_delete_alert(self) -> None:
        alert_uuid: str = '7e7823cc-44fa-403d-853f-d5ce48a002e4'
        with self.subTest('call successful with complete parameter list'):
            responses.add(
                responses.DELETE,
                url=f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}/{alert_uuid}',
                status=204
            )

            self.client.delete_alert(alert_uuid)

            self.assertEqual(len(responses.calls), 1)

            self.assertEqual(
                responses.calls[0].request.url,
                f'{self.base_url}/{self.client._api_version}/{self.client._alerts_api_path}/{alert_uuid}'
            )
