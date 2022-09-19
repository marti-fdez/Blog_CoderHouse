from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Perfiles.models import Avatar

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username']:
            self.fields[fieldname].help_text = None  # type: ignore

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']

class AvatarCreateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']