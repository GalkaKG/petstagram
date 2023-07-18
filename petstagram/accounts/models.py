from django.db import models
from django.contrib.auth.models import AbstractUser

from petstagram.common.models import Like


class PetstagramUser(AbstractUser):
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do_Not_Snow', 'Do_Not_Show')
    )

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_picture = models.URLField(
        null=True,
        blank=True
    )
    gender = models.CharField(
        max_length=11,
        choices=GENDERS,
        null=True,
        blank=True,
    )

    likes = models.ManyToManyField(Like, related_name='users')

    def get_user_name(self):
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name or self.last_name:
            return self.first_name or self.last_name
        else:
            return self.username

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
