from django.db import models


class Lion(models.Model):
    """멋쟁이사자처럼 멤버 모델"""
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Task(models.Model):
    """Lion에 연결된 할 일 모델 (1:N)"""
    lion = models.ForeignKey(
        Lion,
        on_delete=models.CASCADE,
        related_name='tasks',
    )
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{'✔' if self.is_done else '✗'}] {self.title}"


class LionProfile(models.Model):
    """Lion 프로필 모델 (1:1)"""
    lion = models.OneToOneField(
        Lion,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    bio = models.TextField(blank=True, default='')
    github_url = models.URLField(blank=True, default='')

    class Meta:
        ordering = ['-lion__created_at']

    def __str__(self):
        return f"{self.lion.name}의 프로필"


class Tag(models.Model):
    """태그 모델 (N:M)"""
    name = models.CharField(max_length=50, unique=True)
    lions = models.ManyToManyField(
        Lion,
        related_name='tags',
        blank=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
