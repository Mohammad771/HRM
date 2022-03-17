from distutils.log import error
from django.shortcuts import redirect, render, HttpResponse 
from .forms import create_department_form, create_job_title_form
from pprint import pprint
from HRM.CRUD import *
from .models import job_titles as job_titles_model


# Create your views here.

def create_department(request):
    context = {}
    context['departments'] = Read('departments')
    print(context["departments"])
    if request.method == "POST":
        result = Create(request.POST, 'department')
        if result["status"] == True:
            context["success_message"] = "Department has been added 👍"
            context['departments'] = Read('departments')
            return render(request, 'job_management/departments.html', context)
        else:
            context["form_errors"] = result['form']
            return render(request, 'job_management/departments.html', context)

    else:
        context['departments'] = Read('departments')
        return render(request, 'job_management/departments.html', context)

def job_titles(request):
    context = {}
    Job_titles = job_titles_model.objects.all()
    context['departments'] = Read('departments')
    context["job_titles"] = Job_titles
    if request.method == "POST":

        if request.POST['request_type'] == "update":
            job_title_id = request.POST['job_title_id']
            Job_title = job_titles_model.objects.get(pk=job_title_id)
            form = create_job_title_form(request.POST, instance=Job_title)
            if form.is_valid():
                form.save()
                Job_titles = job_titles_model.objects.all()
                context["job_titles"] = Job_titles
                return render(request, 'job_management/job_titles.html', context)
            else:
                context["form_errors"] = form
                return render(request, 'job_management/job_titles.html', context)

        else:
            form = create_job_title_form(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'job_management/job_titles.html', context)
            else:
                context["form_errors"] = form
                return render(request, 'job_management/job_titles.html', context)

    else:
        return render(request, 'job_management/job_titles.html', context)


def change_job_title_status(request):

    job_title_id = request.POST['job_title_id']
    switch = request.POST['switch']
    Job_title = job_titles_model.objects.get(pk=job_title_id)
    print(Job_title.job_title_status)
    
    if switch == "make_active":
        Job_title.job_title_status = True
    else:
        Job_title.job_title_status = False

    Job_title.save()
    print(Job_title.job_title_status)
 
    
    html = "<html><body>Success.</body></html>" 
    return HttpResponse(html)

    
   


def create_contract(request):
    return render(request, 'job_management/create_contract.html')

def viewContract(request):
    return render(request, 'job_management/viewContract.html')