from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import users

class register_form(UserCreationForm):

    class  Meta():
        model = users
        fields = ('email', 'username',  'is_admin', 'user_last_name', 'user_first_name',
         "user_mobile",'user_nationality_ID', "user_DOB" )

# class login_form(forms.ModelForm):
#     class  Meta():
#         model = users
#         fields = ('email', 'user_password_hash')
