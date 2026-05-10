from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    title = models.CharField(max_length=200)
    content = models.TextField()
    is_published = models.BooleanField(default=False)
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Create your models here.
# products/models.py
from django.db import models

class Lion(models.Model):
    TRACK_CHOICES = [
        ('Frontend', '프론트엔드'),
        ('Backend', '백엔드'),
        ('Design', '기획/디자인'),
    ]
    name = models.CharField(max_length=100) #
    track = models.CharField(max_length=20, choices=TRACK_CHOICES) #
    created_at = models.DateTimeField(auto_now_add=True) #

    def __str__(self):
        return f"[{self.track}] {self.name}"