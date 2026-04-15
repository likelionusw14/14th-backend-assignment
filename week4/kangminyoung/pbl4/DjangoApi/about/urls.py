from django.urls import path
from . import views

urlpatterns = [
    path('', views.intro, name='intro'),              # / 접속 시
    path('lions/', views.lions_list, name='lions_list'), # /lions 접속 시
]