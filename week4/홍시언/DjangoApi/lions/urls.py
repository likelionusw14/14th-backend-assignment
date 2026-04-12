from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('lions/', views.lions_list, name='lions_list'), 
]