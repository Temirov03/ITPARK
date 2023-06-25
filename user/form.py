from django import forms
from .models import NewUser
from django.forms import ModelForm


class NewUserForm(ModelForm):
    class Meta:
        model = NewUser
        fields = '__all__'
