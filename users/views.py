from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import register_form
from .models import users as users_model
from job_management.models import contracts
from track_performance.models import evaluations
from django.core.exceptions import ValidationError
from datetime import date
import calendar
import json
from dateutil.relativedelta import relativedelta



def user_login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')

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
                    return redirect('/dashboard')

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
            return redirect('/dashboard')

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

    
@login_required
def dashboard(request):
    context = {}

    user_contract = contracts.objects.filter(contract_user_id=request.user)
    if len(user_contract):
        context["user_contract"] = user_contract[0]

    current_date = date.today()
    # current_month = current_date.month
    period_end = date.today() + relativedelta(days=+1)
    period_start = date.today() + relativedelta(months=-6)
    # print(calendar.month_abbr[current_month])


    evaluations_within_6_months = evaluations.objects.filter(evaluation_user_id=request.user,
    evaluation_deleted_at=None, evaluation_created_at__range=(period_start, period_end))
    months_array = []
    values_array = []
    for evaluation in evaluations_within_6_months:
        # months_array.append(evaluation.evaluation_created_at.date())
        eval_date = evaluation.evaluation_created_at
        months_array.append(date.today().strftime('%b %d'))
        values_array.append(evaluation.evaluation_overall_rate)

    if len(months_array):
        context['months_array'] = months_array
        context['values_array'] = values_array
        # context['months_array'] = json.dumps(months_array)
        # context['values_array'] = json.dumps(values_array)

    print(months_array)
    print(values_array)


    return render(request, 'users/dashboard.html', context)