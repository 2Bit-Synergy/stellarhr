from django.db import models
from apps.employees.models import Employee
from django.utils import timezone




#SET BY ADMIN TO DEFINE WHAT TYPE OF TIME-IN or TIME-OUT (TO DIFFERENTIATE BUSINESS AND NORMAL TIME LOGS)
#POSSIBLE CHOICE: Normal, Business
class TimeLogType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=400, blank=True, null=True)
    
    def __str__(self):
        return self.name
     
     
class AttendanceRecord(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    timein = models.DateTimeField(null=True)
    timeout = models.DateTimeField(null=True)
    type = models.ForeignKey(TimeLogType, on_delete=models.CASCADE, max_length=100, default=1, blank=True, null=True)
    
    def __str__(self):
        return f"{self.employee.user_id.first_name} {self.employee.user_id.last_name}: {self.timein.date()}"




