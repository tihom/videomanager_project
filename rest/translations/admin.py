from django.contrib import admin

from .models import VideoMeta, OriginalVideo

admin.site.register(VideoMeta)
admin.site.register(OriginalVideo)
