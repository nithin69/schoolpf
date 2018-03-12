from django.conf.urls import patterns, url, include
from myproject import models, views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
		url(r'^form/$', views.form, name='form'),
		url(r'^fm16/$', views.fm16, name='fm16'),
		#url(r'^about/$', views.about, name='about'),
		#url(r'^contactus/$', views.contact_form, name='contact_form'),
		
)
