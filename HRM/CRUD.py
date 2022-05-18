from django.utils import timezone
from users.models import users
from job_management.forms import *
from job_management.models import departments, job_titles, contracts
from track_performance.models import evaluations
from track_performance.forms import *
from finance.forms import *
from finance.models import punishments, rewards
from employees_requests.models import loans, vacations, overtime, overtime_categories
from employees_requests.forms import *

# This component manages most of the Create, Read, Update and Delete operations. This component is called from many apps to do the CRUD
# operations on their behalf.

# This function is usually called by the "Create" function, it creates a from for a specific table depending on the "table" variable
def create_form(post, table):

    if table == 'departments':  # if the passed "table" is "departments"

        return(create_department_form(post)) # create a department creation form

    elif table == 'job_titles':
        return(create_job_title_form(post))

    elif table == 'evaluations':
        return(create_evaluation_form(post))

    elif table == 'contracts':
        return(create_contract_form(post))

    elif table == 'annual_bonuses':
        return(create_annual_bonuses_form(post))

    elif table == 'banks_accounts':
        return(create_bank_account_form(post))

    elif table == 'allownces':
        return(create_allowances_form(post))

    elif table == 'rewards':
        return(create_reward(post))

    elif table == 'punishments':
        return(create_punishment(post))

    elif table == 'loans':
        return(create_loan_form(post))

    elif table == 'vacations':
        return(create_vacation_form(post))

    elif table == 'overtime_categories':
        return(create_overtime_category_form(post))

    elif table == 'overtimes':
        return(create_overtime_form(post))

    else:
        print("Table Not Found!! Check if you typed its name correctly.") # debugging alert which means that the table was not found

def fetch_all_rows(table, filter=None): # This function is usually called by the "Read" function, it fetches all rows (except soft-deleted ones) and
    # return them back to the "Read" function

    if table == 'departments': # if the passed "table" is "departments"
        if filter: # checking if there is a constraint on the fetched tables, for example, filter=active_only brings only active departments
            if filter == "active_only":
                return(departments.objects.filter(department_deleted_at=None, department_status=True))
        else:
            return(departments.objects.filter(department_deleted_at=None)) # return all departments rows that have the field
        # department_deleted_at = Null

    elif table == 'job_titles':
        if filter:
            if filter == "active_only":
                return(job_titles.objects.filter(job_title_deleted_at=None, job_title_status=True))
        else:
            return(job_titles.objects.filter(job_title_deleted_at=None))

    elif table == 'evaluations':
        return(evaluations.objects.filter(evaluation_deleted_at=None))

    elif table == 'loans':
        return(loans.objects.filter(loan_deleted_at=None))

    elif table == 'users':
        return(users.objects.filter(user_deleted_at=None))

    elif table == 'rewards':
        return(rewards.objects.filter(reward_deleted_at=None))

    elif table == 'punishments':
        return(punishments.objects.filter(punishment_deleted_at=None))

    elif table == 'contracts':
        return(contracts.objects.filter(contract_deleted_at=None))

    elif table == 'vacations':
        return(vacations.objects.filter(vacation_deleted_at=None))

    elif table == 'overtime_categories':
        return(overtime_categories.objects.filter(overtime_category_deleted_at=None))

    elif table == 'overtimes':
        return(overtime.objects.filter(overtime_deleted_at=None))

    else:
        print("Table Not Found!! Check if you typed its name correctly.")


def fetch_one_row(post, table, primary_key): # This function is usually called by the "Update" function, it fetches one specific row 
    # from a table and returns it to the "Update" function
    
    if table == 'departments': # if the passed "table" is "departments"

        row_to_update = departments.objects.get(pk=primary_key) # use the passed primary key to fetch a single row from the database

        return(create_department_form(post, instance=row_to_update)) # and create a form for that row and return it to the "Update" function

    elif table == 'job_titles':
        row_to_update = job_titles.objects.get(pk=primary_key)
        return (create_job_title_form(post, instance=row_to_update))

    elif table == 'evaluations':
        row_to_update = evaluations.objects.get(pk=primary_key)
        return (create_evaluation_form(post, instance=row_to_update))

    elif table == 'loans':
        row_to_update = loans.objects.get(pk=primary_key)
        return (create_loan_form(post, instance=row_to_update))

    else:
        print("Table Not Found!! Check if you typed its name correctly.")

