from django.db import models                    # Django 모델 기능 임포트
from django.contrib.auth.models import User     # 기본 제공 User 모델

class Post(models.Model):
    author = models.ForeignKey(                 # 글쓴이 (User 테이블과 연결)
        User,
        on_delete=models.CASCADE,               # User 삭제 시 글도 삭제
        related_name='posts'
    )
    title = models.CharField(max_length=200)    # 제목 (최대 200자)
    content = models.TextField()                # 내용 (길이 제한 없음)
    is_published = models.BooleanField(         # 공개 여부
        default=False                           # 기본값: 비공개
    )
    created_at = models.DateTimeField(          # 작성 시간
        auto_now_add=True                       # 생성 시 자동 저장
    )

    def __str__(self):                         # Admin에서 제목으로 표시
        return self.title