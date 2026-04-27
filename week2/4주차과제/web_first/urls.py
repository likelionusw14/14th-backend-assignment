from django.urls import path
from . import views  # 현재 위치(.)에 있는 views.py를 가져온다는 뜻이에요!

urlpatterns = [ 
    # 1. 주소창에 아무것도 안 적었을 때 (예: 127.0.0.1:8000/)
    # 2. views.py 안에 있는 index라는 함수를 실행해라!
    # 3. 이 주소의 별명은 'index'라고 부르겠다.
    path('', views.index, name='index'),
    path('list/', views.baby_lion_list, name='아기사자 목록 보기'),
]