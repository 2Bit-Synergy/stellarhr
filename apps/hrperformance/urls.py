from django.urls import include, path
from apps.hrperformance.views import AttendanceRecordDeleteView, AttendanceRecordEditView, AttendanceRecordDetailView, AttendanceSummaryView, RecognitionSummaryView, RecognitionDetailView, RecognitionDeleteView, RecognitionUdpateView, RecognitionCreateView, AttendanceRecordView, HRSettingUpdateView, OffenseCreateView, OffenseDetailView, OffenseDeleteView, OffenseSummaryView, OffenseUpdateView
from . import views

urlpatterns = [
    #ATTENDNACE RECORD
    path('my-attendance', AttendanceRecordView.as_view(), name="my_dashboard"),
    path('attendance-summary', AttendanceSummaryView.as_view(), name="attendance_summary"),
    path('attendance-detail/<int:pk>/', AttendanceRecordDetailView.as_view(), name='attendance_detail'),
    path('edit-attendance-record/<int:pk>/', AttendanceRecordEditView.as_view(), name="edit_attendance_record"),
    path('delete-attendance-record/<int:pk>/', AttendanceRecordDeleteView.as_view(), name="delete_attendance_record"),

    
    #HR SETTINGS
    path('hr-settings/', HRSettingUpdateView.as_view(), name="hr_settings"),
    
    #OFFENSE
    path('log-offense/<int:id>/', OffenseCreateView.as_view(), name="log_offense"),
    path('delete-offense/<int:pk>/', OffenseDeleteView.as_view(), name="delete_offense"),
    path('update-offense/<int:pk>/', OffenseUpdateView.as_view(), name="update_offense"),
    path('offense-summary', OffenseSummaryView.as_view(), name="offense_summary"),
    path('log-offense/<int:id>/', OffenseCreateView.as_view(), name="log_offense"),
    path('update-detail/<int:pk>/', OffenseDetailView.as_view(), name="offense_detail"),

    #RECOGNITION
    path('add-recognition', RecognitionCreateView.as_view(), name="add_recognition"),
    path('update-recognition/<int:pk>/', RecognitionUdpateView.as_view(), name="update_recognition"),
    path('delete-recognition/<int:pk>/', RecognitionDeleteView.as_view(), name="delete_recognition"),
    path('recognition-detail/<int:pk>/', RecognitionDetailView.as_view(), name="recognition_detail"),
    path('recognition-summary', RecognitionSummaryView.as_view(), name="recognition_summary"),

    
    #TEMPORARY
    path('temporary-success-url/', views.temporary_success_url, name='temporary_sucess_url'),
    path('temporary-failure-url/', views.temporary_failure_url, name='temporary_failure_url'),
    # path('log-offense/<int:id>/', OffenseCreateView.as_view(), name="log_offense"),
    # path('delete-offense/<int:pk>/', OffenseDeleteView.as_view(), name="delete_offense"),
    # path('update-offense/<int:pk>/', OffenseUpdateView.as_view(), name="update_offense"),
    # path('update-detail/<int:pk>/', OffenseDetailView.as_view(), name="offense_detail"),
    # path('offense-summary', OffenseSummaryView.as_view(), name="offense_summary"),
    # path('log-offense/<int:id>/', OffenseCreateView.as_view(), name="log_offense")

]