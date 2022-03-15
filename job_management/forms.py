from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import departments

class create_department_form(forms.ModelForm):

    class  Meta():
        model = departments
        fields = ('department_name',)

