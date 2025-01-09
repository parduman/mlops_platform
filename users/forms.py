# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    invite_code = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'invite_code']
