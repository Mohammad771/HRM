
from django.contrib import admin
from django.urls import path

from finance import views
app_name = "finance"

urlpatterns = [
    path('punishments/', views.punishments,name='finance/punishments'),
    path('rewards/', views.rewards,name='finance/rewards'),


]
