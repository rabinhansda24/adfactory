from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from home.models import *
from .forms import *
# Create your views here.
def index(request):
    if request.session.has_key('admin'):
        adminEmail = request.session['admin']
        admin = AdminDetails.objects.get(adminEmail= adminEmail)
        return render(request, 'admindashboard/dashboard.html', {'admin':admin})
    else:
        return HttpResponseRedirect('/admin-login/')



def viewBloggers(request):
    if request.session.has_key('admin'):
        adminEmail = request.session['admin']
        admin = AdminDetails.objects.get(adminEmail= adminEmail)
        bloggers = Users.objects.filter(userType='blogger')
        return render(request, 'admindashboard/view_bloggers.html', {'bloggers': bloggers})
    else:
        return HttpResponseRedirect('/admin-login/')




def viewBloggerDetails(request, username):
    if request.session.has_key('admin'):
        adminEmail = request.session['admin']
        admin = AdminDetails.objects.get(adminEmail= adminEmail)
        blogger = Users.objects.get(userEmail=username)
        return render(request, 'admindashboard/blogger_details.html', {'blogger': blogger})
    else:
        return HttpResponseRedirect('/admin-login/')



def viewBlogs(request):
    if request.session.has_key('admin'):
        adminEmail = request.session['admin']
        admin = AdminDetails.objects.get(adminEmail= adminEmail)
        blogs = BlogDetails.objects.all()
        return render(request, 'admindashboard/blog.html', {'blogs': blogs })
    else:
        return HttpResponseRedirect('/admin-login/')



def viewBlogDetails(request, blogid):
    if request.session.has_key('admin'):
        blog = BlogDetails.objects.get(blogId=blogid)
        return render(request, 'admindashboard/blog_details.html', {'blog': blog})
    else:
        return HttpResponseRedirect('/admin-login/')



def viewAdvertisement(request):
    if request.session.has_key('admin'):
        ads = AdDetails.objects.all()
        return render(request, 'admindashboard/ads.html', {'ads':ads})
    else:
        return HttpResponseRedirect('/admin-login/')


def viewAdvertisementDetails(request, adid):
    if request.session.has_key('admin'):
        ad = AdDetails.objects.get(adId=adid)
        return render(request, 'admindashboard/addetails.html', {'ad':ad})
    else:
        return HttpResponseRedirect('/admin-login/')




def addCategory(request):
    if request.session.has_key('admin'):
        form = CategoryForm()
        category = Category.objects.all()
        return render(request, 'admindashboard/add_category.html', {'form':form, 'category':category})
    else:
        return HttpResponseRedirect('/admin-login/')


def addCategory_Post(request):
    if request.session.has_key('admin'):
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category(category=form.cleaned_data['category'])
            category.save()

        return HttpResponseRedirect('/admin-dashboard/addcategory/')
    else:
        return HttpResponseRedirect('/admin-login/')


def addMediatype(request):
    if request.session.has_key('admin'):
        form = MediaTypeForm()
        return render(request, 'admindashboard/add_mediatype.html', {'form':form})
    else:
        return HttpResponseRedirect('/admin-login/')


def addMediaType_post(request):
    if request.session.has_key('admin'):
        form = MediaTypeForm(request.POST)
        if form.is_valid():
            media = MediaType(mediaType=form.cleaned_data['mediaType'])
            media.save()
            return HttpResponseRedirect('/admin-dashboard/')

    else:
        return HttpResponseRedirect('/admin-login/')




def addPrice(request):
    if request.session.has_key('admin'):
        form = AddPriceForm()
        return render(request, 'admindashboard/add_price.html', {'form':form})
    else:
        return HttpResponseRedirect('/admin-login/')



def addPrice_post(request):
    if request.session.has_key('admin'):
        form = AddPriceForm(request.POST)
        if form.is_valid():
            price = Price(
                mediaType=form.cleaned_data['media'],
                price=form.cleaned_data['price'],
            )
            price.save()
            return HttpResponseRedirect('/admin-dashboard/')

        return render(request, 'admindashboard/add_mediatype.html', {'form':form})
    else:
        return HttpResponseRedirect('/admin-login/')


def viewAdvertiser(request):
    if request.session.has_key('admin'):
        advertiser = Users.objects.filter(userType='advertiser')
        return render(request, 'admindashboard/advertisers.html', {'advertisers':advertiser})
    else:
        return HttpResponseRedirect('/admin-login/')



def viewAdvertiserDetails(request, username):
    if request.session.has_key('admin'):
        advertiser = Users.objects.get(userEmail=username)
        return render(request, 'admindashboard/advertiser_details.html', {'advertiser': advertiser})
    else:
        return HttpResponseRedirect('/admin-login/')



def SuspendBlogger(request,username, status):
    if request.session.has_key('admin'):
        user = Users.objects.get(userEmail=username)
        user.status = status
        user.save()
        user1 = Users.objects.get(userEmail=username)
        return render(request, 'admindashboard/blogger_details.html', {'blogger': user1})
    else:
        return HttpResponseRedirect('/admin-login/')


def SuspendAdvertiser(request, username, status):
    if request.session.has_key('admin'):
        user = Users.objects.get(userEmail=username)
        user.status = status
        user.save()
        user1 = Users.objects.get(userEmail=username)
        return render(request, 'admindashboard/advertiser_details.html', {'blogger': user1})
    else:
        return HttpResponseRedirect('/admin-login/')



def logout(request):
    try:
        del request.session['admin']
        del request.session['username']
    except:
        pass


    return render(request, 'admindashboard/logout.html')
