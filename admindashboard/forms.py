from django.forms import ModelForm
from django import forms
from home.models import *


class AdminLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=100,label='Email')
    class Meta:
        model = AdminDetails
        fields = ['username','password']



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']



class MediaTypeForm(forms.ModelForm):
    class Meta:
        model = MediaType
        fields = ['mediaType']


class AddPriceForm(forms.ModelForm):
    media = forms.ModelChoiceField(MediaType.objects.all(), label='Select Media type')
    class Meta:
        model = Price
        fields = ['media', 'price']







