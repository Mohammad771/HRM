from django import forms 
from .models import departments, job_titles, contracts

class create_department_form(forms.ModelForm):

    class  Meta():
        model = departments
        fields = ('department_name',)
        error_messages = {
            'department_name': {
                'required': ("Department name cannot be empty 😥"),
            },
        }

class create_job_title_form(forms.ModelForm):

    class  Meta():
        model = job_titles
        fields = ('job_title_name', 'job_title_department_id', 'job_title_hour_price', 'job_title_status')
        error_messages = {
            'job_title_name': {
                'required': ("Job title name cannot be empty 😥"),
            },
            'job_title_hour_price': {
                'required': ("Hour Price cannot be empty 😥"),
                'invalid': ("Hour Price should be a number 😥"),
            },
        }

class create_contract_form(forms.ModelForm):

    class  Meta():
        model = contracts
        fields = ('contract_hour_price', 'contract_expiry_date', 'contract_starting_date', 'contract_conditions',
        'contract_auto_renewal', 'contract_user_id')
        # error_messages = {
        #     'department_name': {
        #         'required': ("Department name cannot be empty 😥"),
        #     },
        # }




