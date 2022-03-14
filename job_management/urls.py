
from django.contrib import admin
from django.urls import path

from job_management import views
app_name = "job_management"

urlpatterns = [
    path('departments/', views.create_department,name='job_management/create_department'),
    path('job_titles/', views.job_titles, name='job_management/job_titles'),
    path('create_contract/', views.create_contract, name='job_management/create_contract'),
    path('viewContract/', views.viewContract, name='job_management/viewContract'),

]
