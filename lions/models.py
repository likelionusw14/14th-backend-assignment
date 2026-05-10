from django.db import models


class Lion(models.Model):
    TRACK_DJANGO = "Django"
    TRACK_SPRINGBOOT = "SpringBoot"
    TRACK_REACT = "React"
    TRACK_DESIGN = "Design"

    TRACK_CHOICES = [
        (TRACK_DJANGO, "Django"),
        (TRACK_SPRINGBOOT, "SpringBoot"),
        (TRACK_REACT, "React"),
        (TRACK_DESIGN, "Design"),
    ]

    name = models.CharField(max_length=50)
    track = models.CharField(
        max_length=20,
        choices=TRACK_CHOICES,
        default=TRACK_DJANGO,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} ({self.track})"


class Task(models.Model):
    lion = models.ForeignKey(
        Lion,
        on_delete=models.CASCADE,
        related_name="tasks",
    )
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.lion.name} - {self.title}"


class LionProfile(models.Model):
    lion = models.OneToOneField(
        Lion,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    github_url = models.URLField(blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"{self.lion.name} 프로필"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    lions = models.ManyToManyField(
        Lion,
        related_name="tags",
        blank=True,
    )

    def __str__(self):
        return self.name
