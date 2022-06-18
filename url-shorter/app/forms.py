from django.forms import ModelForm
from src.models import Users

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = [
            'username',
            'email',
            'password'
        ]