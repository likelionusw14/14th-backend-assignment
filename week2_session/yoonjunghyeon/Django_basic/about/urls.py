# about/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/about/intro/ 주소로 접속하면 intro 뷰 실행
    path('intro/', views.intro, name='about'),
    path('', views.intro, name='about'),
    
]