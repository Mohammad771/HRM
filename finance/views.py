from django.shortcuts import render

# Create your views here.

def punishments(request):
    return render(request, 'finance/punishments.html')

def rewards(request):
    return render(request, 'finance/rewards.html')