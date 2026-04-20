from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='lion_list'),
    path('lions/new/', views.lion_new, name ='lion_create'),
    path('lions/<id>/edit/', views.lion_edit, name='lion_edit'),
    path('lions/<id>/', views.lion_detail, name='lion_detail'),
    path('lions/<id>/delete/', views.lion_delete, name='lion_delete'),
]