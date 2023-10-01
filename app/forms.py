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
    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False

    class Meta:
        model = Urls
        fields = [
            'url',
            'name'
        ]