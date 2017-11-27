from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name="advertiserdashboard"),
    url(r'^advertiser_profile/$', views.advertiser_profile, name="advertiser_profile"),
    url(r'^advertise_details/$', views.advertise_details, name="advertise_details"),
    url(r'^add_advertise/$', views.add_advertise, name="add_advertise"),
    url(r'^add_advertise/ad_post/$', views.add_advertise_post, name="add_advertise_post"),
    url(r'^bank_details/$', views.bank_details, name="bank_details"),
    url(r'^ad_payments/$', views.ad_payments, name="ad_payments"),
    url(r'^logout/$', views.logout, name="logout"),

]