from django.urls import include, path
from apps.hrperformance.views import AttendanceRecordView

urlpatterns = [
    # path('my-dashboard', AttendanceRecordView.as_view(), name="my_dashboard")
    path('test', AttendanceRecordView.as_view(), name="my_dashboard")
]