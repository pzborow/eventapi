import logging

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.viewsets import GenericViewSet

from events.filters import MeetingFilter
from events.permissions import IsPermitted
from events.serializers import MeetingListSerializer, MeetingCreateSerializer

from events.models import Meeting


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
            Q(owner=user) |
            Q(location__manager=user) |
            Q(participants=user)
        )
        return queryset
