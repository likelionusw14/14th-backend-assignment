from django.db import models

class Lions(models.Model):
    TRACK_CHOICES = [
        ('Frontend', 'Frontend'),
        ('Django', 'Django'),
        ('SpringBoot', 'SpringBoot'),
    ]
    name = models.CharField(max_length=30, blank=False, default='')
    track = models.CharField(
        max_length=30,
        choices=TRACK_CHOICES,
        default ='backend'
        )
    created_at = models.DateTimeField(
        auto_now_add = True
    )

