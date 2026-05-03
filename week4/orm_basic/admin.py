from django.contrib import admin
from .models import Lion, Task, LionProfile, Tag

@admin.register(Lion)
class LionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'track', 'created_at']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title', 'completed', 'created_at']

@admin.register(LionProfile)
class LionProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'github_url', 'created_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']