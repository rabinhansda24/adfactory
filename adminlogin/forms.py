from django.forms import ModelForm
from django import forms
from home.models import AdminDetails


class LogInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=100, label='Email')
    class Meta:
        model = AdminDetails
        fields = ['username','password']

