from django.contrib import admin
from django.urls import path
from login import views as login_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', login_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('', login_views.profile, name='profile'),
    path('profile/', login_views.profile, name='profile')
]