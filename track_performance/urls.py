
from django.contrib import admin
from django.urls import path

from track_performance import views
app_name = "track_performance"

urlpatterns = [
    path('viewEvaluations/', views.viewEvaluations,name='track_performance/viewEvaluations'),
    path('createEvaluations/', views.createEvaluations, name='track_performance/createEvaluations'),


]
