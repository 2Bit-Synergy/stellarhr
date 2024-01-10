from django.db import models
from apps.accounts import models as AccountModels
# Create your models here.

#ADMIN MODELS
class Department(models.Model):
    department_name = models.CharField(max_length=50, blank=True, null=True)
    department_code = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.department_name} Department"
    
class Position(models.Model):
    position_name = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.position_name}"
    
class Company(models.Model):
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_address = models.CharField(max_length=50, blank=True, null=True)
    
    
#USER MODELS
class Employee(models.Model):
    user_id = models.OneToOneField(AccountModels.User, on_delete=models.CASCADE)
    employee_id_no = models.IntegerField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, blank=True, null=True)
    manager_id = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.user_id.first_name} {self.user_id.last_name}'s Employee Profile"
    

class EmploymentHistory(models.Model):
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.employee_id.user_id.first_name} {self.employee_id.user_id.last_name}'s Employment History"
    
    
class ContactInformation(models.Model):
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_name = models.CharField(max_length=50, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return f"{self.employee_id.user_id.first_name} {self.employee_id.user_id.last_name}'s Contact Information"
    
