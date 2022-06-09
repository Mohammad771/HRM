from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from HRM.CRUD import *
from datetime import datetime
from .models import loans as loans_model
from .models import vacations as vacations_model
from .models import overtime as overtime_model

# Create your views here.

@login_required
def loans(request):
    context = {} 

    if request.method == "POST": 
        new_post = request.POST.copy()

        if "loan_user_id" in request.POST:
            user_idd = request.POST['loan_user_id']
        else:
            user_idd =  request.user.user_id

        new_post['loan_user_id'] = user_idd

        current_date = datetime.today()
        next_month = current_date.month + 1
        loan_starting_date = str(current_date.year) + "-" + str(next_month) + "-01"
        new_post["loan_started_date"] = loan_starting_date
        print(loan_starting_date)
        
        result = Create(new_post, 'loans')
        if result["status"] == True:
            context["success_message"] = "Loan has been created 👍"
        else:
            context["form_errors"] = result['form_errors']
  
    context["loans"] = Read('loans')
    context["users"] = Read('users')
    return render(request, 'employees_requests/loans.html', context)

def change_loan_status(request):

    loan_id = request.POST['loan_id'] 
    loan_row = loans_model.objects.get(pk=loan_id) 
    
    if loan_row.loan_is_approved:  
        loan_row.loan_is_approved = False 
    else: 
        loan_row.loan_is_approved = True 

    loan_row.loan_updated_at = timezone.now() 
    loan_row.save() 
    html = "<html><body>Success.</body></html>" 
    return HttpResponse(html)

@login_required
def vacations(request):
    context = {} 

    if request.method == "POST": 
        new_post = request.POST.copy()

        if "vacation_user_id" in request.POST:
            user_idd = request.POST['vacation_user_id']
        else:
            user_idd =  request.user.user_id

        new_post['vacation_user_id'] = user_idd
        
        result = Create(new_post, 'vacations')
        if result["status"] == True:
            context["success_message"] = "Vacation has been created 👍"
        else:
            context["form_errors"] = result['form_errors']
  
    context["vacations"] = Read('vacations')
    context["users"] = Read('users')
    return render(request, 'employees_requests/vacations.html', context)

def change_vacation_status(request):

    vacation_id = request.POST['vacation_id'] 
    vacation_row = vacations_model.objects.get(pk=vacation_id) 
    
    if vacation_row.vacation_is_approved:  
        vacation_row.vacation_is_approved = False 
    else: 
        vacation_row.vacation_is_approved = True 

    vacation_row.vacation_updated_at = timezone.now() 
    vacation_row.save() 
    html = "<html><body>Success.</body></html>" 
    return HttpResponse(html)

def overtime_categories(request):
    context = {}

    if request.method == "POST":

        if request.POST["request_type"] == "delete":
            result = Delete("overtime_categories", request.POST["overtime_category_id"])
            if result['status']:
                print("Deletion Successful")
            else:
                print(result['error'])

        else:
            result = Create(request.POST, 'overtime_categories')
            if result["status"] == True:
                context["success_message"] = "Overtime Category has been created 👍"
            else:
                context["form_errors"] = result['form_errors']

    context["overtime_categories"] = Read('overtime_categories')
    return render(request, 'employees_requests/overtimeCategories.html', context)

def overtime(request):
    context = {}

    if request.method == "POST": 
        
        result = Create(request.POST, 'overtimes')
        if result["status"] == True:
            context["success_message"] = "Overtime has been created 👍"
        else:
            context["form_errors"] = result['form_errors']


    context["overtime_categories"] = Read('overtime_categories')
    context["overtimes"] = Read('overtimes')
    context["users"] = Read('users')
    return render(request, 'employees_requests/overtime.html',context)

def change_overtime_status(request):

    overtime_id = request.POST['overtime_id'] 
    overtime_row = overtime_model.objects.get(pk=overtime_id) 
    if overtime_row.overtime_status:  
        overtime_row.overtime_status = False 
    else: 
        overtime_row.overtime_status = True 

    overtime_row.overtime_updated_at = timezone.now() 
    overtime_row.save()
    html = "<html><body>Success.</body></html>" 
    return HttpResponse(html)