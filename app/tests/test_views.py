from django.test import TestCase, Client

class IndexTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_base_index_view(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'app/index.html')

    def test_post_index(self):
        response = self.client.post('/', { 'url': 'https://google.com' })

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['name'], None)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_post_index_with_name(self):
        data = { 'url': 'https://google.com', 'name': 'rcovery' }
        response = self.client.post('/', data)

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.context['name'], None)
        self.assertEqual(len(data['name']), 7)
        self.assertEqual(response.context['name'], 'rcovery')
        self.assertTemplateUsed(response, 'app/index.html')

    def test_post_index_with_same_name(self):
        self.client.post('/', { 'url': 'https://google.com', 'name': 'rcovery' })

        response = self.client.post('/', { 'url': 'https://google.com', 'name': 'rcovery' })

        self.assertEqual(response.status_code, 200)

    def test_post_index_invalid_url(self):
        response = self.client.post('/', { 'url': 'https://teste2.com', 'name': 'rcovery' })

        self.assertEqual(response.status_code, 200)

    def test_get_track(self):
        response = self.client.get('/rcovery')

        self.assertEqual(response.status_code, 200)
