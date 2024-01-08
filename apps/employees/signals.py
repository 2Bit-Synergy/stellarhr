from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.accounts.models import User
from .models import Employee
from .views import manage_employee_data


@receiver(post_save, sender=User)
def create_employee(sender, instance, created, **kwargs):
    if created:
        Employee.objects.create(user_id=instance)
        print("Employee Profile Created")
        

@receiver(post_save, sender=User)
def save_employee(sender, instance, **kwargs):
    instance.employee.save()
    print("Employee Profile Saved")