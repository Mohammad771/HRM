from django.shortcuts import render
from .models import rewards as rewards_model
from .models import punishments as punishments_model
from HRM.CRUD import *

# Create your views here.

def punishments(request):

    context = {}
    if request.method == "POST":
        print(request.POST)
        result = Create(request.POST, 'punishments')
        if result["status"] == True:
            context["success_message"] = "Alhamdulillah"
        else:
            context["form_errors"] = result['form_errors']

    context['viewPunishment'] = Read("punishments")
    context["users"] = Read("users")
    return render(request, 'finance/punishments.html', context)

def rewards(request):
    context = {}
    if request.method == "POST":
        print(request.POST)
        result = Create(request.POST, 'rewards')
        if result["status"] == True:
            context["success_message"] = "Alhamdulillah"
        else:
            context["form_errors"] = result['form_errors']

    context['viewReward'] = Read("rewards")
    context["users"] = Read("users")
    return render(request, 'finance/rewards.html', context)