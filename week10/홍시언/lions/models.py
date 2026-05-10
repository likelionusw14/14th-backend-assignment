from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Lion(models.Model):
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='lions')

    class Meta:
        ordering = ['-created_at'] # 최신순 정렬

    def __str__(self):
        return self.name

class LionProfile(models.Model):
    lion = models.OneToOneField(Lion, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, default="자기소개가 없습니다.")

class Task(models.Model):
    lion = models.ForeignKey(Lion, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']