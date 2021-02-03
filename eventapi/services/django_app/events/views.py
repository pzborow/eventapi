import logging

from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.viewsets import GenericViewSet


logger = logging.getLogger(__name__)


class FileList(ListModelMixin, GenericViewSet):
    queryset = Meeting.objects.all()
    serializer_class = FileSerializer
    filterset_class = FileFilter
    permission_classes = [IsPermitted]
    filter_fields = ("id", "real_name", "operation_status")
    ordering_fields = ("id", "real_name", "operation_status")
    search_fields = ("id", "real_name")
