# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from uw_person_client.models import PersonQueue, EnrolledStudentQueue
from uw_person_client.utils import sync_person
from uw_person_client.exceptions import PersonNotFoundException


class UtilsTest(TestCase):
    fixtures = ['person.json']

    def test_sync_existing(self):
        uwnetid = 'javerage'
        person = sync_person(uwnetid)
        self.assertEqual(person.uwnetid, uwnetid)

    def test_sync_unknown(self):
        uwnetid = 'nobody'
        self.assertRaises(
            PersonNotFoundException, sync_person, uwnetid, timeout=1)

        model = PersonQueue.objects.get(uwnetid=uwnetid)
        self.assertEqual(model.uwnetid, uwnetid)
