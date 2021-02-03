# factories.py
import factory
from . import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.User

    first_name = factory.Sequence(lambda n: "Agent %03d" % n)
    username = factory.Sequence(lambda n: "Username %03d" % n)
    email = factory.Sequence(lambda n: "username_%03d@test.com" % n)