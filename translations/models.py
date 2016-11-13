from django.db import models


class VideoMeta(models.Model):
    youtube_url = models.CharField(unique=True, max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.youtube_url


class OriginalVideo(models.Model):
    sno = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    tutorial = models.CharField(max_length=255)
    priority = models.IntegerField(blank=True)
    # has one video meta object
    video_meta = models.ForeignKey(VideoMeta, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.url
