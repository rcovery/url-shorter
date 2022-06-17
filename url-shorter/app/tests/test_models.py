from django.test import TestCase
from src.models import *

# Create your tests here.
class StoreTest(TestCase):
    def test_create_user(self):
        newUser = Users.object.create(
            email = 'rcoverybot@protonmail.com',
            username = 'rcovery',
            password = 'testpass'
        )

        self.assertEqual(newUser.username, 'rcovery')