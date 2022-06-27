from django.test import TestCase, Client

class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_base_index_view(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'app/index.html')

    def test_post_index_template(self):
        response = self.client.post('/', { 'url': 'https://teste.com' })

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['name'], None)
        self.assertTemplateUsed(response, 'app/index.html')
