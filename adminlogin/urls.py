from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name="adminlogin"),
    url(r'^login/$', views.login_post, name='adminlogin_post'),

]