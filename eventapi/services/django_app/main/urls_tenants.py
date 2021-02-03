from tenants.views import TenantView, TenantViewRandomForm
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from events.views import MeetingList

urlpatterns = [
    path('', MeetingList.as_view({'get': 'list'}), name="index"),
    ]
