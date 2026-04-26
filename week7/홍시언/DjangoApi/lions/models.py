from django.db import models

class Lion(models.Model):
    TRACK_CHOICES = [
        ('FE', 'Frontend'),
        ('BE', 'Backend'),
        ('DE', 'Design'),
        ('PM', 'Project Manager'),
    ]

    name = models.CharField(max_length=20)
    track = models.CharField(max_length=20, choices=TRACK_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.track}] {self.name}"