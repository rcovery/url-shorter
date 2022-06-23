from django.test import TestCase, Client

class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'app/index.html')