
from django.contrib import admin
from django.urls import path

from job_management import views
app_name = "job_management"

urlpatterns = [
    path('', views.departments,name='job_management/departments'),

]
