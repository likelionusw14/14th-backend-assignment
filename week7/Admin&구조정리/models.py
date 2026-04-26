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

    def __str__(self):
        return f"{self.name} ({self.track})"
