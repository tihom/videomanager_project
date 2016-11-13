from django.db import models


class VideoMeta(models.Model):
    youtube_url = models.CharField(max_length=1024, unique=True)
    title = models.CharField(max_length=1024)
    description = models.TextField()

    def __str__(self):
        return self.youtube_url


class OriginalVideo(models.Model):
    sno = models.CharField(max_length=1024)
    url = models.CharField(max_length=1024)
    domain = models.CharField(max_length=1024)
    subject = models.CharField(max_length=1024)
    topic = models.CharField(max_length=1024)
    tutorial = models.CharField(max_length=1024)
    priority = models.IntegerField(blank=True)
    # has one video meta object
    video_meta = models.ForeignKey(VideoMeta, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.url