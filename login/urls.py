from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [

    #admin urls

    url(r'^$', views.index, name='index'),
    url(r'^admin/$', views.adminlog, name='adminlog'),
    url(r'^student/$', views.studentlog, name='studentlog'),
    url(r'^admin/login$', views.adminlogin, name='adminlogin'),
    url(r'^admin/login/addstd$', views.addstd, name='addstd'),
    url(r'^admin/login/updatestd$', views.updatestd, name='updatestd'),
    url(r'^admin/login/fee$', views.fee, name='fee'),
    url(r'^admin/solve$', views.updatecompsol, name='updatecompsol'),
    url(r'^admin/feefetch$', views.feefetch, name='feefetch'),
    url(r'^admin/addstd$', views.addstddb, name='addstddb'),
    url(r'^admin/updatesearch$', views.upsearch, name='upsearch'),
    url(r'^admin/updatestd$', views.updatestddone, name='updatestddone'),
    url(r'^admin/login/addnoti$', views.addnoti, name='addnoti'),
    url(r'^admin/addnoti$', views.addnotification, name='addnotification'),
    url(r'^admin/logout$', views.logout, name='logout'),
    url(r'^admin/viewcomp$', views.viewcomp, name='viewcomp'),

    #stduent urls
    url(r'^std/login$', views.stdlogin, name='stdlogin'),
    url(r'^std/comp$', views.addcomp, name='addcomp'),
    url(r'^std/payment$', views.dopayment, name='dopayment'),
    url(r'^std/paymentdone$', views.donepayment, name='donepayment'),
    url(r'^std/addcomp$', views.addstdcomp, name='addstdcomp'),
    url(r'^std/logout$', views.stdlogout, name='stdlogout'),
    url(r'^std/viewcomp$', views.stdcomp, name='stdcomp'),
    url(r'^std/change$', views.stdchange, name='stdchange'),
    url(r'^std/changedone$', views.changedone, name='changedone'),
]
