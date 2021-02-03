from django.contrib.auth.models import AbstractUser
from timezone_field import TimeZoneField


class User(AbstractUser):
    time_zone = TimeZoneField(default="UTC")
