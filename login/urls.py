from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/$', views.adminlog, name='adminlog'),
    url(r'^student/$', views.studentlog, name='studentlog'),
    url(r'^admin/login$', views.adminlogin, name='adminlogin'),
    url(r'^admin/login/addstd', views.addstd, name='addstd'),
    url(r'^admin/login/updatestd', views.updatestd, name='updatestd'),
    url(r'^admin/login/fee', views.fee, name='fee'),
    url(r'^admin/feefetch', views.feefetch, name='feefetch'),
    url(r'^admin/addstd', views.addstddb, name='addstddb'),
    url(r'^admin/updatesearch', views.upsearch, name='upsearch'),
    url(r'^admin/updatestd', views.updatestddone, name='updatestddone'),
    url(r'^admin/login/addnoti', views.addnoti, name='addnoti'),
    url(r'^admin/addnoti', views.addnotification, name='addnotification'),
    url(r'^admin/logout', views.logout, name='logout'),
]
