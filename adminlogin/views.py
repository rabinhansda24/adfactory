from django.shortcuts import render
from home.models import AdminDetails
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LogInForm

def index(request):
    form = LogInForm()
    return render(request, 'adminlogin/login.html', {'form':form})



def login_post(request):
    form = LogInForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        adminemail = data['username']
        password = data['password']

        user = AdminDetails.objects.get(adminEmail=adminemail)

        if password == user.password:
            request.session['admin'] = adminemail
            return HttpResponseRedirect('/admin-dashboard/')

        else:
            return HttpResponseRedirect('/admin-login/')

    else:
        return HttpResponseRedirect('/admin-login/')