def change_updated_at_field(table, primary_key): # This function is usually called by the "Update" function, the job of this function is
    # just to change the updated at field for a specfic row
    
    if table == 'departments': # if the passed "table" is "departments"

        row = departments.objects.get(pk=primary_key) # use the passed primary key to select a single row from the database

        row.department_updated_at = timezone.now() # change the updated_at field for that row to the current time

        row.save() # save the change that has been done to the row

    elif table == 'job_titles':
        row = job_titles.objects.get(pk=primary_key)
        row = job_titles.objects.get(pk=primary_key)
        row.job_title_updated_at = timezone.now()
        row.save()

    elif table == 'evaluations':
        row = evaluations.objects.get(pk=primary_key)
        row.evaluation_updated_at = timezone.now()
        row.save()

    elif table == 'loans':
        row = loans.objects.get(pk=primary_key)
        row.loan_updated_at = timezone.now()
        row.save()

    else:
        print("Table Not Found!! Check if you typed its name correctly.")



def Create(post, table): # The Create function, this function is called from the file "views.py" from several apps, it receives the POST
    # array that contains a filled form for a specifc table and the table name to create a new row in that table.

    result = {} # the dictionary variable that will be returned to the calling function after the operation is done

    form = create_form(post, table) # creating a form for the required table using the function "create_form" that was mentioned above

    if form.is_valid(): # checking if the form is valid

        form.save() # if it is valid, save the new row to the database

        result["status"] = True # appending a new element with the value of "True" to the "result" dictionary to show that the operation
        # was successful and there are no validation errors

        return result # returning the result dictionary to the calling function

    else: # if the form is not valid
        result["status"] = False # appending a new element with the value of "False" to the "result" dictionary to show that the operation
        # was unsuccessful and there are validation errors

        result["form_errors"] = form # appending a new element to the result dictionary that contains the form object for the passed table
        # this form object contains the validation errors which will be shown to the user

        return result # returning the result dictionary to the calling function

def Read(table, filter=None): # The Read function, this function is called from the file "views.py" from several apps, it receives the table name
    # and returns all objects for that table that were not deleted

    result = [] # creating the result array that will be returned to the calling function

    rows = fetch_all_rows(table, filter) # calling the "fetch_all_rows" function that will fetch all rows from the database, refer to the function 
    # above
    
    count = 1 # this variable is used to count the number of fetched rows, the numbers are stored in the array here because it is not 
    # possible to create a count variable and incrementing it in the HTML file using template tags.

    for row in rows: # for each row in the "rows" variable, create a dictionary and append the number of the row and the row it self in it

        result.append(
            {
                'info':row,
                'number':count
            }
        )
        count = count + 1

    return result # return the result array to the calling function

def Update(post, table, primary_key): # The Update function, this function is called from the file "views.py" from several apps, it receives 
    # the table name and a primary key with the new information for a row and update that row. 

    result = {} # creating the result array that will be returned to the calling function

    form = fetch_one_row(post, table, primary_key) # calling the "fetch_one_row" function that will fetch one single rows from the database
    # and create an update form for the specifc row, refer to the function above for more info
    
    if form.is_valid(): # checking if the form is valid

        form.save() # if it is valid, update the row in the database

        change_updated_at_field(table, primary_key) # calling the "change_updated_at_field" function that will take a table name and a 
        # primary key and change the updated_at field for that row, refer to the function above for more info

        result['status'] = True # appending a new element with the value of "True" to the "result" dictionary to show that the operation
        # was successful and there are no validation errors

        return(result) # returning the result dictionary to the calling function

    else:
        result['status'] = False # appending a new element with the value of "False" to the "result" dictionary to show that the operation
        # was unsuccessful and there are validation errors

        result['form_errors'] = form # appending a new element to the result dictionary that contains the form object for the passed table
        # this form object contains the validation errors which will be shown to the user

        return(result) # returning the result dictionary to the calling function
    

def Delete(): # The Update function, this function is called from the file "views.py" from several apps, it receives 
    # the table name and a primary key and performs a soft delete on that row, soft deletion does not delete the row, it only changes the 
    # deleted_at field for that row, and when we retreive the rows from that table, we ignore all rows that have deleted_at != Null
    
    pass

