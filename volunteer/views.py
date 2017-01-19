from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer
from .authentication import google_auth

def google_auth_view(request):
	greeting = google_auth()
	return HttpResponse(greeting)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
