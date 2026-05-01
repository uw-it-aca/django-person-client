# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.test import TestCase
from django.core.management import call_command
from django.core.management.base import CommandError
from django.db import connections
from django.apps import apps
from unittest.mock import patch, MagicMock
from uw_person_client.management.commands.initialize_person_db import Command
import os


class FakeUnmanagedModel:
    class _meta:
        app_label = 'uw_person_client'
        db_table = 'fake_unmanaged_table'
        managed = False


class TestSetupUWPersonCommand(TestCase):
    databases = {'default', 'uw_person'}

    def test_get_person_connection_success(self):
        cmd = Command()
        conn = cmd.get_person_connection()
        self.assertIs(conn, connections['uw_person'])

    def test_get_person_connection_missing_db(self):
        cmd = Command()

        with patch.dict(connections.databases, {}, clear=True):
            with self.assertRaises(CommandError):
                cmd.get_person_connection()

    def test_handle_raises_if_not_localdev(self):
        cmd = Command()

        with patch.dict(os.environ, {'ENV': 'prod'}):
            with self.assertRaises(CommandError):
                cmd.handle()

    @patch('uw_person_client.management.commands.initialize_person_db.'
           'Command.create_person_models')
    @patch('django.core.management.call_command')
    def test_handle_loads_fixtures(self,
                                   mock_call_command,
                                   mock_create_models):
        cmd = Command()

        with patch.dict(os.environ, {'ENV': 'localdev'}):
            cmd.handle()

        mock_create_models.assert_called_once()

        expected_fixtures = [
            'person.json', 'employee.json', 'term.json', 'major.json',
            'student.json', 'adviser.json', 'transfer.json',
            'transcript.json', 'hold.json', 'degree.json', 'sport.json'
        ]

        for call, fixture in zip(mock_call_command.call_args_list,
                                 expected_fixtures):
            _, kwargs = call
            self.assertEqual(kwargs['database'], 'uw_person')
            self.assertEqual(kwargs['app_label'], 'uw_person_client')
            self.assertEqual(kwargs['fixture_name'], fixture)
