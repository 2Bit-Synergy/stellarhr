from django.urls import include, path
from apps.hrperformance.views import AttendanceRecordView, HRSettingUpdateView, OffenseCreateView
from . import views

urlpatterns = [
    # path('my-dashboard', AttendanceRecordView.as_view(), name="my_dashboard")
    path('my-attendance', AttendanceRecordView.as_view(), name="my_dashboard"),
    path('hr-settings/', HRSettingUpdateView.as_view(), name="hr_settings"),
    path('temporary-success-url/', views.temporary_success_url, name='temporary_sucess_url'),
    path('log-offense/<int:id>/', OffenseCreateView.as_view(), name="log_offense")
]