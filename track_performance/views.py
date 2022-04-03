from distutils.log import error
import pandas as pd
from django.shortcuts import redirect, render, HttpResponse 
from HRM.CRUD import *
from .models import attendance_file, attendance
from .forms import attendance_file_form, create_attendance_form
from users.models import users as users_model
from datetime import datetime, date, timedelta

# Create your views here.
def viewEvaluations(request):
    context = {}

    context['evaluations'] = Read('evaluations')
    return render(request, 'track_performance/viewEvaluations.html', context)

def createEvaluations(request):
    context = {}

    if request.method == "POST": 

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
    attendance_rows_beginning_date = date.today()
    attendance_rows_ending_date = False
    context = {}
    context['duplicate_attendance_file_date'] = False

        
    if request.method == 'POST':
        if request.POST['request_type'] == "search_date":
            date_period = request.POST['beginning_to_end']
            attendance_rows_beginning_date = date_period[:10]
            if "to" in date_period:
                attendance_rows_ending_date = date_period[14:]



        else:
            all_attendance_files = attendance_file.objects.all()
            uploaded_file_date = request.POST['attendance_file_date']
            attendance_rows_beginning_date = request.POST['attendance_file_date']
            attendance_rows_ending_date = request.POST['attendance_file_date']
            for attendance_file_row in all_attendance_files:
                
                if str(attendance_file_row.attendance_file_date) == str(uploaded_file_date):
                    context['duplicate_attendance_file_date'] = True


            if context['duplicate_attendance_file_date'] == False:

                attendance_sheet_form = attendance_file_form(request.POST, request.FILES)
                if attendance_sheet_form.is_valid():
                    attendance_sheet_form.save()

                    attendance_rows = pd.read_excel(request.FILES['attendance_file'])
                    attendance_rows = attendance_rows.to_dict()      

                    required_column_is_not_in_file = False
                    missing_columns_in_file = []
                    if not 'attendance_user_id' in attendance_rows:
                        required_column_is_not_in_file = True
                        missing_columns_in_file.append("attendance_user_id")
                    if not 'attendance_clock_in' in attendance_rows:
                        required_column_is_not_in_file = True
                        missing_columns_in_file.append("attendance_clock_in")
                    if not 'attendance_clock_out' in attendance_rows:
                        required_column_is_not_in_file = True
                        missing_columns_in_file.append("attendance_clock_out")
                    if not 'attendance_working_from' in attendance_rows:
                        required_column_is_not_in_file = True
                        missing_columns_in_file.append("attendance_working_from")

                    if required_column_is_not_in_file:
                        context['missing_columns_in_file'] = missing_columns_in_file
                    
                    else:

                        uploaded_file_name = (request.FILES['attendance_file'])
                        users_count = len(attendance_rows['attendance_user_id'])

                        insert_dict = {}
                        attendance_forms_array = []
                        manual_errors_array = []
                        automatic_errors_dict = {}
                        allowed_time_formats = ["%H:%M:%S", "%H:%M"]
                        success = True
                        if users_count == 0:
                            context['empty_file'] = "The uploaded file does not contain any records"
                            attendance_file.objects.latest('attendance_file_id').delete()
                        for index in range(users_count):

                            try:
                                user_id = attendance_rows['attendance_user_id'][index]
                                user_row = users_model.objects.get(pk=user_id)
                                insert_dict['attendance_user_id'] = user_id
                            except (users_model.DoesNotExist):
                                manual_errors_array.append("The user with id {} in the row {} does not exist in the system"
                                .format(user_id, index + 2))
                                success = False
                                
                            
                            try:
                                clock_in_time = attendance_rows['attendance_clock_in'][index]
                                datetime.strptime(str(clock_in_time), allowed_time_formats[0])
                                insert_dict['attendance_clock_in'] = clock_in_time
                            except ValueError:
                                try:
                                    datetime.strptime(str(clock_in_time), allowed_time_formats[1])
                                    insert_dict['attendance_clock_in'] = clock_in_time
                                except ValueError:
                                    manual_errors_array.append("""The Clock in time for the user with id {} in the row {} does not match
                                    the correct time formatting, Must be hh:mm or hh:mm:ss""".format(user_id, index + 2))
                                    success = False
                                        
                            try:
                                clock_out_time = attendance_rows['attendance_clock_out'][index]
                                datetime.strptime(str(clock_out_time), allowed_time_formats[0])
                                insert_dict['attendance_clock_out'] = clock_out_time
                            except ValueError:
                                try:
                                    datetime.strptime(str(clock_in_time), allowed_time_formats[1])
                                    insert_dict['attendance_clock_in'] = clock_out_time
                                except ValueError:
                                    manual_errors_array.append("""The Clock out time for the user with id {} in the row {} does not match
                                    the correct time formatting, Must be hh:mm or hh:mm:ss""".format(user_id, index + 2))
                                    success = False

                            result = substract_dates(clock_in_time, clock_out_time)
                            if result['sucess'] == False:
                                manual_errors_array.append(result['error'])
                                success = False
                            else:
                                insert_dict['attendance_duration'] = result['duration']

                            insert_dict['attendance_working_from'] = attendance_rows['attendance_working_from'][index]
                            insert_dict['attendance_source_file_id'] = attendance_file.objects.latest('attendance_file_id').attendance_file_id
                            insert_dict['attendance_date'] = uploaded_file_date

                            if not success:
                                context['excel_row_manual_errors'] = manual_errors_array
                                attendance_file.objects.latest('attendance_file_id').delete()
                                break
                            else:
                                attendance_form = create_attendance_form(insert_dict)
                                attendance_forms_array.append(attendance_form)
                                if not attendance_form.is_valid():
                                    attendance_file.objects.latest('attendance_file_id').delete()
                                    automatic_errors_dict = {"row":index+2, "user_id":attendance_rows['attendance_user_id'][index],
                                    "errors":attendance_form.errors}
                                    context['excel_row_automatic_errors'] = automatic_errors_dict
                                    break
                                else:
                                    for attendance_form_loop in attendance_forms_array:
                                        attendance_form_loop.save()
                                

                else:
                    context['file_upload_errors'] = attendance_sheet_form.errors

    if attendance_rows_ending_date:

        attendance_rows_beginning_date_object = datetime.strptime(attendance_rows_beginning_date, '%Y-%m-%d')
        attendance_rows_ending_date_object = datetime.strptime(attendance_rows_ending_date, '%Y-%m-%d')
        total_attendance_rows_in_period = []

        for day in daterange(attendance_rows_beginning_date_object, attendance_rows_ending_date_object):
            day = day.date()
            print(day)
            print(attendance.objects.filter(attendance_date=day))
            total_attendance_rows_in_period.extend(
                attendance.objects.filter(attendance_date=day)
            )
        context['attendance_rows'] = total_attendance_rows_in_period
        print(total_attendance_rows_in_period)

    else:
        context['attendance_rows'] = attendance.objects.filter(attendance_date=attendance_rows_beginning_date)

    return render(request, 'track_performance/manageAttendance.html', context)


def substract_dates(start, end):
    result = {}
    result['sucess'] = True
    days = datetime.combine(date.min, end) - datetime.combine(date.min, start)
    hours = divmod(days.total_seconds(), 3600)

    if hours[0] <= 0:
        result['sucess'] = False
        result['error'] = "The clock out time is before the clock in time, please verify."
    elif hours[0] > 24:
        result['sucess'] = False
        result['error'] = "The difference between clock in and clock out time is more than 24 hours, please verify."

    result['duration'] = "{}:{}".format(int(hours[0]), int(hours[1] * 60))
    return result


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

