from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from events.views import MeetingList
from rest_framework import routers
from tenants.views import TenantView, TenantViewRandomForm

router = routers.DefaultRouter()
router.register(r"events", MeetingList, basename="files")

urlpatterns = [path("", include(router.urls))]
