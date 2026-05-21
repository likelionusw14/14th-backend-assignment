from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('success/', views.login_success, name = 'login_success'),
    path('profile/', views.profile_view, name='profile' ),
    path('change-password/', views.change_password, name='change_password'),
]