from django import forms 
from .models import *

class create_evaluation_form(forms.ModelForm):

    class  Meta():
        model = evaluations
        fields = ('evaluation_user_id', 'evaluation_department_id', 'evaluation_job_title_id', 'evaluation_interaction_rate',
        'evaluation_time_rate', 'evaluation_quality_rate', 'evaluation_overall_rate', 'evaluation_date')
        error_messages = {
            'evaluation_date': {
                'required': ("Please select the evaluation's date 🙁"),
            },
        }


class attendance_file_form(forms.ModelForm):
    class  Meta():
        model = attendance_file
        fields = ('attendance_file', 'attendance_file_date')


class create_attendance_form(forms.ModelForm):
    class  Meta():
        model = attendance
        fields = ('attendance_user_id', 'attendance_date', 'attendance_clock_in', 'attendance_clock_out'
        , 'attendance_duration', 'attendance_half_day', 'attendance_working_from' )
