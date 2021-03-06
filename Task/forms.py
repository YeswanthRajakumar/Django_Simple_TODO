from django.contrib.auth.models import User
from django import forms
from .models import Notes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
