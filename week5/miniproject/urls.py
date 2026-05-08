# myapp/urls.py
from django.urls import path
from . import views

app_name = 'miniproject'

urlpatterns = [
    path('', views.lion_list, name='lion_list'),
    path('new/', views.lion_create, name='lion_create'),
    path('<int:pk>/', views.lion_detail, name='lion_detail'),
    path('<int:pk>/edit/', views.lion_edit, name='lion_edit'),
    path('<int:pk>/delete/', views.lion_delete, name='lion_delete'),
    path('<int:pk>/tasks/<int:task_id>/toggle/', views.task_toggle, name='task_toggle'),
    path('<int:pk>/profile/edit/', views.profile_edit, name='profile_edit'),
    path('<int:pk>/tags/<int:tag_id>/toggle/', views.tag_toggle, name='tag_toggle'),
]