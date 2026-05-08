from django.db import models


class Lion(models.Model):

    TRACK_CHOICES = [
        ('Django', 'Django'),
        ('SpringBoot', 'SpringBoot'),
        ('Frontend', 'Frontend'),
    ]

    name       = models.CharField(max_length=100)
    track      = models.CharField(max_length=100, choices=TRACK_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ── 1:N ───────────────────────────────────────────
class Task(models.Model):
    lion       = models.ForeignKey(Lion, on_delete=models.CASCADE, related_name='tasks')
    title      = models.CharField(max_length=200)
    completed  = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = '완료' if self.completed else '미완료'
        return f"[{status}] {self.title} ({self.lion.name})"


# ── 1:1 ───────────────────────────────────────────
class LionProfile(models.Model):
    lion       = models.OneToOneField(Lion, on_delete=models.CASCADE, related_name='profile')
    github_url = models.URLField(blank=True)
    bio        = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lion.name}의 프로필"


# ── N:M ───────────────────────────────────────────
class Tag(models.Model):
    name  = models.CharField(max_length=50, unique=True)
    lions = models.ManyToManyField(Lion, related_name='tags', blank=True)

    def __str__(self):
        return self.name