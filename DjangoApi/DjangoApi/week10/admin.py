from django.contrib import admin

from .models import Lion, LionProfile, Tag, Task


@admin.register(Lion)
class LionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lion', 'is_done', 'created_at')
    list_filter = ('is_done', 'created_at')
    search_fields = ('title',)


@admin.register(LionProfile)
class LionProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'lion', 'bio', 'github_url')
    search_fields = ('lion__name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
