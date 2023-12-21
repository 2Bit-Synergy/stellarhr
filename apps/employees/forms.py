from django import forms
from .models import Department, Company, Position, Employee, EmploymentHistory, ContactInformation


class CreateEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
