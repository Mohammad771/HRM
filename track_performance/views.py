from distutils.log import error
import pandas as pd
from django.shortcuts import redirect, render, HttpResponse 
from HRM.CRUD import *
from .models import attendance_file, attendance
from .forms import attendance_file_form
from users.models import users as users_model
from datetime import datetime

# Create your views here.
def viewEvaluations(request):
    context = {}

    context['evaluations'] = Read('evaluations')
    return render(request, 'track_performance/viewEvaluations.html', context)

def createEvaluations(request):
    context = {}

    if request.method == "POST": 

        print(request.POST)
        result = Create(request.POST, 'evaluations')
        if result["status"] == True:
            context["success_message"] = "Evaluation has been added 👍"
        else:
            context["form_errors"] = result["form_errors"]

    context['departments'] = Read('departments')
    context['job_titles'] = Read('job_titles')
    context['users'] = Read('users')
    return render(request, 'track_performance/createEvaluations.html', context)


def manageAttendance(request):
    # d = attendance_file.objects.get(pk=1)
    # print(d.attendance_file_created_at)
    # d.attendance_file_created_at = "2020-12-12,12:12:12"
    # d.save()
    # print(d.attendance_file_created_at)
    context = {}
    attendance_rows = pd.read_excel("static/upload/attendance_files/Attendance_Sheet_1.xlsx")
    attendance_rows = attendance_rows.to_dict()
    users_count = len(attendance_rows['attendance_user_id'])
    insert_dict = {}
    print(substract_dates(attendance_rows['attendance_clock_in'][0], attendance_rows['attendance_clock_out'][0]))
    for index in range (users_count):
        attendance.objects.create(
            attendance_user_id = users_model.objects.get(pk=attendance_rows['attendance_user_id'][index]),
            attendance_date = attendance_rows['attendance_date'][index],
            attendance_clock_in = attendance_rows['attendance_clock_in'][index],
            attendance_clock_out = attendance_rows['attendance_clock_out'][index],
            attendance_duration = substract_dates(attendance_rows['attendance_clock_in'][index], attendance_rows['attendance_clock_out'][index]),
            attendance_working_from = attendance_rows['attendance_working_from'][index]
            )



    
    if request.method == 'POST':  
        attendance_sheet_form = attendance_file_form(request.POST, request.FILES)
        if attendance_sheet_form.is_valid():
            attendance_sheet_form.save()
        else:
            context['file_upload_error'] = attendance_sheet_form.errors

    return render(request, 'track_performance/manageAttendance.html', context)


def substract_dates(start, end):

    # duration = end - start
    days = end - start
    hours = divmod(days.total_seconds(), 3600) 
    result = "{}:{}".format(int(hours[0]), int(hours[1] * 60))
    return result

