# products/models.py
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self): return self.name

class Lion(models.Model):
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    # N:M 관계 (Tag) 
    tags = models.ManyToManyField(Tag, related_name='lions')

    class Meta:
        ordering = ['-created_at'] # [지침] 기본 정렬 지정

class Task(models.Model):
    # 1:N 관계 (Lion) 
    lion = models.ForeignKey(Lion, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)

class LionProfile(models.Model):
    # 1:1 관계 (Lion) 
    lion = models.OneToOneField(Lion, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)