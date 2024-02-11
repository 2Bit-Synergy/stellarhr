from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import CreateEmployeeForm, EmploymentHistoryForm, ContactInformationForm, RegisterEmployeeForm, UserDetailsUpdateForm, EmployeeDetailsUpdateForm
from .models import Employee
from apps.accounts import models as AccountModels
from apps.accounts import forms as AccountForms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from apps.accounts.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.views.generic import TemplateView, View, DeleteView







# Create your views here.



def register_employee(request):
    if request.method == "POST":
        register_form = RegisterEmployeeForm(request.POST)
        if register_form.is_valid():
            employee_instance = register_form.save()
            details_form = EmployeeDetailsUpdateForm(request.POST, instance=employee_instance)
            if details_form.is_valid():
                details_form.save()
                messages.success(request, 'Employee added successfully.', extra_tags='success')
                return redirect('apps.employees:employee_data', id=employee_instance.id)
            else:
                print("Opps details_form is not valid ")
                print(details_form.errors)
                
        else:
            print("Opps register_form is not valid ")       
    else:
        register_form = RegisterEmployeeForm()
        
    context = {
        'register_form': register_form,

    }
    
    return render(request, 'register-employee.html', context)





def manage_employee_data(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        user_form = UserDetailsUpdateForm(request.POST, instance=user)
        employee_data_form = EmployeeDetailsUpdateForm(request.POST, instance=user.employee)
        employee_emp_history_form = EmploymentHistoryForm(request.POST, instance=user.employee.employmenthistory)
        employee_contact_info_form = ContactInformationForm(request.POST, instance=user.employee.contactinformation)
        
        if user_form.is_valid() and employee_data_form.is_valid() and employee_emp_history_form.is_valid and employee_contact_info_form.is_valid():
            user_form.save()
            employee_data_form.save()
            employee_emp_history_form.save()
            employee_contact_info_form.save()
            messages.success(request, 'Employee updated successfully.', extra_tags='info')
            return redirect('apps.employees:employee_data', id=user.id)
    
    else:
        user_form = UserDetailsUpdateForm(instance=user)
        employee_data_form = EmployeeDetailsUpdateForm(instance=user.employee)
        employee_emp_history_form = EmploymentHistoryForm(instance=user.employee.employmenthistory)
        employee_contact_info_form = ContactInformationForm(instance=user.employee.contactinformation)
        
    context = {
        'user_form':user_form,
        'employee_data_form':employee_data_form,
        'employee_emp_history_form': employee_emp_history_form,
        'employee_contact_info_form':employee_contact_info_form
        
    }
    
    return render(request, 'manage-employee-data.html', context)



# def delete_employee(request, id):
#     user = User.objects.get(id=id)
#     if request.method == "POST":
#         user.delete()
#         messages.success(request, 'Employee deleted.', extra_tags='warning')
#         return redirect('apps.employees:employee_list')
        
#     context = {
#         'user':user,
#     }
    
#     return render(request, 'delete-employee.html', context)




class DeleteEmployee(View):
    def get(self, request):
        id = request.GET.get('id', None)
        User.objects.get(id=id).delete()
        
        data = {
            'deleted':True
        }
        
        return JsonResponse(data)


def employee_list(request):
    users = User.objects.all()
    
    context = {
        'users': users
    }
    return render(request, 'employee-list.html', context)


def employee_data(request, id):
    user = User.objects.get(id=id)
    
    context = {
        'user': user
    }
    return render(request, 'employee-data.html', context)



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





# def register_employee(request):
#     if request.method == "POST":
#         register_form = RegisterEmployeeForm(request.POST)
#         if register_form.is_valid():
#             employee_instance = register_form.save()
#             details_form = EmployeeDetailsUpdateForm(request.POST, instance=employee_instance)
#             if details_form.is_valid():
#                 details_form.save()
#                 return redirect('apps.employees:employee_data', id=employee_instance.id)
#             else:
#                 print("Opps details_form is not valid ")
                
#         else:
#             print("Opps register_form is not valid ")       
#     else:
#         register_form = RegisterEmployeeForm()
#         details_form = EmployeeDetailsUpdateForm()
        
#     context = {
#         'register_form': register_form,
#         'details_form': details_form
#     }
    
#     return render(request, 'register-employee.html', context)
