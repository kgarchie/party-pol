# from django.contrib.auth.models import User
from django import forms
from .models import CustomUser


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password',
        )