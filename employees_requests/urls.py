
from django.contrib import admin
from django.urls import path

from employees_requests import views
app_name = "employees_requests"

urlpatterns = [
    path('loans/', views.loans,name='employees_requests/loans'),
    path('loans/change_loan_status/', views.change_loan_status,name='employees_requests/change_loan_status'),
    path('vacations/change_vacation_status/', views.change_vacation_status,name='employees_requests/change_vacation_status'),
    path('vacations/', views.vacations,name='employees_requests/vacations'),
    path('overtime-categories/', views.overtime_categories,name='employees_requests/overtime_categories'),
    path('overtime/', views.overtime,name='employees_requests/overtime'),
    path('overtime/change_overtime_status/', views.change_overtime_status,name='employees_requests/change_overtime_status'),

]
