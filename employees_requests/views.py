from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponse
from HRM.CRUD import *
from datetime import datetime
from .models import loans as loans_model

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

    loan_row.department_updated_at = timezone.now() 
    loan_row.save() 
    html = "<html><body>Success.</body></html>" 
    return HttpResponse(html) 

