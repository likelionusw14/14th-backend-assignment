
from django.db import models

class Lion(models.Model):

    TRACK_CHOICES = [
        ('frontend', '프론트엔드'),
        ('backend', '백엔드'),
        ('design', '디자인'),
        ('planning', '기획'),
    ]

    name  = models.CharField(max_length=100)   # 이름 (필수)
    track = models.CharField(max_length=100, choices=TRACK_CHOICES, blank=True, null=True)  # 트랙 (선택)
    #blank = True/ null = True : 입력 안 해도, 빈값(NULL)으로 저장해도 OK

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): #객체를 글자로 표현할 때 사용하는 함수
        return self.name
