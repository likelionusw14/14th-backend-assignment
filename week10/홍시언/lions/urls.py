from django.urls import path
from . import views

urlpatterns = [
    path('', views.lion_list, name='lion_list'),
    path('new/', views.lion_create, name='lion_create'),
    path('<int:lion_id>/', views.lion_detail, name='lion_detail'),
    path('<int:lion_id>/edit/', views.lion_edit, name='lion_edit'),
    path('<int:lion_id>/delete/', views.lion_delete, name='lion_delete'),
    path('<int:lion_id>/tasks/<int:task_id>/toggle/', views.task_toggle, name='task_toggle'),
    path('<int:lion_id>/profile/edit/', views.profile_edit, name='profile_edit'),
    path('<int:lion_id>/tags/<int:tag_id>/toggle/', views.tag_toggle, name='tag_toggle'),
]