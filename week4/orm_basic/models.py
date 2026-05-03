from django.db import models

class Lion(models.Model):
    TRACK_CHOICE = [
        ('django', 'Django'),
        ('springboot', 'SpringBoot'),
        ('frontend', 'Frontend'),
    ]
    name = models.CharField(max_length=100)
    track = models.CharField(max_length=100, choices=TRACK_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'lions'

    def __str__(self):
        return self.name


class Task(models.Model):
    author = models.ForeignKey(
        Lion,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return self.title


class LionProfile(models.Model):
    user = models.OneToOneField(
        Lion,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    github_url = models.URLField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'lion_profile'

    def __str__(self):
        return self.user.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lions = models.ManyToManyField(Lion, blank=True)

    class Meta:
        db_table = 'tags'

    def __str__(self):
        return self.name