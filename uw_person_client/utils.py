# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from uw_person_client.models import Person, PersonQueue, EnrolledStudentQueue
from uw_person_client.exceptions import PersonNotFoundException
import time


def sync_person(uwnetid, timeout=15):
    person = None
    pq = None
    start = time.time()

    while True:
        if time.time() >= start + timeout:
            break

        try:
            person = Person.objects.get_person_by_uwnetid(uwnetid)
            break
        except PersonNotFoundException:
            if pq is None:
                pq = PersonQueue(uwnetid=uwnetid)
                pq.save()
        except Exception as e:
            raise

        time.sleep(3)

    if person is None:
        raise PersonNotFoundException(uwnetid)

    if person.system_key is not None and len(person.system_key):
        esq = EnrolledStudentQueue(system_key=person.system_key)
        esq.save()

    return person
