from django.urls import path
from . import views

app_name = 'lions'

urlpatterns = [
    path('', views.lion_list, name='lion_list'),
    path('new/', views.lion_create, name='lion_create'),
    path('<int:pk>/', views.lion_detail, name='lion_detail'),
    path('<int:pk>/edit/', views.lion_update, name='lion_update'),
    path('<int:pk>/delete/', views.lion_delete, name='lion_delete'),
]