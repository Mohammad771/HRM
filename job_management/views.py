from distutils.log import error
from django.shortcuts import redirect, render
from .forms import create_department_form
from pprint import pprint


# Create your views here.

def create_department(request):
    context = {}
    if request.method == "POST":

        form = create_department_form(request.POST)
        if form.is_valid():
            form.save()
            context["success_message"] = "Department has been added 👍" 
            return render(request, 'job_management/departments.html', context)
        else:

            if (request.POST['department_name'] == ''):
                context["create_department_errors"] = "Department name can't be empty 😥"
            
            else:
                context["create_department_errors"] = form.errors 

            return render(request, 'job_management/departments.html', context)

    else:
        return render(request, 'job_management/departments.html')

def job_titles(request):
    return render(request, 'job_management/job_titles.html')

def create_contract(request):
    return render(request, 'job_management/create_contract.html')

def viewContract(request):
    return render(request, 'job_management/viewContract.html')