from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]