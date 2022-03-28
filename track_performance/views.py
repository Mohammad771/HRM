from distutils.log import error
import pandas as pd
from django.shortcuts import redirect, render, HttpResponse 
from HRM.CRUD import *
from .models import attendance_file, attendance
from .forms import attendance_file_form, create_attendance_form
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
    context = {}
    context['duplicate_attendance_file_date'] = False

        
    if request.method == 'POST':
        all_attendance_files = attendance_file.objects.all()
        for attendance_file_row in all_attendance_files:
            if attendance_file_row.attendance_file_date == request.POST['attendance_file_date']:
                context['duplicate_attendance_file_date'] = True


        if context['duplicate_attendance_file_date'] == False:

            attendance_sheet_form = attendance_file_form(request.POST, request.FILES)
            if attendance_sheet_form.is_valid():

                attendance_rows = pd.read_excel(request.FILES['attendance_file'])
                attendance_rows = attendance_rows.to_dict()      

                required_column_is_not_in_file = False
                missing_columns_in_file = []
                if not 'attendance_user_id' in attendance_rows:
                    required_column_is_not_in_file = True
                    missing_columns.append("attendance_user_id")
                if not 'attendance_clock_in' in attendance_rows:
                    required_column_is_not_in_file = True
                    missing_columns.append("attendance_clock_in")
                if not 'attendance_clock_out' in attendance_rows:
                    required_column_is_not_in_file = True
                    missing_columns.append("attendance_clock_out")
                if not 'attendance_user_id' in attendance_rows:
                    required_column_is_not_in_file = True
                    missing_columns.append("attendance_user_id")
                if not 'attendance_working_from' in attendance_rows:
                    required_column_is_not_in_file = True
                    missing_columns.append("attendance_working_from")

                if required_column_is_not_in_file:
                    context['missing_columns_in_file'] = missing_columns_in_file
                
                else:

                    uploaded_file_name = (request.FILES['attendance_file'])
                    users_count = len(attendance_rows['attendance_user_id'])

                    insert_dict = {}
                    manual_errors_dict = {}
                    automatic_errors_dict = []
                    success = True
                    for index in range(users_count):

                        try:
                            user_row = users_model.objects.get(pk=attendance_rows['attendance_user_id'][index])
                        except (users_model.DoesNotExist):
                            manual_errors_dict.append("The user with id {} in the row {} does not exist in the system"
                            .format(attendance_rows['attendance_user_id'][index], index + 2))
                            continue

                        insert_dict['attendance_user_id'] = user_row
                        insert_dict['attendance_clock_in'] = attendance_rows['attendance_clock_in'][index]
                        insert_dict['attendance_clock_out'] = attendance_rows['attendance_clock_out'][index]
                        insert_dict['attendance_duration'] = substract_dates(attendance_rows['attendance_clock_in'][index], attendance_rows['attendance_clock_out'][index]),
                        insert_dict['attendance_working_from'] = attendance_rows['attendance_working_from'][index]
                        attendance_form = create_attendance_form(insert_dict)
                        if not attendance_form.is_valid():
                            success = False
                            automatic_errors_dict.update({"row":index, "attendance_user_id":attendance_rows['attendance_user_id'][index],
                            "errors":attendance_form.errors})
            else:
                context['file_upload_error'] = attendance_sheet_form.errors

                attendance_sheet_form.save()

    return render(request, 'track_performance/manageAttendance.html', context)


def substract_dates(start, end):

    # duration = end - start
    days = end - start
    hours = divmod(days.total_seconds(), 3600)
    result = "{}:{}".format(int(hours[0]), int(hours[1] * 60))
    return result

