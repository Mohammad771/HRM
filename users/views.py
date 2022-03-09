import imp
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import register_form
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

# User = get_user_model()

def user_login(request):

    if request.method == "POST":
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')

        user = authenticate(email=email, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard')

            else:
                print("User is not yet activated")
        
        else: 
            print("incorrect credentials")
    
    else:
        return render(request, 'users/login.html')

 

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')




def register(request):

    context = {}

    if request.method == "POST":
        form = register_form(request.POST)
        # username = request.POST.
        # request.POST.update({'username': ['something']})
        print(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password1)
            login(request, user)
            return redirect('/dashboard')

        else:
            print(form.errors)
            context['errors'] =  form.errors
            context['register_form'] = form
            # return redirect('/register')
            return render(request, 'users/register.html', context)

            
    else: #GET request

        form = register_form()
        context['register_form'] =  form
        
        return render(request, 'users/register.html', context)

    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         email = form.cleaned_data['email']
    #         password = form.cleaned_data['password1']
    #         user = authenticate(email=email, password=password)
    #         login(request, user)
    #         messages.success(request, ("Registration Successful"))
    #         return redirect('/dashboard')
    # else:
    #     form = UserCreationForm()

    #     return render(request, 'users/register.html', {"form":form})
    

def dashboard(request):
    return render(request, 'users/dashboard.html')


def viewUsers(request):
    return render(request, 'users/viewUsers.html')
