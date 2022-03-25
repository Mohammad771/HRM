from django import forms 
from .models import evaluations

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


