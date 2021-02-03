from datetime import timedelta

from django.contrib.auth import get_user_model
from drf_writable_nested import WritableNestedModelSerializer
from events.models import Location, Meeting
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class LocationSerializer(WritableNestedModelSerializer):
    manager = serializers.SlugRelatedField(
        slug_field="email", queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Location
        fields = "__all__"


class MeetingCreateSerializer(WritableNestedModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="email", queryset=get_user_model().objects.all()
    )
    participants = serializers.SlugRelatedField(
        many=True, slug_field="email", queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Meeting
        fields = "__all__"

    def validate_time_range(self, value):
        if value:
            if value.lower is None or value.upper is None:
                raise ValidationError(
                    "Meeting time need to has lower and upper value"
                )
            if value.upper - value.lower > timedelta(hours=8):
                raise ValidationError("Meeting is longer than 8h")
        return value or None


class MeetingListSerializer(WritableNestedModelSerializer):
    location = LocationSerializer()
    owner = serializers.SlugRelatedField(
        slug_field="email", queryset=get_user_model().objects.all()
    )
    participants = serializers.SlugRelatedField(
        many=True, slug_field="email", queryset=get_user_model().objects.all()
    )

    class Meta:
        model = Meeting
        fields = "__all__"
