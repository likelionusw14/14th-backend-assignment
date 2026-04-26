from django.db import models

class Lion(models.Model):
    TRACK_CHOICES = [
        ('기획/디자인', '기획/디자인'),
        ('프론트엔드', '프론트엔드'),
        ('백엔드', '백엔드'),
    ]
    
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=20, choices=TRACK_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
