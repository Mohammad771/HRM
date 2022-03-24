from django import forms 
from .models import departments, job_titles, contracts
from users.forms import UserCreationForm
from finance.models import annual_bonuses, bank_account, allowances

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

class contract_form_class(forms.ModelForm):

    class  Meta():
        model = contracts
        fields = ('contract_hour_price', 'contract_expiry_date', 'contract_starting_date', 'contract_conditions',
        'contract_auto_renewal', 'contract_user_id')
        # error_messages = {
        #     'department_name': {
        #         'required': ("Department name cannot be empty 😥"),
        #     },
        # }

class annual_bonuses_form_class(forms.ModelForm):

    class  Meta():
        model = annual_bonuses
        fields = ('annual_bonus_amount',)
        error_messages = {
            'annual_bonus_amount': {
                'required': ("Anuual Bonus Amount cannot be empty, you can set it to 0 instead"),
            },
        }

class bank_account_form_class(forms.ModelForm):

    class  Meta():
        model = bank_account
        fields = ('bank_account_bank_name', 'bank_account_card_holder_name', 'bank_account_iban_number', 'bank_account_user_id')
        error_messages = {
            'bank_account_bank_name': {
                'required': ("Bank Name cannot be empty 😥"),
            },
            'bank_account_card_holder_name': {
                'required': ("Card Holder Name cannot be empty 😥"),
            },
            'bank_account_iban_number': {
                'required': ("IBAN Number name cannot be empty 😥"),
            },
        }

class allowances_form_class(forms.ModelForm):

    class  Meta():
        model = allowances
        fields = ('allowance_type', 'allowance_amount', 'allowance_user_id')
        error_messages = {
            'department_name': {
                'required': ("Department name cannot be empty 😥"),
            },
        }

class create_department_form(forms.ModelForm):

    class  Meta():
        model = departments
        fields = ('department_name',)
        error_messages = {
            'department_name': {
                'required': ("Department name cannot be empty 😥"),
            },
        }

