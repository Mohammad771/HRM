from distutils.log import error
from django.shortcuts import redirect, render, HttpResponse 
from pprint import pprint
from HRM.CRUD import *
from .models import job_titles as job_titles_model
from .models import departments as departments_model


# This is the function which is responsible for all crud operations for the departments table
def departments_handler(request): 
    context = {} # Declaring the variable which will be sent to the html file

    if request.method == "POST": # if the received request is "POST", it means that the user wants to add or update a department
        if request.POST['request_type'] == "update": 
            department_id = request.POST['department_id'] 
            result = Update(request.POST, "departments", department_id) 

            if result['status'] == False: 
                context["form_errors"] = result['form_errors']
            
        else:
            result = Create(request.POST, 'departments') # The "Create" functinon takes the post array (which contains a create department
        #  form which was filled by the user) and the table name and adds a new row to the DB, this function returns an array
        #  that contains the status of the operation and the form validation errors if any

        if result["status"] == True: # checking if the create operation was successful
            context["success_message"] = "Department has been added 👍" # inserting a success message in the context variable 
             
        else:
            print(result['form_errors'])
            context["form_errors"] = result['form_errors'] # if the create operation failed, the errors are taken from the the array
            # that was returned from the "Create" function and put inside the context dictionary
            print(context)

    context['departments'] = Read('departments')  # creating a new element (departments) in the context dictionary that will contain
    #  all departments records from the database, the function "Read" takes the table name as input and returns all database records  
    #  for that table, this function is defined in HRM/CRUD.py file 
    return render(request, 'job_management/departments.html', context) # rendering the departments.html file and passing the context variable 
         # which contains all the departments rows and any other success or error messages 


# This is the function which is responsible for all crud operations for the job_titles table, please refer to the above departments_handler
#  function for any uncommented line in the job_titles_handler function, because they are the same.
def job_titles_handler(request):
    context = {} 

    if request.method == "POST": 

        if request.POST['request_type'] == "update": 
            job_title_id = request.POST['job_title_id'] 
            result = Update(request.POST, "job_titles", job_title_id) 

            if result['status'] == False: 
                context["form_errors"] = result['form_errors'] 

        else:
            result = Create(request.POST, 'job_titles')
            if result["status"] == True:
                context["success_message"] = "Job Title has been added 👍"
            else:
                context["form_errors"] = result['form']
  
    context['departments'] = Read('departments') # Here, we are sending the departments rows because we need to list the
    # departments in the job title creation form so the user can select the department which the job title will be under
    context["job_titles"] = Read('job_titles')
    return render(request, 'job_management/job_titles.html', context)


# this function has only one job, which is to change the job title status when the checkbox in the job titles table is clicked,
# this function receives a post request sent by ajax function (you can take a look in the job_titles.html file)
def change_job_title_status(request):

    job_title_id = request.POST['job_title_id'] # get the id of the job title to be changed
    switch = request.POST['switch'] # check if the user wants to activate or deativate the job title
    Job_title = job_titles_model.objects.get(pk=job_title_id) # fetch the job title row that the user wants to change
    
    if switch == "make_active":  # if user wants to make the job title active
        Job_title.job_title_status = True # activate the jobtitle
    else: # if user wants to make the job title inactive
        Job_title.job_title_status = False # deactivate the jobtitle

    Job_title.department_updated_at = timezone.now() # changing the "department_updated_at" field for this row to the current date and time
    Job_title.save() # saving the changes
    
    html = "<html><body>Success.</body></html>" # a variable that contains a success message to be sent as an http respone back to ajax function
    return HttpResponse(html) # returning "success" as an http response because an error is produced when noting is returned.

# Please refer to the above change_job_title_status function, because the beloew function does the same but for a job title
def change_department_status(request):
    department_id = request.POST['department_id']
    switch = request.POST['switch']
    department = departments_model.objects.get(pk=department_id)

    if switch == "make_active":
        department.department_status = True
    else:
        department.department_status = False

    department.department_updated_at = timezone.now()
    department.save()

    html = "<html><body>Success.</body></html>"
    return HttpResponse(html)
    

def create_contract(request):
    return render(request, 'job_management/create_contract.html')

def viewContract(request):
    return render(request, 'job_management/viewContract.html')