from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

from .models import Employee
from .forms import AddEmployeeForm, UpdateEmployeeForm



def home(request):
    request.session['last_page'] = 'home'
    print(request.session['last_page'])
    employee_list = Employee.objects.all()
    return render(request, 'home.html', {'employees': employee_list})
   
def authorize_admin(request):
    user = str(request.user)
    # print(user)
    last_page = request.session.get('last_page', None)
    if user != 'admin':
        login_form = AuthenticationForm()

        if request.method == 'POST':
            login_form = AuthenticationForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)

                print(last_page)
                if last_page == 'home':
                    return redirect(home)
                elif last_page == 'add':
                    return redirect(add_employee)
                elif last_page == 'update':
                    return redirect(update_employee_list)
            
        return render(request, 'login.html', {'login_form': login_form})
    
    # If you accidently pressed login & already logged in, then it just redirects you to the last page.
    if last_page == 'home':
        return redirect(home)
    elif last_page == 'add':
        return redirect(add_employee)
    elif last_page == 'update':
        return redirect(update_employee_list)
    

def unauthorize_admin(request):
    logout(request)
    return redirect(home)

def add_employee(request):
    user = str(request.user)
    if user != 'admin':
        request.session['last_page'] = 'add'
        return redirect(authorize_admin)
    
    if request.method == 'POST':
        new_employee = AddEmployeeForm(request.POST)
        
        if new_employee.is_valid():
            new_employee.save()
            return redirect(home)
        else:
            return render(request, 'employee_form.html', {'employee_form': new_employee})

    return render(request, 'employee_form.html', {'employee_form': AddEmployeeForm()})


def update_employee_list(request):
    user = str(request.user)
    if user != 'admin':
        request.session['last_page'] = 'update'
        return redirect(authorize_admin)
        # login_form = AuthenticationForm()

        # if request.method == 'POST':
        #     login_form = AuthenticationForm(data=request.POST)
        #     if login_form.is_valid():
        #         user = login_form.get_user()
        #         print(user)
        #         login(request, user)
        #         return redirect(update_employee_list)
            
        # return render(request, 'login.html', {'login_form': login_form})

    employee_list = Employee.objects.all()
    return render(request, 'update_employee.html',  {'employees': employee_list})


def update_an_employee(request,pk):
    user = str(request.user)
    if user != 'admin':
        # return redirect()
        return render(request, 'not_admin.html', {'user': user})
    
    try:
        # print(pk)
        employee = Employee.objects.get(pk=pk)
        update_employee_form = UpdateEmployeeForm(instance=employee)

        if request.method == 'POST':
            updated_employee = UpdateEmployeeForm(request.POST, instance=employee)
            
            if updated_employee.is_valid():
                updated_employee.save()
                return redirect(home)
            else:
                return render(request, 'employee_form.html', {'employee_form': updated_employee})
        
        return render(request, 'employee_form.html', {'employee_form': update_employee_form})

    except Employee.DoesNotExist:
        return HttpResponse('No employee exists by the given id')
        