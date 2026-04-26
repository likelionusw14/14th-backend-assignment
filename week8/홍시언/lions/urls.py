from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lions/', views.lion_list, name='lion_list'),
    path('lions/new/', views.lion_create, name='lion_create'),
    path('lions/<int:pk>/', views.lion_detail, name='lion_detail'),
    path('lions/<int:pk>/edit/', views.lion_edit, name='lion_edit'),
    path('lions/<int:pk>/delete/', views.lion_delete, name='lion_delete'),
]