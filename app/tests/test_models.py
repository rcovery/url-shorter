from django.test import TestCase
from src.models import *

# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
        self.newUser = Users.objects.create(
            email = 'rcoverybot@protonmail.com',
            username = 'rcovery',
            password = 'testpass'
        )

        self.newUrl = None

    def test_create_user(self):
        self.assertTrue(self.newUser.id)

    def test_update_user_email(self):
        modUser = self.newUser
        modUser.email = 'test@yahoo.com'
        modUser.save()

        self.assertNotEqual(modUser.email, 'rcoverybot@protonmail.com')

    def test_create_url(self):
        self.newUrl = Urls.objects.create(
            url = 'https://test.com/',
            name = 'rcovery',
            user = self.newUser
        )

        self.assertEqual(self.newUrl.name, 'rcovery')

    def test_create_url_with_same_name(self):
        self.newUrl = Urls.objects.create(
            url = 'https://testagrande.com/',
            name = 'rcovery',
            user = self.newUser
        )

        self.assertEqual(self.newUrl.name, 'rcovery')