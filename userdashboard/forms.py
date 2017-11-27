from django.forms import ModelForm
from django import forms
from home.models import *


class BlogDetailsForms(forms.ModelForm):
    class Meta:
        model=BlogDetails
        fields=['url','type','description']


class BankDetailsForms(forms.ModelForm):
    class Meta:
        model=BankDetails
        fields=['accNo','bankName','branchName','ifsc']