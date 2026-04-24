from django.urls import path
from . import views

urlpatterns = [
    path('', views.lion_list, name='lion_list'),
    path('new/', views.lion_create, name='lion_create'),
    path('<int:id>/', views.lion_detail, name='lion_detail'),
    path('<int:id>/edit/', views.lion_edit, name='lion_edit'),
    path('<int:id>/delete/', views.lion_delete, name='lion_delete'),
]
