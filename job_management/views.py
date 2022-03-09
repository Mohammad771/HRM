from django.shortcuts import redirect, render


# Create your views here.

def departments(request):
    return render(request, 'job_management/departments.html')

def job_titles(request):
    return render(request, 'job_management/job_titles.html')