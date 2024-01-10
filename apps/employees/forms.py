from django import forms
from .models import Department, Company, Position, Employee, EmploymentHistory, ContactInformation
from apps.accounts import models as AccountModel



class RegisterEmployeeForm(forms.ModelForm):
    class Meta:
        model = AccountModel.User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = AccountModel.User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        
       
class EmployeeDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('employee_id_no', 'date_of_birth', 'department', 'position', 'manager_id')
        
class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        

class EmploymentHistoryForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = '__all__'
        
class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = '__all__'