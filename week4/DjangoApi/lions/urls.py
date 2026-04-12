from django.urls import path
from . import views

urlpatterns = [
    path('', views.lion_list),
]