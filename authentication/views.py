from django.http import HttpResponse

from .google import google_login

def google_auth(request):
	_next = request.GET.get("next", "/")
	greeting = google_login(_next)
	return HttpResponse(greeting)
