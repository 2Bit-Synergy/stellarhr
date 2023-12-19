from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, ContactInformation
from .forms import EmployeeAndContactForm
from django.views.decorators.http import require_POST

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    contact_info = ContactInformation.objects.get(employee=employee)
    return render(request, 'employee_detail.html', {'employee': employee, 'contact_info': contact_info})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeAndContactForm(request.POST)
        if form.is_valid():
            print("asdasd")
             # Create a User instance and save it
  
            employee = form.save(commit=False)
            employee.user = request.user
            employee.save()

            contact_info_data = {
                'employee': employee,
                'address': form.cleaned_data['address'],
                'phone_number': form.cleaned_data['phone_number'],
                'emergency_contact_name': form.cleaned_data['emergency_contact_name'],
                'emergency_contact_number': form.cleaned_data['emergency_contact_number'],
            }
            contact_info = ContactInformation(**contact_info_data)
            contact_info.save()
            return redirect('apps.mployees:employee_list')
    else:
        form = EmployeeAndContactForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    print("ASDSD")
    if request.method == 'POST':
        form = EmployeeAndContactForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            print("asdasdasdasdxxx")
            print(employee)
            # Update contact information using the same form
            # contact_info = ContactInformation.objects.get(employee=employee)
            form_contact = EmployeeAndContactForm(request.POST, instance=employee)
            form_contact.save()
            return redirect('apps.employees:employee_list')
    else:
        # Populate the forms with existing data for the GET request
        print(employee)
        form = EmployeeAndContactForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form, 'employee': employee})