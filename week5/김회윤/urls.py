from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lions", views.lion_list, name="lion_list"),
    path("lions/", views.lion_list, name="lion_list_slash"),
    path("lions/new", views.lion_new, name="lion_new"),
    path("lions/new/", views.lion_new, name="lion_new_slash"),
]
