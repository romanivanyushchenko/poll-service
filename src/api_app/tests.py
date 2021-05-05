from rest_framework.test import APITestCase
from model_bakery import baker

class SomeTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        baker.make('api_app.PollModel', make_m2m=True, _quantity=7)

    def test_get_poll_list(self):
        response = self.client.get('/api/v1/polls/', {'limit': 5})
        self.assertEqual(200, response.status_code)
        self.assertEqual(7, response.data['count'])
        self.assertEqual('http://testserver/api/v1/polls/?limit=5&offset=5', response.data['next'])
        self.assertEqual(None, response.data['previous'])
        self.assertEqual(5, len(response.data['results']))
        self.assertIn('name', response.data['results'][0])
        self.assertIn('start_date', response.data['results'][0])
        self.assertIn('end_date', response.data['results'][0])
        self.assertIn('description', response.data['results'][0])
        self.assertIn('questions', response.data['results'][0])
