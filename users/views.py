from django.shortcuts import redirect, render
from .froms import login_form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def user_login(request):

    if request.method == "POST":
        email = request.POST.get('login_email')
        password = request.POST.get('login_password')

        user = authenticate(email=email, password=password)
        print(user)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('/dashboard')

            else:
                print("User is not yet activated")
        
        else: 
            print("incorrect credentials")
    
    else:
        return render(request, 'users/login.html')

 

@login_required
def user_logout(request):
    logout(request)
    return redirect('/')




def register(request): 

    # authenticated = False

    # if request.method == "POST":
    #     login_info = login_form(data=request.POST)
    #     if login_info.is_valid():
    #         user = login_info.save()
    #         user.set_password(user.password)
    #         user.save()

    #         authenticated = True

    #     else:
    #         print(login_form.errors)
    # else:
        
    #     loginForm = login_form()


    return render(request, 'users/register.html',)
    #  {
    #     'login_form':loginForm,
    #     'authenticated':authenticated
    # })
    

def dashboard(request):
    return render(request, 'users/dashboard.html')


def viewUsers(request):
    return render(request, 'users/viewUsers.html')
