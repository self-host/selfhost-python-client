from typing import List, Dict

import unittest

from selfhost_client import SelfHostClient, AlertType, CreatedAlertResponse


class TestIntegrationAlertsClient(unittest.TestCase):
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
        cls.created_alert: CreatedAlertResponse = cls.client.create_alert(
            resource='webfrontend',
            environment='development',
            event='Down',
            value='OOM',
            description='Process died due to low memory',
            origin='watcher.go:check L123',
            severity='minor',
            status='open',
            service=['web'],
            tags=['test_tag'],
            timeout=3600,
            rawdata='aGVsbG8sIHdvcmxkIQo='
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_alert(cls.created_alert['uuid'])

    def test_get_alerts(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        alerts: List[AlertType] = self.client.get_alerts(**params)
        self.assertIsNotNone(alerts)

    def test_create_get_and_delete_alert(self) -> None:
        # Create and delete happens in setup and teardown methods.
        fetched_alert: AlertType = self.client.get_alert(self.created_alert['uuid'])
        self.assertEqual(fetched_alert['uuid'], self.created_alert['uuid'])
        self.assertEqual(fetched_alert['description'], 'Process died due to low memory')

    def test_update_alert(self) -> None:
        self.client.update_alert(
            self.created_alert['uuid'],
            resource='updated',
            environment='updated',
            event='updated',
            value='updated',
            description='updated',
            origin='updated',
            severity='trace',
            status='close',
            service=['web'],
            tags=['updated'],
            timeout=4000
        )
        fetched_alert: AlertType = self.client.get_alert(self.created_alert['uuid'])
        self.assertEqual(fetched_alert['resource'], 'updated')
        self.assertEqual(fetched_alert['environment'], 'updated')
        self.assertEqual(fetched_alert['event'], 'updated')
        self.assertEqual(fetched_alert['value'], 'updated')
        self.assertEqual(fetched_alert['description'], 'updated')
        self.assertEqual(fetched_alert['origin'], 'updated')
        self.assertEqual(fetched_alert['severity'], 'trace')
        self.assertEqual(fetched_alert['status'], 'close')
        self.assertEqual(fetched_alert['service'], ['web'])
        self.assertEqual(fetched_alert['tags'], ['updated'])
        self.assertEqual(fetched_alert['timeout'], 4000)
