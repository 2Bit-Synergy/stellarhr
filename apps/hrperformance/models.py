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
    timein = models.DateTimeField()
    timeout = models.DateTimeField()
    type = models.ForeignKey(TimeLogType, on_delete=models.CASCADE, max_length=100, blank=True, null=True) 




