from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import departments

class create_department_form(UserCreationForm):

    class  Meta():
        model = departments
        fields = ('department_name',)

