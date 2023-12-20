from django.db import models

# Create your models here.


class Departments(models.Model):
    department_name = models.CharField(max_length=50, blank=True, null=True)
    department_code = models.CharField(max_length=50, blank=True, null=True)
    
class Companies(models.Model):
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_address = models.CharField(max_length=50, blank=True, null=True)
    
class Positions(models.Model):
    position_name = models.CharField(max_length=50, blank=True, null=True)
    
    
    
    
class Employees(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Departments, on_delete=models.SET_NULL, blank=True, null=True)
    position = models.ForeignKey(Positions, on_delete=models.SET_NULL, blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    

class EmploymentHistory(models.Model):
    employee_id = models.OneToOneField(Employees, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Companies, on_delete=models.SET_NULL, blank=True, null=True)
    
    
class ContactInformation(models.Model):
    employee_id = models.OneToOneField(Employees, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=50, blank=True, null=True)
    
