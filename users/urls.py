
from django.contrib import admin
from django.urls import path

from users import views

urlpatterns = [
    path('', views.login,name='users/login'),
    path('register/', views.register,name='users/register'),
    path('dashboard/', views.dashboard, name='users/dashboard'),

]
