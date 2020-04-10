from django.contrib.auth.models import User
from django import forms
from .models import Notes


class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description', 'user']
