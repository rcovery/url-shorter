from django.test import TestCase
from app.forms import *

# Create your tests here.
class FormsTest(TestCase):
    def test_fail_create_userform(self):
        data = { 'username': 'Ryanzinho', 'password': '121212121'}
        form = UserForm(data)

        self.assertFalse(form.is_valid())

    def test_create_userform(self):
        data = { 'username': 'Ryanzinho', 'email': 'aoiewoai@eoaiwoeiwa.com', 'password': '121212121'}
        form = UserForm(data)

        self.assertTrue(form.is_valid())