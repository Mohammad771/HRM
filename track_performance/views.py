from django.shortcuts import render

# Create your views here.
def viewEvaluations(request):
    return render(request, 'track_performance/viewEvaluations.html')

def createEvaluations(request):
    return render(request, 'track_performance/createEvaluations.html')