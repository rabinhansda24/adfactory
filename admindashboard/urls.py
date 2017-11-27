from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name="admin_dash"),
    url(r'^bloggers/$', views.viewBloggers, name="viewbloggers"),
    url(r'^bloggers/(?P<username>[\w.@+-]+)/$', views.viewBloggerDetails, name="viewbloggers"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^blogs/$', views.viewBlogs, name="blogdetails"),
    url(r'^blogs/(?P<blogid>\d+)/$', views.viewBlogDetails, name="blogdetails"),
    url(r'^ads/$', views.viewAdvertisement, name="ads"),
    url(r'^ads/(?P<adid>\d+)/$', views.viewAdvertisementDetails, name="ad_details"),
    url(r'^addcategory/$', views.addCategory, name="addcategory"),
    url(r'^addcategory/post/$', views.addCategory_Post, name="addcategorypost"),
    url(r'^add_mediatype/$', views.addMediatype, name="addmedia"),
    url(r'^add_mediatype/post/$', views.addMediaType_post, name="addmediapost"),
    url(r'^add_price/$', views.addPrice, name="addprice"),
    url(r'^add_price/post/$', views.addPrice_post, name="addpricepost"),
    url(r'^advertiser/$', views.viewAdvertiser, name="advertisers"),
    url(r'^advertiser/(?P<username>[\w.@+-]+)/$', views.viewAdvertiserDetails, name="viewadvertisersdetails"),
    url(r'^bloggers/(?P<username>[\w.@+-]+)/(?P<status>[\w.@+-]+)/$', views.SuspendBlogger, name="suspendblogger"),
    url(r'^advertiser/(?P<username>[\w.@+-]+)/(?P<status>[\w.@+-]+)/$', views.SuspendAdvertiser, name="viewadvertisersdetails"),

]