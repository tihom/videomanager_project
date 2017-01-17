# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    return render(request, "videomanager/index.html", {})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def sandbox(request):
    from django.http import HttpResponse
    from google.appengine.api import users
    user = users.get_current_user()

    if user:
        nickname = user.nickname()
        logout_url = users.create_logout_url('/')
        greeting = 'Welcome, {}! (<a href="{}">sign out</a>)'.format(
            nickname, logout_url)
    else:
        login_url = users.create_login_url('/')
        greeting = '<a href="{}">Sign in</a>'.format(login_url)

    return HttpResponse(greeting)
