from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    username = models.CharField(max_length=256, unique=True)
    avatar = models.URLField(max_length=500, blank=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    date_joined = models.DateTimeField(null=True)

    def __str__(self):
        return self.username

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return None

