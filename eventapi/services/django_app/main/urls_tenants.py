from tenants.views import TenantView, TenantViewRandomForm
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from events.views import MeetingList

router = routers.DefaultRouter()
router.register(r"events", MeetingList, basename="files")

urlpatterns = [
    path("", include(router.urls)),
]
