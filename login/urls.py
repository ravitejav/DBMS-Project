from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/$', views.adminlog, name='adminlog'),
    url(r'^student/$', views.studentlog, name='studentlog'),
    url(r'^admin/login$', views.adminlogin, name='adminlogin'),
]
