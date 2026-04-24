from django.db import models


class Lion(models.Model):
    name = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.track})'
