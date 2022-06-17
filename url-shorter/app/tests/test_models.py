from django.test import TestCase
from src.models import *

# Create your tests here.
class UrlShorterTest(TestCase):
    def setUp(self):
        self.newUser = Users.objects.create(
            email = 'rcoverybot@protonmail.com',
            username = 'rcovery',
            password = 'testpass'
        )

    def test_create_user(self):
        self.assertEqual(self.newUser.id, 1)

    def test_update_user_email(self):
        modUser = self.newUser
        modUser.email = 'test@yahoo.com'
        modUser.save()

        self.assertNotEqual(modUser.email, 'rcoverybot@protonmail.com')