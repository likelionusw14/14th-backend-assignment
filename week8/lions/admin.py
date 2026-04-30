from django.contrib import admin
from .models import Lion


@admin.register(Lion)
class LionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'track', 'created_at')  # 목록에 표시할 컬럼
    list_filter = ('track',)                               # 우측 트랙 필터
    search_fields = ('name',)                              # 검색 (이름)
    ordering = ('-created_at',)                            # 최신순 정렬
