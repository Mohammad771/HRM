from job_management.forms import create_department_form
from distutils.log import error
from pprint import pprint
from job_management.forms import *
from job_management.models import *

def create_form(post, table):
        
    return {
        'department':create_department_form(post),
        'b': 2,
    }[table]

def fetch_data(table):
        
    return {
        'departments':departments.objects.all(),
        'b': 2,
    }[table]

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
    rows = fetch_data(table)
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

def Update():
    pass

def Delete():
    pass

