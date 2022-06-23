from django.test import TestCase, Client

class UrlsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_url(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_404_url(self):
        response = self.client.get('/404')

        self.assertEqual(response.status_code, 404)