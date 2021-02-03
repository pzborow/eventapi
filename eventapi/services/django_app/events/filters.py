import datetime
from django_filters import rest_framework as filters
from psycopg2.extras import DateTimeTZRange
from events.models import Meeting


class MeetingFilter(filters.FilterSet):
    day = filters.DateFilter(method='day_filter')
    class Meta:
        model = Meeting
        fields = [
            "location_id",
            "event_name",
            "meeting_agenda",
        ]

    def day_filter(self, queryset, name, value):
        if value is not None:
            range = DateTimeTZRange(
                value,
                value + datetime.timedelta(days=1),
                "[)"
            )
            queryset = queryset.filter(
                time_range__overlap=range
            )
        return queryset