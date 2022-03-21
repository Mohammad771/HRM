from job_management.forms import create_department_form, create_job_title_form
from distutils.log import error
from django.utils import timezone
from job_management.forms import *
from job_management.models import departments, job_titles
from track_performance.models import evaluations
from track_performance.forms import *
from users.models import users

def create_form(post, table):

    if table == 'departments':
        return(create_department_form(post))

    elif table == 'job_titles':
        return(create_job_title_form(post))

    elif table == 'evaluations':
        return(create_evaluation_form(post))

    else:
        print("Table Not Found!! Check if you typed its name correctly.")

def fetch_all_rows(table):
    
    if table == 'departments':
        return(departments.objects.filter(department_deleted_at=None))

    elif table == 'job_titles':
        return(job_titles.objects.filter(job_title_deleted_at=None))

    elif table == 'evaluations':
        return(evaluations.objects.filter(evaluation_deleted_at=None))

    elif table == 'users':
        return(users.objects.filter(user_deleted_at=None))

    else:
        print("Table Not Found!! Check if you typed its name correctly.")


def fetch_one_row(post, table, primary_key):
    
    if table == 'departments':
        row_to_update = departments.objects.get(pk=primary_key)
        return(create_department_form(post, instance=row_to_update))

    elif table == 'job_titles':
        row_to_update = job_titles.objects.get(pk=primary_key)
        return (create_job_title_form(post, instance=row_to_update))

    elif table == 'evaluations':
        row_to_update = evaluations.objects.get(pk=primary_key)
        return (create_evaluation_form(post, instance=row_to_update))

    else:
        print("Table Not Found!! Check if you typed its name correctly.")

def change_updated_at_field(table, primary_key):
    
    if table == 'departments':
        row = departments.objects.get(pk=primary_key)
        row.department_updated_at = timezone.now()
        row.save()

    elif table == 'job_titles':
        row = job_titles.objects.get(pk=primary_key)
        row.job_title_updated_at = timezone.now()
        row.save()

    elif table == 'evaluations':
        row = evaluations.objects.get(pk=primary_key)
        row.evaluation_updated_at = timezone.now()
        row.save()

    else:
        print("Table Not Found!! Check if you typed its name correctly.")



def Create(post, table):
    result = {}
    form = create_form(post, table)
    if form.is_valid():
        form.save()
        result["status"] = True
        return result
    else:
        result["status"] = False
        result["form_errors"] = form
        return result

def Read(table):
    rows = fetch_all_rows(table)
    arr = []
    count = 1
    for row in rows:
        arr.append(
            {
                'info':row,
                'number':count
            }
        )
        count = count + 1
    return arr

def Update(post, table, primary_key):
    result = {}

    form = fetch_one_row(post, table, primary_key)
    
    if form.is_valid():
        form.save()
        change_updated_at_field(table, primary_key)
        result['status'] = True
        return(result)
    else:
        result['status'] = False
        result['form_errors'] = form
        return(result)
    

def Delete():
    pass

