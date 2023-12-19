from django.db import models

from apps.account.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    join_date = models.DateField()
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    # Add more fields based on your specific requirements

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class ContactInformation(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_number = models.CharField(max_length=15)
    # Add more contact-related fields as needed

class EmploymentHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=100)
    job_title = models.CharField(max_length=50)
    responsibilities = models.TextField()
    