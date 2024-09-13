from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Employee
from .forms import AddEmployeeForm, UpdateEmployeeForm


def home(request):
    # print(request.user)
    employee_list = Employee.objects.all()
    
    # user = str(request.user)
    # if (user == 'AnonymousUser'):

    return render(request, 'home.html', {'user': 'AnonymousUser', 'employees': employee_list})
    
    # return render(request, 'home.html', {'user': 'Admin'})


def add_employee(request):
    if request.method == 'POST':
        new_employee = AddEmployeeForm(request.POST)
        
        if new_employee.is_valid():
            new_employee.save()
            return redirect(home)
        else:
            return render(request, 'employee_form.html', {'employee_form': new_employee})

    return render(request, 'employee_form.html', {'employee_form': AddEmployeeForm()})


def update_employee(request,pk):
    try:
        print(pk)
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
        