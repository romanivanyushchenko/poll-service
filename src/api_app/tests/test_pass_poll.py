import json

from rest_framework.test import APITestCase

from api_app.models import PollModel, UserAnswerModel
from api_app.tests.base import create_test_poll


class PassPollTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.poll = create_test_poll()

    def test_get_poll_list(self):
        poll = PollModel.objects.get(name='Test Poll', description='Super!')
        q1 = poll.questions.all()[0]
        q2 = poll.questions.all()[1]
        q3 = poll.questions.all()[2]

        a2_1 = q2.answers.all()[0]
        a2_2 = q2.answers.all()[1]
        a2_3 = q2.answers.all()[2]

        a3_1 = q3.answers.all()[0]
        a3_2 = q3.answers.all()[1]
        a3_3 = q3.answers.all()[2]

        payload = {
            'poll_id': poll.id,
            'answers': [
                {'question_id': q1.id, 'text_answer': 'free text'},
                {'question_id': q2.id, 'answer_id': a2_1.id},
                {'question_id': q3.id, 'answer_ids': [a3_1.id, a3_3.id]},
            ]
        }

        response = self.client.post(f'/api/v1/pass_poll/', json.dumps(payload), content_type='application/json')

        self.assertEqual(201, response.status_code)

        self.assertEqual(3, UserAnswerModel.objects.filter(poll_id=poll.id).count())

        user_answer_q1 = UserAnswerModel.objects.get(poll_id=poll.id, question_id=q1.id)
        user_answer_q2 = UserAnswerModel.objects.get(poll_id=poll.id, question_id=q2.id)
        user_answer_q3 = UserAnswerModel.objects.get(poll_id=poll.id, question_id=q3.id)

        self.assertEqual('free text', user_answer_q1.text_answer)
        self.assertEqual(None, user_answer_q2.text_answer)
        self.assertEqual(None, user_answer_q3.text_answer)

        self.assertEqual(0, user_answer_q1.answers.all().count())
        self.assertEqual(1, user_answer_q2.answers.all().count())
        self.assertEqual(2, user_answer_q3.answers.all().count())
