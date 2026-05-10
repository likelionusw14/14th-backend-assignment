# products/admin.py
from django.contrib import admin
from .models import Lion, Task, LionProfile, Tag # Post 대신 새로운 모델들 임포트

# 관리자 페이지에서 모델들을 관리할 수 있도록 등록합니다.
admin.site.register(Lion)
admin.site.register(Task)
admin.site.register(LionProfile)
admin.site.register(Tag)