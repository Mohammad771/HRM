from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import register_form
from .models import users as users_model
from .models import departments
from .models import job_titles
from django.core.exceptions import ValidationError



def user_login(request):
    if request.user.is_authenticated:
        return redirect('/departments')

    if 'next' in request.GET:
        request.session['next'] = request.GET['next']
    context = {}

    if request.method == "POST":
        requried_page = request.GET.get('next', None)
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')

        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.session:
                    requested_url = request.session['next']
                    return redirect(requested_url)
                else:
                    return redirect('/departments')

            else:
                print("User is not yet activated")
                context['login_error'] = "User is not yet activated"
                return render(request, 'users/login.html', context)
                
        
        else:
            print("incorrect credentials")
            context['login_error'] = "incorrect credentials"
            return render(request, 'users/login.html', context)
    
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
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('/departments')

        else:
            print(form.errors)
            context['errors'] =  form.errors
            context['form_errors'] = form
            # return redirect('/register')
            return render(request, 'users/register.html', context)

            
    else: #GET request

        form = register_form()
        context['register_form'] = form
        
        return render(request, 'users/register.html', context)
    
#@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')

@login_required 
def viewUsers(request):
    context = {}
    if request.user.is_admin:
        viewUsers = users_model.objects.all()
        #department = departments.objects.all()
        #jobTitles = job_titles.objects.all()
        context['viewUser'] = viewUsers
    else:
        context["not_admin"] = "Sorry, you are not authorized to view this page"
    return render(request, 'users/viewUsers.html', context)
