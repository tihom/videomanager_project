from django.conf.urls import url
from .google_authentication import GoogleAuthentication

# kludge as cant figure out how to redirect
if GoogleAuthentication().is_valid():
	from . import views
	urlpatterns = [
	    url(r'^login/$', views.login, name='login'),
	    url(r'^logout/$', views.logout, name='logout'),
	]
else:
	from django.contrib.auth import views
	template_name = {'template_name': 'rest_framework/login.html'}
	app_name = 'rest_framework'
	urlpatterns = [
	    url(r'^login/$', views.login, template_name, name='login'),
	    url(r'^logout/$', views.logout, template_name, name='logout'),
	]