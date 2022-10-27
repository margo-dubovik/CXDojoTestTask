from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    username = models.CharField(max_length=256, unique=True)
    avatar = models.ImageField(upload_to='user_image', blank=True)

    def __str__(self):
        return self.username

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        else:
            return None

