from django import forms 
from finance.models import annual_bonuses, bank_account, allowances, rewards, punishments


class create_annual_bonuses_form(forms.ModelForm):

    class  Meta():
        model = annual_bonuses
        fields = ('annual_bonus_amount','annual_bonus_user_id')
        error_messages = {
            'annual_bonus_amount': {
                'required': ("Anuual Bonus Amount cannot be empty, you can set it to 0 instead"),
            },
        }

class create_bank_account_form(forms.ModelForm):

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

class create_allowances_form(forms.ModelForm):

    class  Meta():
        model = allowances
        fields = ('allowance_type', 'allowance_amount', 'allowance_user_id')
        error_messages = {
            'department_name': {
                'required': ("Department name cannot be empty 😥"),
            },
        }

class create_reward(forms.ModelForm):

    class  Meta():
        model = rewards
        fields = ('reward_user_id', 'reward_amount')


class create_punishment(forms.ModelForm):

    class  Meta():
        model = punishments
        fields = ('punishment_user_id', 'punishment_amount')