from django.contrib import admin
from .models import Lion

@admin.register(Lion)
class LionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'track', 'created_at')
    search_fields = ('name', 'track') #검색창
    list_filter = ('track',) #필터링 패널
    ordering = ('-created_at',) #-가 붙으면 내림차순(최신순), -가 없으면 오름차순(오래된순)
    list_per_page = 10 #한 페이지에 10개씩 보여줌