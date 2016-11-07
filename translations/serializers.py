from .models import VideoMeta, OriginalVideo
from rest_framework import serializers


class VideoMetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoMeta
        fields = ('youtube_url', 'title', 'description')


class OriginalVideoSerializer(serializers.HyperlinkedModelSerializer):
    video_meta = VideoMetaSerializer()

    class Meta:
        model = OriginalVideo
        fields = ('sno', 'url', 'domain', 'subject', 'topic',
                  'tutorial', 'subject', 'priority', 'video_meta')

    def create(self, validated_data):
        video_meta_data = validated_data.pop('video_meta')
        video_meta = VideoMeta.objects.create(**video_meta_data)

        original_video = OriginalVideo.objects.create(video_meta=video_meta,
                                                      **validated_data)

        return original_video

    # Update will not work with nested atributes see
    # http://stackoverflow.com/questions/27434593/django-rest-framework-3-0-create-or-update-in-nested-serializer
    # it can be overwritten to work with nested attributes but a bit more involved
    # for now assuming update will be done separately for the relted video meta
    # will need to use PATCH for updating OriginalVideo as PUT expects all the fields specified in the serilizer