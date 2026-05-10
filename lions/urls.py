from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("lions/", views.lion_list, name="lion_list"),
    path("lions/new/", views.lion_create, name="lion_create"),
    path("lions/<int:lion_id>/", views.lion_detail, name="lion_detail"),
    path("lions/<int:lion_id>/edit/", views.lion_edit, name="lion_edit"),
    path("lions/<int:lion_id>/delete/", views.lion_delete, name="lion_delete"),
    path(
        "lions/<int:lion_id>/tasks/<int:task_id>/toggle/",
        views.task_toggle,
        name="task_toggle",
    ),
    path(
        "lions/<int:lion_id>/tasks/new/",
        views.task_create,
        name="task_create",
    ),
    path(
        "lions/<int:lion_id>/profile/edit/",
        views.profile_edit,
        name="profile_edit",
    ),
    path("lions/<int:lion_id>/tags/toggle/", views.tag_toggle, name="tag_toggle"),
]
