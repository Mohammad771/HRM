from django.shortcuts import render
from .models import rewards as rewards_model
from .models import punishments as punishments_model
from HRM.CRUD import *

# Create your views here.

def punishments(request):
    context = {}
    viewPunishments = punishments_model.objects.all()
    context['viewPunishment'] = viewPunishments
    if request.method == "POST":
        print(request.POST)
        result = Create(request.POST, 'punishments')
        if result["status"] == True:
            context["success_message"] = "Alhamdulillah"
        else:
            context["form_errors"] = result['form_errors']
    context["users"] = Read("users")
    return render(request, 'finance/punishments.html', context)

def rewards(request):
    context = {}
    viewRewards = rewards_model.objects.all()
    # jobTitles = job_titles.objects.all()
    context['viewReward'] = viewRewards
    if request.method == "POST":
        print(request.POST)
        result = Create(request.POST, 'rewards')
        if result["status"] == True:
            context["success_message"] = "Alhamdulillah"
        else:
            context["form_errors"] = result['form_errors']
    context["users"] = Read("users")
    return render(request, 'finance/rewards.html', context)