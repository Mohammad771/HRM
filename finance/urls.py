
from django.contrib import admin
from django.urls import path

from finance import views
app_name = "finance"

urlpatterns = [
    path('punishments/', views.punishments,name='finance/punishments'),
    path('rewards/', views.rewards,name='finance/rewards'),
    path('create_payroll/', views.create_payroll,name='finance/create_payroll'),
    path('view_payroll/', views.view_payroll,name='finance/view_payroll'),


]
