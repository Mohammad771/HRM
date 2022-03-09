
from django.contrib import admin
from django.urls import path

from job_management import views
app_name = "job_management"

urlpatterns = [
    path('departments/', views.departments,name='job_management/departments'),
    path('job_titles/', views.job_titles, name='job_management/job_titles'),

]
