# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.db import connections
from django.apps import apps
import os


class Command(BaseCommand):
    help = 'Set up the uw_person database for a localdev environment.'

    def create_person_models(self):
        unmanaged_models = [m for m in apps.get_models() if (
            m._meta.app_label == 'uw_person_client' and
            m._meta.managed is False)]

        connection = self.get_person_connection()
        existing_tables = connection.introspection.table_names()

        with connection.schema_editor() as schema_editor:
            for model in unmanaged_models:
                if model._meta.db_table not in existing_tables:
                    schema_editor.create_model(model)

    def get_person_connection(self):
        if 'uw_person' not in connections.databases:
            raise CommandError(
                'The "uw_person" database alias is not configured. '
                'Add a "uw_person" entry to DATABASES and ensure any '
                'database router configuration routes uw_person_client '
                'models to that alias.'
            )
        return connections['uw_person']

    def handle(self, *args, **options):
        if os.getenv('ENV', '') != 'localdev':
            raise CommandError('Localdev only!')

        self.create_person_models()

        # Load uw_person data
        for fixture in [
                'person.json', 'employee.json', 'term.json', 'major.json',
                'student.json', 'adviser.json', 'transfer.json',
                'transcript.json', 'hold.json', 'degree.json', 'sport.json']:
            call_command('loaddata', fixture, database='uw_person',
                         app_label='uw_person_client')
