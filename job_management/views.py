from distutils.log import error
from django.shortcuts import redirect, render
from .forms import create_department_form


# Create your views here.

def create_department(request):
    context = {}
    if request.method == "POST":

        form = create_department_form(request.POST)
        if form.is_valid():
            form.save()
            context["success_message"] = "Department has been added" 
            return redirect('/job_management/departments.html')
        else:
            context["create_department_errors"] = form.errors 
            return redirect('/job_management/departments.html', context)

    else:
        return render(request, 'job_management/departments.html')

def job_titles(request):
    return render(request, 'job_management/job_titles.html')