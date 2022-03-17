
from django.contrib import admin
from django.urls import path

from job_management import views
app_name = "job_management"

urlpatterns = [
    path('departments/', views.create_department,name='job_management/create_department'),
    path('job_titles/', views.job_titles, name='job_management/job_titles'),
    path('job_titles/change_job_title_status/', views.change_job_title_status, name='job_management/change_job_title_status'),
    # path('job_titles/update_job_title/', views.update_job_title, name='job_management/update_job_title'),
    path('create_contract/', views.create_contract, name='job_management/create_contract'),
    path('viewContract/', views.viewContract, name='job_management/viewContract'),

]
