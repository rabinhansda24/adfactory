from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name="userdashboard"),
    url(r'^bloger_profile/$', views.bloger_profile, name="bloger_profile"),
    url(r'^blog_details/$', views.blog_details, name="blog_details"),
    url(r'^addblog/$', views.add_blog_details, name="add_blog_details"),
    url(r'^addblog/post/$', views.blog_details_post, name="blog_details_post"),
    url(r'^blog_api/$', views.blog_api, name="blog_api"),
    url(r'^bank_details/$', views.bank_details, name="bank_details"),
    url(r'^bank_details/post/$', views.BankDetailPost, name="BankDetailPost"),
    url(r'^logout/$', views.logout, name="logout"),
]