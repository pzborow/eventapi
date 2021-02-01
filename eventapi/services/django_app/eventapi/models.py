from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)


class Meeting(models.Model):
    event_name = models.CharField(max_length=100)
    meeting_agenda = models.TextField()
    # start_end = DateTimeRangeField()
    # participant = ManyToMany
    # location = ForeightField(null=True)
