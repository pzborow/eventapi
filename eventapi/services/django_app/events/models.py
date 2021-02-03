from django.conf import settings
from django.contrib.postgres.fields import DateTimeRangeField
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )


class Meeting(models.Model):
    event_name = models.CharField(max_length=100)
    meeting_agenda = models.TextField()
    time_range = DateTimeRangeField()
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="participate_meetings"
    )
    location = models.ForeignKey(
        Location, null=True, on_delete=models.SET_NULL
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="own_meetings",
    )
