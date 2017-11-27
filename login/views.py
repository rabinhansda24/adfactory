from django.shortcuts import render
from home.models import Users
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LogInForm,UsersForm

def index(request):
    form = LogInForm()
    return render(request, 'login/login.html', {'form':form})



def login_post(request):
    form = LogInForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        userEmail = data['username']
        password = data['password']
        usertype = data['choice']
        user = Users.objects.get(userEmail=userEmail)

        if password == user.password:
            request.session['username'] = userEmail
            if usertype == 'blogger':
                return HttpResponseRedirect('/user-dashboard/')

            return HttpResponseRedirect('/advertiser-dashboard/')


        else:
            return HttpResponseRedirect('/login/')



def blogger_reg(request):

    form = UsersForm()
    return render(request, 'login/registration.html', {'form':form})


def blogger_post(request):
    form = UsersForm(request.POST)
    if form.is_valid():
        user = Users(userEmail=form.cleaned_data['userEmail'],
                     password=form.cleaned_data['password'],
                     name=form.cleaned_data['name'],
                     address=form.cleaned_data['address'],
                     phone=form.cleaned_data['phone'],
                     userType=form.cleaned_data['userType'],

                     )
        user.save()


    return HttpResponseRedirect('/login/')
