from django.forms import ModelForm
from django import forms
from home.models import *

class AddAdvertiseForm(forms.ModelForm):
    class Meta:
        model=AdDetails
        fields=['adTitle','adDescription','mediaLink']



