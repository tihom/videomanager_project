from .models import VideoMeta, OriginalVideo
from rest_framework import serializers


class VideoMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoMeta
        fields = ('youtube_url', 'title', 'description')


class OriginalVideoSerializer(serializers.HyperlinkedModelSerializer):
    youtube_url = serializers.CharField(source='video_meta.youtube_url', required=False)
    title = serializers.CharField(source='video_meta.title', required=False)
    description = serializers.CharField(source='video_meta.description', required=False)
    self_link = serializers.HyperlinkedIdentityField(view_name='originalvideo-detail')

    class Meta:
        model = OriginalVideo
        fields = ('sno', 'url', 'domain', 'subject', 'topic',
                  'tutorial', 'subject', 'priority', 'self_link',
                  'youtube_url', 'title', 'description',)
        extra_kwargs = {
            "tutorial": {"required": False}
        }

    def create(self, validated_data):
        video_meta_data = validated_data.pop('video_meta', None)
        if video_meta_data is not None:
            video_meta = VideoMeta.objects.create(**video_meta_data)
            validated_data.update({'video_meta': video_meta})

        original_video = OriginalVideo.objects.create(**validated_data)
        return original_video

    def update(self, instance, validated_data):
        video_meta_data = validated_data.pop('video_meta', None)
        if video_meta_data is not None:
            if hasattr(instance, 'video_meta'):
                video_meta = instance.video_meta
                super(OriginalVideoSerializer, self).update(video_meta, video_meta_data)
            else:
                video_meta = VideoMeta.objects.create(**video_meta_data)
                instance.video_meta = video_meta

        return super(OriginalVideoSerializer, self).update(instance, validated_data)
