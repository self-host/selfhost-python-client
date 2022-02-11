import uuid
from typing import List, Dict

import unittest

from selfhost_client import SelfHostClient, ProgramType


class TestIntegrationProgramsClient(unittest.TestCase):
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
        cls.created_program: ProgramType = cls.client.create_program(
            name=cls.unique_name,
            program_type='routine',
            state='active',
            schedule='0 45 23 * * 6',
            deadline=500,
            language='tengo',
            tags=['test_tag']
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.client.delete_program(cls.created_program['uuid'])

    def test_get_programs(self) -> None:
        params: Dict[str, int] = {
            'limit': 20,
            'offset': 0
        }
        programs: List[ProgramType] = self.client.get_programs(**params)
        self.assertIsNotNone(programs)

    def test_create_and_delete_program(self) -> None:
        # Create and delete happens in setup and teardown methods.
        self.assertEqual(self.created_program['name'], self.unique_name)

    def test_get_program(self) -> None:
        fetched_program: ProgramType = self.client.get_program(self.created_program['uuid'])
        self.assertEqual(fetched_program['name'], self.created_program['name'])

    def test_update_program(self) -> None:
        self.client.update_program(
            program_uuid=self.created_program['uuid'],
            name=f'{self.created_program["name"]} Updated',
            program_type='module',
            state='inactive',
            schedule='0 45 23 * * 5',
            deadline=1000,
            language='tengo',
            tags=['tag_updated']
        )
        fetched_program: ProgramType = self.client.get_program(self.created_program['uuid'])
        self.assertEqual(fetched_program['name'], f'{self.created_program["name"]} Updated')
        self.assertEqual(fetched_program['type'], 'module')
        self.assertEqual(fetched_program['state'], 'inactive')
        self.assertEqual(fetched_program['schedule'], '0 45 23 * * 5')
        self.assertEqual(fetched_program['deadline'], 1000)
        self.assertEqual(fetched_program['language'], 'tengo')
        self.assertEqual(fetched_program['tags'], ['tag_updated'])
