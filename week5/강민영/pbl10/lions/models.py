from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Lion(models.Model):
    TRACK_CHOICES = [
        ('FE', 'Front-end'),
        ('BE', 'Back-end'),
        ('DESIGN', 'Design'),
    ]
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=10, choices=TRACK_CHOICES)
    tags = models.ManyToManyField(Tag, related_name='lions', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.track}] {self.name}"

class Task(models.Model):
    lion = models.ForeignKey(Lion, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lion.name} - {self.title}"

class LionProfile(models.Model):
    lion = models.OneToOneField(Lion, on_delete=models.CASCADE, related_name='profile')
    github_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lion.name}'s Profile"