from django.http import HttpResponse
from django.shortcuts import redirect

from .google_authentication import GoogleAuthentication, GoogleAuthException

def login(request):
	_next = request.GET.get("next", "/")
	try:
		greeting = GoogleAuthentication().auth_greeting(_next)
		return HttpResponse(greeting)
	except GoogleAuthException, e:
		return HttpResponse(str(e))
		

def logout(request):
	_next = request.GET.get("next", "/")
	try:
		greeting = GoogleAuthentication().auth_greeting(_next)
		return HttpResponse(greeting)
	except GoogleAuthException, e:
		return HttpResponse(str(e))
		

	
