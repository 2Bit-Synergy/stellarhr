from django.urls import include, path
from apps.hrperformance.views import AttendanceRecordView, HRSettingView

urlpatterns = [
    # path('my-dashboard', AttendanceRecordView.as_view(), name="my_dashboard")
    path('my-attendance', AttendanceRecordView.as_view(), name="my_dashboard"),
    path('hr-settings', HRSettingView.as_view(), name="hr_settings")
]