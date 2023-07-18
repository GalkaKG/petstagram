from django.db import models
from django.contrib.auth.models import AbstractUser


class PetstagramUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    profile_picture = models.URLField()
    gender = models.CharField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
