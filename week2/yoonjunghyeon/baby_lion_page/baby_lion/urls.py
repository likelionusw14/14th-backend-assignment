from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lions/', views.lion_list, name='lion_list'),
    path('lions/<str:name>/', views.lion_detail, name='lion_detail'),
]