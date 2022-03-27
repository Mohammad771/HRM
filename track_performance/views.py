from distutils.log import error
import pandas as pd
from django.shortcuts import redirect, render, HttpResponse 
from HRM.CRUD import *
from .models import attendance_file
from .forms import attendance_file_form

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
    df = pd.read_excel("static/upload/attendance_files/Attendance_Sheet_1.xlsx")
    # df.to_dict()
    df = df.to_dict()
    print(df)
    users_count = len(df['attendance_user_id'])
    insert_dict = {}
    for index in df:
        print(df[index])



    
    if request.method == 'POST':  
        attendance_sheet_form = attendance_file_form(request.POST, request.FILES)
        if attendance_sheet_form.is_valid():
            attendance_sheet_form.save()
        else:
            context['file_upload_error'] = attendance_sheet_form.errors

    return render(request, 'track_performance/manageAttendance.html', context)


# def handle_uploaded_file(file):  
#     with open('static/upload/attendace_files/', 'wb+') as destination:  
#         for chunk in file.chunks():  
#             destination.write(chunk)  

# from datetime import datetime
# then = datetime(2012, 3, 5, 23, 8, 15)        # Random date in the past
# now  = datetime.now()                         # Now
# duration = now - then                         # For build-in functions
# duration_in_s = duration.total_seconds()      # Total number of seconds between dates
# hours = divmod(duration_in_s, 3600)[0]        # Duration in hours