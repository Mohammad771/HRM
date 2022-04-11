
from django.contrib import admin
from django.urls import path

from employees_requests import views
app_name = "employees_requests"

urlpatterns = [
    path('loans/', views.loans,name='employees_requests/loans'),



]
