from django import forms 
# from django.contrib.auth.models import User
from .models import users

class login_form(forms.ModelForm):
    class  Meta():
        model = users
        fields = ('email', 'user_password_hash')