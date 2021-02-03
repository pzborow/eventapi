import logging

from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.viewsets import GenericViewSet

from events.filters import MeetingFilter
from events.serializers import MeetingSerializer

from events.models import Meeting


class MeetingList(ListModelMixin, GenericViewSet):
    queryset = Meeting.objects.all()
    serializer_class = MeetingSerializer
    filterset_class = MeetingFilter
    # permission_classes = [IsPermitted]
    filter_fields = ("location_id", "day")
    search_fields = ("meeting_agenda", "event_name")
