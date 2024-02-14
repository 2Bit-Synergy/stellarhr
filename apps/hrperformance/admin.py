from django.contrib import admin
from apps.hrperformance.models import AttendanceRecord, TimeLogType, HRSetting



admin.site.register(TimeLogType)
admin.site.register(AttendanceRecord)
admin.site.register(HRSetting)
