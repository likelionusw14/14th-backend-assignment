from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),             # '/' 경로 접속 시 home 뷰 실행
    path('lion_list/', views.lion_list, name='lion_list')]