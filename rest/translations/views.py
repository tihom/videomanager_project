from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .models import OriginalVideo, VideoMeta
from .serializers import OriginalVideoSerializer, VideoMetaSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the translations index.")


class OriginalVideoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows original videos to be viewed or edited.
    """
    queryset = OriginalVideo.objects.all()
    serializer_class = OriginalVideoSerializer


class VideoMetaViewSet(viewsets.ModelViewSet):
    queryset = VideoMeta.objects.all()
    serializer_class =  VideoMetaSerializer