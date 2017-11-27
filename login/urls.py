from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.index, name="loginindex"),
    url(r'^registration/$', views.blogger_reg, name='blogger_reg'),
    url(r'^registration/post/$', views.blogger_post, name='blloger_post'),
    url(r'^login/$', views.login_post, name='login_post'),

]