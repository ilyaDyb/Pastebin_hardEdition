from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    subscribers = models.ManyToManyField('self', symmetrical=False, related_name='subscribed_to')

    class Meta:
        db_table = "Users"

