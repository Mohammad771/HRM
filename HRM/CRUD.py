from job_management.forms import create_department_form, create_job_title_form
from distutils.log import error
from pprint import pprint
from job_management.forms import *
from job_management.models import *

def create_form(post, table):

    if table == 'departments':
        return(create_department_form(post))

    elif table == 'job_titles':
        return(create_job_title_form(post))

    else:
        print("Table Not Found!! Check if you typed its name correctly.")

def fetch_all_rows(table):
    
    if table == 'departments':
        return(departments.objects.all())

    elif table == 'job_titles':
        return(job_titles.objects.all())

    else:
        print("Table Not Found!! Check if you typed its name correctly.")


def fetch_one_row(post, table, primary_key):
    
    if table == 'departments':
        return(create_department_form(post, instance=job_titles.objects.get(pk=primary_key)))

    elif table == 'job_titles':
        return(create_job_title_form(post, instance=job_titles.objects.get(pk=primary_key)))

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
        result["form"] = form
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

def Update(post, table, row_id):
    result = {}

    job_title_form = fetch_one_row(post, table, row_id)
    
    if job_title_form.is_valid():
        job_title_form.save()
        result['status'] = True
        return(result)
    else:
        result['status'] = False
        result['form_errors':job_title_form.errors]
        return(result)
    

def Delete():
    pass

