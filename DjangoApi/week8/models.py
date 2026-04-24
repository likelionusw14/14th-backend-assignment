from django.db import models

class Lion(models.Model):
    TRACK_CHOICES = [
        ('Django', 'Django'),
        ('SpringBoot', 'SpringBoot'),
        ('Frontend', 'Frontend'),
        ('Design', 'Design'),
    ]

    name = models.CharField(max_length=20)
    track = models.CharField(max_length=20, choices=TRACK_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'week8_lion'

    def __str__(self):
        return f"{self.name} ({self.track})"
