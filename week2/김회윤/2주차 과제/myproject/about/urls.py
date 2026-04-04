from django.urls import path
from .views import intro

urlpatterns = [
    path('', intro),
]