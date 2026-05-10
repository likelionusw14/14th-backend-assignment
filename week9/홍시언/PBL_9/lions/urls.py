from django.urls import path
from . import views

urlpatterns = [
    path('', views.lion_list, name='lion_list'),
    path('create/', views.lion_create, name='lion_create'),
    path('<int:id>/', views.lion_detail, name='lion_detail'),
    path('task/<int:task_id>/toggle/', views.toggle_task, name='toggle_task'),
    path('<int:id>/delete/', views.lion_delete, name='lion_delete'),
    path('<int:id>/update/', views.lion_update, name='lion_update'),
]