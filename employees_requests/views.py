from django.shortcuts import render

# Create your views here.

def loans(request):
    return render(request, 'employees_requests/loans.html')
