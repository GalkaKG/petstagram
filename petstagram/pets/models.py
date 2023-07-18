from django.db import models
from django.template.defaultfilters import slugify

from petstagram.accounts.models import PetstagramUser


class Pet(models.Model):
    name = models.CharField(
        max_length=30,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    user = models.ForeignKey(to=PetstagramUser, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}--{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name
