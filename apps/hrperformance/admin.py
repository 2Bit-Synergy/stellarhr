from django.contrib import admin
from apps.hrperformance.models import AttendanceRecord, TimeLogType, HRSetting, Recognition, Offense



admin.site.register(TimeLogType)
admin.site.register(AttendanceRecord)
admin.site.register(HRSetting)
admin.site.register(Recognition)
admin.site.register(Offense)

