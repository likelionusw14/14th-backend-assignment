from django.db import models


class Lion(models.Model):

    name = models.CharField(max_length=100)

    track = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.name