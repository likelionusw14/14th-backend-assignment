from django.urls import path

from . import views

app_name = 'lions'

urlpatterns = [
    # Lion CRUD
    path('', views.lion_list, name='list'),
    path('new/', views.lion_new, name='new'),
    path('<int:lion_id>/', views.lion_detail, name='detail'),
    path('<int:lion_id>/edit/', views.lion_edit, name='edit'),
    path('<int:lion_id>/delete/', views.lion_delete, name='delete'),

    # Task 토글
    path('<int:lion_id>/tasks/<int:task_id>/toggle/', views.task_toggle, name='task_toggle'),

    # LionProfile 수정
    path('<int:lion_id>/profile/edit/', views.profile_edit, name='profile_edit'),

    # Tag 토글
    path('<int:lion_id>/tags/<int:tag_id>/toggle/', views.tag_toggle, name='tag_toggle'),
]
