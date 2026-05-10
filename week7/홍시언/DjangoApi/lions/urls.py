from django.urls import path
from . import views

urlpatterns = [
    path('', views.lion_list, name='lion_list'),              
    path('new/', views.lion_new, name='lion_create'),            
    path('<int:pk>/', views.lion_detail_update, name='lion_detail'), 
    path('<int:pk>/edit/', views.lion_edit, name='lion_edit'),
    path('<int:pk>/delete/', views.lion_delete, name='lion_delete'), 
]