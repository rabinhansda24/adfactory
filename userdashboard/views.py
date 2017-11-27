from django.shortcuts import render
from home.models import *
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    if request.session.has_key('username'):
        username=request.session['username']
        user=Users.objects.get(userEmail=username)
        return render(request, 'userdashboard/dash.html',{'user':user})
    else:
        return HttpResponseRedirect('/login/')


def bloger_profile(request):
    if request.session.has_key('username'):
        username=request.session['username']
        user=Users.objects.get(userEmail=username)
        return render(request, 'userdashboard/bloger_profile.html',{'user':user})
    else:
        return HttpResponseRedirect('/login/')


def blog_details(request):
    if request.session.has_key('username'):
        username=request.session['username']
        blogs = BlogDetails.objects.all()
        return render(request, 'userdashboard/blog_details.html',{'blogs':blogs})
    else:
        return HttpResponseRedirect('/login/')

def add_blog_details(request):
    blog = BlogDetailsForms()
    return render(request,'userdashboard/blog_details_post.html',{'blog':blog})

def blog_details_post(request):
    blog = BlogDetails.objects.all()
    form = add_blog_details(request.POST)
    email = request.session['username']
    if form.is_valid():
        if blog.exists():
            last = BlogDetails.objects.latest('blogId')
            newBlog = BlogDetails(
                blogId=last.blogId + 1,
                userEmail= email,
                url=form.cleaned_data['url'],
                type=form.cleaned_data['type'],
                description=form.cleaned_data['description']
            )

            newBlog.save()
        else:
            newBlog = BlogDetails(
                blogId=1012101,
                userEmail=email,
                url=form.cleaned_data['url'],
                type=form.cleaned_data['type'],
                description=form.cleaned_data['description']
            )

            newBlog.save()


    return HttpResponseRedirect('/userdashboard/')



def blog_api(request):
    if request.session.has_key('username'):
        username=request.session['username']
        user=Users.objects.get(userEmail=username)
        return render(request, 'userdashboard/blog_api.html',{'user':user})
    else:
        return HttpResponseRedirect('/login/')


def bank_details(request):
    if request.session.has_key('username'):
       # username=request.session['username']
        #user=Users.objects.get(userEmail=username)
        form=BankDetailsForms()
        return render(request, 'userdashboard/bank_details.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')


def BankDetailPost(request):
    form=BankDetailsForms(request.POST)
    if form.is_valid():
        bank=BankDetails(
            accNo=form.cleaned_data['accNo'],
            bankName=form.cleaned_data['bankName'],
            branchName=form.cleaned_data['branchName'],
            ifsc=form.cleaned_data['ifsc'],)


        bank.save()


    return HttpResponseRedirect('/user-dashboard/')



def bloger_earning(request):
    if request.session.has_key('username'):
        username=request.session['username']
        user=Users.objects.get(userEmail=username)
        return render(request, 'userdashboard/bloger_earning.html',{'user':user})
    else:
        return HttpResponseRedirect('/login/')


def logout(request):
    try:
        del request.session['username']
    except:
        pass


    return render(request, 'userdashboard/logout.html')


