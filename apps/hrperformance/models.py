from django.db import models
from apps.employees.models import Employee
from django.utils import timezone




#SET BY ADMIN TO DEFINE WHAT TYPE OF TIME-IN or TIME-OUT (TO DIFFERENTIATE BUSINESS AND NORMAL TIME LOGS)
#POSSIBLE CHOICE: Normal, Business
#MIGHT NOT REQUIRE FRONT-END ADMIN (JUST USE DJANGO's DEFAULT ADMIN)
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
    
    
# COMPANY SETTING TO WORK WITH LATES AND OVERTIME
class HRSetting(models.Model):
    timein_setpoint = models.TimeField(null=True)
    timeout_setpoint = models.TimeField(null=True)
    break_time_start = models.TimeField(null=True)
    break_time_end = models.TimeField(null=True)
    awol_setpoint = models.TimeField(null=True)
    late_offense_verbalwarning = models.IntegerField(null=True)
    late_offense_writtenwarning = models.IntegerField(null=True)
    late_offense_suspension = models.IntegerField(null=True)
    awol_offense_verbalwarning = models.IntegerField(null=True)
    awol_offense_writtenwarning = models.IntegerField(null=True)
    awol_offense_suspension = models.IntegerField(null=True)
    # last_updated = models.DateTimeField()
    # updated_by = models.ForeignKey(User)



class Offense(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    type = models.CharField(null=True)
    date = models.DateTimeField(blank=True, null=True)
    description = models.CharField(null=True)
    status = models.CharField(null=True)
    
    def __str__(self):
        return f"{self.employee.user_id.first_name} {self.type}: {self.description}"


class Recognition(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True)
    title = models.CharField(null=True)
    description = models.TextField(null=True)
    
    def __str__(self):
        return f"{self.employee.user_id.first_name} {self.title} {self.description}"
    

# THIS MODEL IS FOR OPERATIONAL KPI ACHIEVEMENT
# class Achievement(models.Model)
    
    
