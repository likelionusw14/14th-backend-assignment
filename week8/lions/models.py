from django.db import models


class Lion(models.Model):
    TRACK_CHOICES = [
        ('Django', 'Django'),
        ('SpringBoot', 'SpringBoot'),
        ('Frontend', 'Frontend'),
    ]

    name = models.CharField(max_length=100)
    track = models.CharField(max_length=100, choices=TRACK_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # 최신순 정렬

    def __str__(self):
        return f'{self.name} ({self.track})'
