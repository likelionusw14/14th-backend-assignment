from django.urls import path
from . import views

app_name = 'lions'

urlpatterns = [
    path('lions/', views.lion_list, name='lion_list'),

    path('lions/new/', views.lion_create, name='lion_create'),

    path(
        'lions/<int:lion_id>/',
        views.lion_detail,
        name='lion_detail'
    ),

    path(
        'lions/<int:lion_id>/edit/',
        views.lion_edit,
        name='lion_edit'
    ),

    path(
        'lions/<int:lion_id>/delete/',
        views.lion_delete,
        name='lion_delete'
    ),
]