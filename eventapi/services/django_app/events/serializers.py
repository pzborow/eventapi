from pathlib import Path

from django.contrib.auth import get_user_model
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer

from events.models import Meeting, Location


class LocationSerializer(WritableNestedModelSerializer):
    manager = serializers.SlugRelatedField(
        slug_field='email',
        queryset=get_user_model().objects.all()
    )
    class Meta:
        model = Location
        fields = "__all__"


class MeetingSerializer(WritableNestedModelSerializer):
    location = LocationSerializer()
    owner = serializers.SlugRelatedField(
        slug_field='email',
        queryset=get_user_model().objects.all()
    )
    participants = serializers.SlugRelatedField(
        many=True,
        slug_field='email',
        queryset=get_user_model().objects.all()
    )
    class Meta:
        model = Meeting
        fields = "__all__"

    def xxxxupdate(self, instance, validated_data):
        __import__('ipdb').set_trace()
        location = validated_data.pop('location')
        super().update(instance, validated_data)
        if location is None:
            instance.location = Location.objects.get(pk=location["pk"])
        instance.save()


#m = Meeting.objects.filter(time_range__overlap=('2021-2-2 17:33:00', '2021-2-2 17:34:00')).first()