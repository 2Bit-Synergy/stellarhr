from django.contrib import admin
from apps.hrperformance.models import AttendanceRecord, TimeLogType



admin.site.register(TimeLogType)
admin.site.register(AttendanceRecord)
