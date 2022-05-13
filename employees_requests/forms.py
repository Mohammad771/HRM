from django import forms 
from .models import *

class create_loan_form(forms.ModelForm):

    class  Meta():
        model = loans
        fields = ('loan_user_id', 'loan_amount', 'loan_started_date', 'loan_period',
        'loan_status', 'loan_is_approved')
        error_messages = {
            'loan_amount': {
                'required': ("Please enter the loan's amount"),
                'invalid': ("loan amount must be a number"),
            },
            'loan_period': {
                'required': ("Please enter the loan's period"),
                'invalid': ("loan period must be a number"),
            },
        }
        
class create_vacation_form(forms.ModelForm):

    class  Meta():
        model = vacations
        fields = ('vacation_user_id', 'vacation_leaving_date', 'vacation_coming_date', 'vacation_is_paid',)
        error_messages = {
            'vacation_leaving_date': {
                'required': ("Please enter the leaving date"),
            },
            'vacation_coming_date': {
                'required': ("Please enter the returning date"),
            },
        }
