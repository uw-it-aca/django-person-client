# Copyright 2026 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.db import connections, router
from django.apps import apps
from django.db import models
from django.core.management import call_command


class TempUWPersonModel(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'uw_person_client'
        db_table = 'temp_person'
        managed = False


class TestUWPersonRouterIntegration(TestCase):
    databases = {'default', 'uw_person'}

    def setUp(self):
        self.model = TempUWPersonModel

    def test_db_for_read_routes_to_uw_person(self):
        db = router.db_for_read(self.model)
        self.assertEqual(db, 'uw_person')

    def test_db_for_write_routes_to_uw_person(self):
        db = router.db_for_write(self.model)
        self.assertEqual(db, 'uw_person')

    def test_other_app_not_routed(self):
        class OtherModel(models.Model):
            class Meta:
                app_label = 'other_app'
                managed = False

        self.assertEqual(router.db_for_read(OtherModel), 'default')
        self.assertEqual(router.db_for_write(OtherModel), 'default')

    def test_allow_migrate_uw_person_app_on_uw_person_db(self):
        allowed = router.allow_migrate('uw_person', 'uw_person_client')
        self.assertTrue(allowed)

    def test_allow_migrate_uw_person_app_on_default_db(self):
        allowed = router.allow_migrate('default', 'uw_person_client')
        self.assertFalse(allowed)

    def test_allow_migrate_other_app_on_uw_person_db(self):
        allowed = router.allow_migrate('uw_person', 'other_app')
        self.assertFalse(allowed)

    def test_allow_migrate_other_app_on_default_db(self):
        allowed = router.allow_migrate('default', 'other_app')
        self.assertTrue(allowed)

    def test_migrations_apply_only_to_uw_person_db(self):
        '''
        Verifies that migrations for uw_person_client only apply to the
        uw_person database and not the default database.
        '''
        # Run migrations for the uw_person_client app on the uw_person DB
        call_command(
            'migrate', 'uw_person_client', database='uw_person', verbosity=0)

        table_name = self.model._meta.db_table

        # Table should not exist in uw_person
        uw_conn = connections['uw_person']
        self.assertNotIn(table_name, uw_conn.introspection.table_names())

        # Table should not exist in default
        default_conn = connections['default']
        self.assertNotIn(table_name, default_conn.introspection.table_names())
