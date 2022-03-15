from distutils.log import error
from django.shortcuts import redirect, render
from .forms import create_department_form
from pprint import pprint
from HRM.CRUD import *


# Create your views here.

def create_department(request):
    context = {}
    context['departments'] = Read('departments')
    if request.method == "POST":

        result = Create(request.POST, 'department')
        if result["status"] == True:
            context["success_message"] = "Department has been added 👍"
            return render(request, 'job_management/departments.html', context)
        else:
            context["create_department_form"] = result['form']
            return render(request, 'job_management/departments.html', context)

    else:
        context['departments'] = Read('departments')
        return render(request, 'job_management/departments.html', context)

def job_titles(request):
    return render(request, 'job_management/job_titles.html')

def create_contract(request):
    return render(request, 'job_management/create_contract.html')

def viewContract(request):
    return render(request, 'job_management/viewContract.html')