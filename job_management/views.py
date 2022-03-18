from distutils.log import error
from django.shortcuts import redirect, render, HttpResponse 
from pprint import pprint
from HRM.CRUD import *
from .models import job_titles as job_titles_model
from .models import departments as departments_model


# Create your views here.

def create_department(request):
    context = {}
    context['departments'] = Read('departments')
    pprint(context["departments"])
    if request.method == "POST":
        result = Create(request.POST, 'departments')
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
    context['departments'] = Read('departments')
    context["job_titles"] = Read('job_titles')

    if request.method == "POST":
        if request.POST['request_type'] == "update":
            job_title_id = request.POST['job_title_id']
            result = Update(request.POST, "job_titles", job_title_id)

            if result['status'] == True:
                context["job_titles"] = Read('job_titles')
                return render(request, 'job_management/job_titles.html', context)

            else:
                context["form_errors"] = result['form_errors']
                return render(request, 'job_management/job_titles.html', context)

        else:
            result = Create(request.POST, 'job_titles')
            if result["status"] == True:
                context["success_message"] = "Job Title has been added 👍"
                context['job_titles'] = Read('job_titles')
                return render(request, 'job_management/job_titles.html', context)
            else:
                context["form_errors"] = result['form']
                return render(request, 'job_management/job_titles.html', context)

    else:
        return render(request, 'job_management/job_titles.html', context)


def change_job_title_status(request):

    job_title_id = request.POST['job_title_id']
    switch = request.POST['switch']
    Job_title = job_titles_model.objects.get(pk=job_title_id)
    
    if switch == "make_active":
        Job_title.job_title_status = True
    else:
        Job_title.job_title_status = False

    Job_title.save() 
    
    html = "<html><body>Success.</body></html>" 
    return HttpResponse(html)


def change_department_status(request):
    department_id = request.POST['department_id']
    switch = request.POST['switch']
    department = departments_model.objects.get(pk=department_id)

    if switch == "make_active":
        department.department_status = True
    else:
        department.department_status = False

    department.save()

    html = "<html><body>Success.</body></html>"
    return HttpResponse(html)
    
   


#def added_jobs(request):
#    var_1 = add_job_titles.objects.all()
#    return render(request, 'job_management/job_titles.html', {'var_1':var_1})

def create_contract(request):
    return render(request, 'job_management/create_contract.html')

def viewContract(request):
    return render(request, 'job_management/viewContract.html')