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





# def manage_employee_data(request, id):
#     user = User.objects.get(id=id)
#     if request.method == "POST":
#         user_form = UserDetailsUpdateForm(request.POST, instance=user)
#         employee_data_form = EmployeeDetailsUpdateForm(request.POST, instance=user.employee)
#         employee_emp_history_form = EmploymentHistoryForm(request.POST, instance=user.employee.employmenthistory)
#         employee_contact_info_form = ContactInformationForm(request.POST, instance=user.employee.contactinformation)
        
#         if user_form.is_valid() and employee_data_form.is_valid() and employee_emp_history_form.is_valid and employee_contact_info_form.is_valid():
#             user_form.save()
#             employee_data_form.save()
#             employee_emp_history_form.save()
#             employee_contact_info_form.save()
#             messages.success(request, 'Employee updated successfully.', extra_tags='info')
#             return redirect('apps.employees:employee_data', id=user.id)
    
#     else:
#         user_form = UserDetailsUpdateForm(instance=user)
#         employee_data_form = EmployeeDetailsUpdateForm(instance=user.employee)
#         employee_emp_history_form = EmploymentHistoryForm(instance=user.employee.employmenthistory)
#         employee_contact_info_form = ContactInformationForm(instance=user.employee.contactinformation)
        
#     employee = {'username':user_form.username, 'password':user_form.password, 'first_name':user_form.first_name, 'last_name':user_form.last_name, 'email':user_form.email}    
#     context = {
#         'user_form':user_form,
#         'employee_data_form':employee_data_form,
#         'employee_emp_history_form': employee_emp_history_form,
#         'employee_contact_info_form':employee_contact_info_form,
#         'user':user
        
#     }
    
#     return JsonResponse(employee)
    




def manage_employee_data(request, id):
    user = User.objects.get(id=id)
    
    if request.is_ajax() and request.method == 'GET':
        data = {
            'username': user.username,
            'password': user.password,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            }
        
        return JsonResponse(data)
    
   
    
    
    


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




        
        

class EmployeeData(View):
    def get(self, request, id):
        try:
            employee = User.objects.get(id=id)
            username = employee.username
            password = employee.password
            first_name = employee.first_name
            last_name = employee.last_name
            email = employee.email
            id_no = employee.employee.employee_id_no
            date_of_birth = employee.employee.date_of_birth
            department = employee.employee.department
            position = employee.employee.position
            manager = employee.employee.manager_id
            start_date = employee.employee.employmenthistory.start_date
            end_date = employee.employee.employmenthistory.end_date
            company = employee.employee.employmenthistory.company
            address = employee.employee.contactinformation.address
            phone_number = employee.employee.contactinformation.phone_number
            emergency_contact = employee.employee.contactinformation.emergency_contact_name
            emergency_no = employee.employee.contactinformation.emergency_contact_number

            
            
            
            
            data = {
                'username':username,
                'first_name':first_name,
                'last_name':last_name,
                'email':email,
                'password':password,              
                'id_no':id_no,
                'date_of_birth':date_of_birth,
                'department': department,
                'position': position,
                'manager': manager,
                'start_date': start_date,
                'end_date': end_date,
                'company': company,
                'address': address,
                'phone_number': phone_number,
                'emergency_contact': emergency_contact,
                'emergency_no':emergency_no
            }

            
            return JsonResponse(data)
        
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
            
            




def employee_data(request, id):
    user = User.objects.get(id=id)
    
    context = {
        'user': user
    }
    return render(request, 'employee-data.html', context)


