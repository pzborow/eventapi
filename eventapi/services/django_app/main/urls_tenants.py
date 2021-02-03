from django.urls import include, path
from events.views import MeetingList
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"events", MeetingList, basename="files")

urlpatterns = [path("", include(router.urls))]
