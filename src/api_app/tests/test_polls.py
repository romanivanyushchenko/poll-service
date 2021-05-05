from rest_framework.test import APITestCase
from model_bakery import baker

from api_app.tests.base import create_test_poll


class PollsTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.poll = create_test_poll()
        baker.make('api_app.PollModel', make_m2m=True, _quantity=6)

    def test_get_poll_list(self):
        response = self.client.get('/api/v1/polls/', {'limit': 5})
        self.assertEqual(200, response.status_code)
        self.assertEqual(7, response.data['count'])
        self.assertEqual('http://testserver/api/v1/polls/?limit=5&offset=5', response.data['next'])
        self.assertEqual(None, response.data['previous'])
        self.assertEqual(5, len(response.data['results']))

        # test poll fields
        self.assertIn('id', response.data['results'][0])
        self.assertIn('name', response.data['results'][0])
        self.assertIn('start_date', response.data['results'][0])
        self.assertIn('end_date', response.data['results'][0])
        self.assertIn('description', response.data['results'][0])
        self.assertIn('questions', response.data['results'][0])

        # test question fields
        self.assertIn('id', response.data['results'][0]['questions'][0])
        self.assertIn('text', response.data['results'][0]['questions'][0])
        self.assertIn('type', response.data['results'][0]['questions'][0])
        self.assertIn('answers', response.data['results'][0]['questions'][0])

        # test answer fields
        self.assertEqual(0, len(response.data['results'][0]['questions'][0]['answers']))

        self.assertIn('id', response.data['results'][0]['questions'][1]['answers'][0])
        self.assertIn('name', response.data['results'][0]['questions'][1]['answers'][0])
        self.assertIn('value', response.data['results'][0]['questions'][1]['answers'][0])
