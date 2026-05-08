from django.urls import path
from . import views

urlpatterns = [
    # Lion CRUD (기존과 동일)
    path('',                 views.lion_list,   name='lion_list'),
    path('new/',             views.lion_create, name='lion_create'),
    path('<int:pk>/',        views.lion_detail, name='lion_detail'),
    path('<int:pk>/edit/',   views.lion_edit,   name='lion_edit'),
    path('<int:pk>/delete/', views.lion_delete, name='lion_delete'),

    # Task 완료 토글 (새로 추가)
    path('<int:pk>/tasks/<int:task_id>/toggle/', views.task_toggle, name='task_toggle'),

    # 프로필 수정 (새로 추가)
    path('<int:pk>/profile/edit/', views.profile_edit, name='profile_edit'),

    # 태그 토글 (새로 추가)
    path('<int:pk>/tags/<int:tag_id>/toggle/', views.tag_toggle, name='tag_toggle'),

    # 태그별 사자 목록 (새로 추가)
    path('tags/<int:tag_id>/lions/', views.tag_lions, name='tag_lions'),
]