from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'), # 서버에 들어갔을 때 로그인 페이지로 이동하도록 설정
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.login_success, name='login_success'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
]