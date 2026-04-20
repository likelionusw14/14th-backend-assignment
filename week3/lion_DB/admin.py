from django.contrib import admin
from .models import Lions
# Register your models here.
@admin.register(Lions)
class LionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'track', 'created_at'] 
    search_fields = ['name', 'track']                     
    list_filter = ['track']                             
    ordering = ['-created_at']                           
    list_per_page = 10  