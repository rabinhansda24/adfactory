from django.shortcuts import render
from home.models import *
from django.http import HttpResponseRedirect
from .form import *



# Create your views here.
def index(request):
    if request.session.has_key('username'):
        username=request.session['username']
        user=Users.objects.get(userEmail=username)
        return render(request, 'advertiserdashboard/dashboard.html', {'user': user})
    else:
        return HttpResponseRedirect('/login/')


def advertiser_profile(request):
    if request.session.has_key('username'):
        username=request.session['username']
        user=Users.objects.get(userEmail=username)
        return render(request, 'advertiserdashboard/advertiser_profile.html',{'user':user})
    else:
        return HttpResponseRedirect('/login/')


def advertise_details(request):
    if request.session.has_key('username'):
        username=request.session['username']
        ads = AdDetails.objects.get()
        return render(request, 'advertiserdashboard/advertise_details.html',{'user':user})
    else:
        return HttpResponseRedirect('/login/')

def add_advertise(request):
    form=AddAdvertiseForm()
    return render(request,'advertiserdashboard/add_advertise.html',{'form':form})

def add_advertise_post(request):
    ad=AdDetails.objects.all()
    form=AddAdvertiseForm(request.POST,request.FILES)
    email=request.session['username']
    if form.is_valid():
        if ad.exists():
            last = AdDetails.objects.latest('adId')
            newAd = AdDetails(
                adId = last.adId + '1',
                category = 'demo_category',
                adTitle = form.cleaned_data['adTitle'],
                adDescription = form.cleaned_data['adDescription'],
                mediaLink = form.cleaned_data['mediaLink'],
                mediaType = 'image',

            )
            newAd.save()
        else:
            newAd = AdDetails(
                adId=121101,
                category='demo_category',
                adTitle=form.cleaned_data['adTitle'],
                adDescription=form.cleaned_data['adDescription'],
                mediaLink=form.cleaned_data['mediaLink'],
                mediaType='image',

            )
            newAd.save()


def bank_details(request):
    if request.session.has_key('username'):
        username=request.session['username']
        user=Users.objects.get(userEmail=username)
        return render(request, 'advertiserdashboard/bank_details.html',{'user':user})
    else:
        return HttpResponseRedirect('/login/')


def ad_payments(request):
    if request.session.has_key('username'):
        username = request.session['username']
        user = Users.objects.get(userEmail=username)
        return render(request, 'advertiserdashboard/ad_payments.html', {'user': user})
    else:
        return HttpResponseRedirect('/login/')


def logout(request):
    try:
        del request.session['username']
    except:
        pass


    return render(request, 'advertiserdashboard/logout.html')



