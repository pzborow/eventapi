from django.db.models import Q
from events.filters import MeetingFilter
from events.models import Meeting
from events.permissions import IsPermitted
from events.serializers import MeetingCreateSerializer, MeetingListSerializer
from rest_framework.mixins import (CreateModelMixin, ListModelMixin,
                                   RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet


class MeetingList(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Meeting.objects.all()
    filterset_class = MeetingFilter
    permission_classes = [IsPermitted]
    filter_fields = ("location_id", "day")
    search_fields = ("meeting_agenda", "event_name")

    def get_serializer_class(self):
        if self.action in ("update", "create"):
            return MeetingCreateSerializer
        return MeetingListSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_superuser:
            return queryset
        queryset = queryset.filter(
            Q(owner=user) | Q(location__manager=user) | Q(participants=user)
        )
        return queryset
