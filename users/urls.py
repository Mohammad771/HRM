
from django.contrib import admin
from django.urls import path

from users import views
app_name = "users"

urlpatterns = [
    path('', views.user_login,name='users/login'),
    path('logout/', views.user_logout,name='users/logout'),
    path('register/', views.register,name='users/register'),
    path('dashboard/', views.dashboard, name='users/dashboard'),
    path('viewUsers/', views.viewUsers, name='users/viewUsers'),

]
