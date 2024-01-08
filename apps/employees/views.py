from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import CreateEmployeeForm, EmploymentHistoryForm, ContactInformationForm, RegisterEmployeeForm, UserDetailsUpdateForm, EmployeeDetailsUpdateForm
from .models import Employee
from apps.accounts import models as AccountModels
from apps.accounts import forms as AccountForms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from apps.accounts.models import User




# Create your views here.

def register_employee(request):
    if request.method == "POST":
        register_form = RegisterEmployeeForm(request.POST)
        if register_form.is_valid():
            employee_instance = register_form.save()
            details_form = EmployeeDetailsUpdateForm(request.POST, instance=employee_instance)
            if details_form.is_valid():
                details_form.save()
                return redirect('apps.employees:employee_list')
            else:
                print("Opps details_form is not valid ")
                
        else:
            print("Opps register_form is not valid ")       
    else:
        register_form = RegisterEmployeeForm()
        details_form = EmployeeDetailsUpdateForm()
        
    context = {
        'register_form': register_form,
        'details_form': details_form
    }
    
    return render(request, 'register-employee.html', context)






def manage_employee_data(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        form1 = UserDetailsUpdateForm(request.POST, instance=user.id)
        form2 = EmployeeDetailsUpdateForm(request.POST, instance=request.user.id)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('apps.employees:manage_employee_data')
    
    else:
        form1 = UserDetailsUpdateForm(instance=request.user)
        employee_instance = get_object_or_404(Employee, user_id=request.user)
        form2 = EmployeeDetailsUpdateForm(instance=request.user.employee_instance)
    
    return render(request, 'manage-employee-data.html')

# CONTINUE HERE!!!


# def RegisterEmployeeView(request):
#     if request.method == "POST":
#         user_form =  AccountForms.UserForm(request.POST)
#         create_employee_form = CreateEmployeeForm(request.POST)
#         employment_history_form = EmploymentHistoryForm(request.POST)
#         contact_info_form = ContactInformationForm(request.POST)
#         if user_form.is_valid() and create_employee_form.is_valid() and employment_history_form.is_valid() and contact_info_form.is_valid():
#             user = user_form.save()
#             employee = create_employee_form.save(commit=False)
#             history = employment_history_form.save(commit=False)
#             contact = contact_info_form.save(commit=False)
            
#             employee.user_id = user
#             history.employee_id = employee
#             contact.employee_id = employee
            
#             employee.save()
#             history.save()
#             contact.save()
            
#             return redirect('manage_employee_data')
        
#         else:
#             print(user_form.errors)
#             print(create_employee_form.errors)
#             print(employment_history_form.errors)
#             print(contact_info_form.errors)
    
#     else:
#         user_form =  AccountForms.UserForm()
#         create_employee_form = CreateEmployeeForm()
#         employment_history_form = EmploymentHistoryForm()
#         contact_info_form = ContactInformationForm()
            
#     context = {
#         'user_form':user_form,
#         'create_employee_form':create_employee_form,
#         'employment_history_form':employment_history_form,
#         'contact_info_form':contact_info_form,
        
#     }
    
#     return render(request, 'register-employee.html', context=context)





def delete_employee(request):
    return render(request, template_name='delete-employee.html')

def employee_list(request):
    users = User.objects.all()
    
    context = {
        'users': users
    }
    return render(request, 'employee-list.html', context)


def employee_data(request, id):
    employee = User.objects.get(id=id)
    
    context = {
        'employee': employee
    }
    return render(request, 'employee-data.html', context)