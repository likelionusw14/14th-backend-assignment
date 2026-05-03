from django.urls import path
from . import views

app_name = 'orm_basic'

urlpatterns = [
    path('create/', views.lion_create, name='lion_create'),
    path('', views.lion_list, name='lion_list'),
    path('<int:pk>/', views.lion_detail, name='lion_detail'),
    path('<int:pk>/edit/', views.lion_edit, name='lion_edit'),
    path('<int:pk>/delete/', views.lion_delete, name='lion_delete'),
    path('task/<int:pk>/toggle/', views.task_toggle, name='task_toggle'),
]