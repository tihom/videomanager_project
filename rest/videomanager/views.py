# -*- coding: utf-8 -*-
from django.shortcuts import render

def home(request):
    return render(request, "videomanager/index.html", {})


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")

def sandbox(request):
    greeting = "test stuff"
    return HttpResponse(greeting)
