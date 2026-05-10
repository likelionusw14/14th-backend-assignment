from django.contrib import admin

from .models import Lion, LionProfile, Tag, Task


@admin.register(Lion)
class LionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "track", "created_at")
    list_editable = ("track",)
    search_fields = ("name", "track")
    list_filter = ("track",)
    ordering = ("-created_at",)
    list_per_page = 10
    readonly_fields = ("created_at",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "lion", "title", "completed", "created_at")
    list_editable = ("completed",)
    search_fields = ("title", "lion__name")
    list_filter = ("completed", "lion__track")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)


@admin.register(LionProfile)
class LionProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "lion", "github_url")
    search_fields = ("lion__name", "github_url", "bio")


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)
