"""videomanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework.schemas import get_schema_view

from .views import home, home_files, sandbox
from volunteer.urls import urlpatterns as volunteer_urlpatterns
from translations.urls import urlpatterns as translations_urlpatterns

schema_view = get_schema_view(title="Video Manager API")
api_urls = volunteer_urlpatterns #+ translations_urlpatterns

urlpatterns = [
    url(r'^$', home),
    # url(r'^sandbox', sandbox),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
    url(r'^_/', include(api_urls)),
    url(r'^_/$', schema_view),
    url(r'^api-auth/', include('authentication.urls',
        namespace='rest_framework'))
]
