# ref: http://www.django-rest-framework.org/api-guide/routers/
from rest_framework.routers import DefaultRouter, SimpleRouter

class VideoRouter(SimpleRouter):
    """
    Custom router for user related api endpoints
    """