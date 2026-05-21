from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    track = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


