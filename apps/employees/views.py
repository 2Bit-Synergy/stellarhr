from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import CreateEmployeeForm
from .models import Employee

# Create your views here.


class CreateEmployeeView(CreateView):
    model = Employee
    form_class = CreateEmployeeForm
    template_name = 'create-employee.html'
    
# def create_employee(request):
#     if request.method == "POST":
#         form = CreateEmployeeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Added Employee Successfully', extra_tags='success')
#             return redirect('employee_list')
        
#     else:
#         form = CreateEmployeeForm()
        
#     context = {
#         'form':form
#     }
    
#     return render(request, template_name='create-employee.html', context=context)
    


# def create_employee(request):
#     return render(request, template_name='create-employee.html')


def update_employee(request):
    return render(request, template_name='update-employee.html')

def delete_employee(request):
    return render(request, template_name='delete-employee.html')

def employee_list(request):
    return render(request, template_name='employee-list.html')