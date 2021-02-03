import datetime

import factory
from users.factories import UserFactory

from .models import Location, Meeting


class LocationFactory(factory.DjangoModelFactory):
    name = factory.Faker("name")
    address = factory.Faker("address")
    manager = factory.SubFactory(UserFactory)

    class Meta:
        model = Location


class MeetingFactory(factory.DjangoModelFactory):
    event_name = factory.Faker("sentence", nb_words=4)
    meeting_agenda = factory.Faker("sentence")
    location = factory.SubFactory(LocationFactory)
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = Meeting

    @factory.lazy_attribute
    def time_range(self):
        from django.utils import timezone
        from psycopg2.extras import DateRange, DateTimeTZRange

        now = timezone.now()
        start = now - datetime.timedelta(hours=1)
        stop = now + datetime.timedelta(hours=1)
        timeslot = DateTimeTZRange(start, stop, "[]")
        return timeslot
