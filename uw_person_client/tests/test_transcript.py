# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from uw_person_client.tests import ModelTest
from uw_person_client.models import Person


class TranscriptTest(ModelTest):
    def test_get_transcripts(self):
        p = Person.objects.get_person_by_uwnetid(
            'javerage', include_student=True, include_student_transcripts=True)

        transcripts = p.student.transcripts.all()
        self.assertEqual(len(transcripts), 3)

        # default transcript sorting
        t1 = transcripts[0]
        t2 = transcripts[1]
        t3 = transcripts[2]
        self.assertLess(int(f'{t2.tran_term.year}{t2.tran_term.quarter}'),
                        int(f'{t1.tran_term.year}{t1.tran_term.quarter}'))
        self.assertLess(int(f'{t3.tran_term.year}{t3.tran_term.quarter}'),
                        int(f'{t2.tran_term.year}{t2.tran_term.quarter}'))

        # computed attributes
        self.assertEqual(t2.deductible_credits, 1.0)
        self.assertEqual(t2.grade_points, 19.0)
        self.assertEqual(t2.graded_attempted, 4.0)
        self.assertEqual(t2.nongraded_earned, 2.0)
        self.assertEqual(t2.total_attempted, 5.0)
        self.assertEqual(t2.total_earned, 6.0)

        data = t2.to_dict()
        self.assertEqual(data['deductible_credits'], 1.0)
        self.assertEqual(data['grade_points'], 19.0)
        self.assertEqual(data['graded_attempted'], 4.0)
        self.assertEqual(data['nongraded_earned'], 2.0)
        self.assertEqual(data['total_attempted'], 5.0)
        self.assertEqual(data['total_earned'], 6.0)
