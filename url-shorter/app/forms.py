from django.forms import ModelForm
from src.models import *

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = [
            'username',
            'email',
            'password'
        ]

class UrlForm(ModelForm):
    class Meta:
        model = Urls
        fields = [
            'url',
        ]