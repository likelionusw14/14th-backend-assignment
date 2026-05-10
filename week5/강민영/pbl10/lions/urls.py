from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), # 홈 화면 (경로 중복 피하기 위해 /home/으로 설정)
    path('', views.lion_list, name='lion_list'), # 목록 페이지
    path('new/', views.lion_create, name='lion_create'), # 등록 페이지
    path('<int:id>/', views.lion_detail, name='lion_detail'), # 상세 페이지
    path('<int:id>/edit/', views.lion_edit, name='lion_edit'), # 기본 정보 수정
    path('<int:id>/delete/', views.lion_delete, name='lion_delete'), # 삭제
    path('<int:id>/profile/', views.profile_edit, name='profile_edit'), # 1:1 프로필 수정
    path('<int:lion_id>/tag/<int:tag_id>/', views.tag_toggle, name='tag_toggle'), # N:M 태그 토글
    path('<int:lion_id>/task/<int:task_id>/', views.task_toggle, name='task_toggle'), # 1:N 과제 토글
]