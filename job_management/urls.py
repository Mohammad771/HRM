
from django.contrib import admin
from django.urls import path

from job_management import views
app_name = "job_management"

urlpatterns = [
<<<<<<< HEAD
    path('departments/', views.create_department,name='job_management/create_department'),
    path('departments/change_department_status/', views.change_department_status, name='job_management/change_department_status'),
    path('job_titles/', views.job_titles, name='job_management/job_titles'),
=======
    path('departments/', views.departments_handler,name='job_management/create_department'),
    path('job_titles/', views.job_titles_handler, name='job_management/job_titles'),
>>>>>>> 7b1af9374a6a3f611515085d29bb44a247d26347
    path('job_titles/change_job_title_status/', views.change_job_title_status, name='job_management/change_job_title_status'),
    path('create_contract/', views.create_contract, name='job_management/create_contract'),
    path('viewContract/', views.viewContract, name='job_management/viewContract'),

]
