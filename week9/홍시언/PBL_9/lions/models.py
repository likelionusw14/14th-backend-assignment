from django.db import models

class Lion(models.Model):
    TRACK_CHOICES = [
        ('FE', 'Frontend'),
        ('BE', 'Backend'),
        ('DE', 'Design'),
    ]
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=10, choices=TRACK_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    lion = models.ForeignKey(Lion, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.lion.name}] {self.title}"

class LionProfile(models.Model):
    lion = models.OneToOneField(Lion, on_delete=models.CASCADE, related_name='profile')
    github_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lion.name}'s Profile"

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    lions = models.ManyToManyField(Lion, related_name='tags', blank=True)

    def __str__(self):
        return self.name