from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.accounts.models import User
from .models import Employee, EmploymentHistory,ContactInformation
from .views import manage_employee_data


@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        employee = Employee.objects.create(user_id=instance)
        print("Employee Profile Created")
        
        EmploymentHistory.objects.create(employee_id=employee)
        print("EmploymentHistory Created")
        
        ContactInformation.objects.create(employee_id=employee)
        print("ContactInformation Created")
        

# @receiver(post_save, sender=User)
# def save_employee(sender, instance, **kwargs):
#     instance.employee.save()
#     print("Employee Profile Saved")
    
# @receiver(post_save, sender=Employee)
# def create_employment_history(sender, instance, created, **kwargs):
#     if created:
#         employment_history = EmploymentHistory.objects.create(employee_id=instance)
#         employment_history.save()
#         print("EmploymentHistory Created and Saved")

# @receiver(post_save, sender=Employee)
# def create_contact_information(sender, instance, created, **kwargs):
#     if created:
#         contact_information = ContactInformation.objects.create(employee_id=instance)
#         contact_information.save()
#         print("ContactInformation Created and Saved")