from django.forms import ModelForm
from django import forms
from home.models import Users


class LogInForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(max_length=100, label='Email')

    usertype = (
        ('blogger', 'Blogger'),
        ('advertiser','Advertiser'),
    )
    choice = forms.ChoiceField(choices=usertype, label= 'User type')
    class Meta:
        model = Users
        fields = ['choice','username','password']


class UsersForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    usertype = (
        ('blogger', 'Blogger'),
        ('advertiser', 'Advertiser'),
    )
    userType = forms.ChoiceField(choices=usertype, label='Select User Typr')
    class Meta:
        model = Users
        fields = ['userEmail','password','name','address','phone','userType']
