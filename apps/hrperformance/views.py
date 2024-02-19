from django.shortcuts import render
from apps.hrperformance.models import AttendanceRecord, HRSetting
from apps.hrperformance.forms import AttendanceRecordForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AttendanceRecordForm, HRSettingForm
from .models import AttendanceRecord 
from django.shortcuts import get_object_or_404
from django.utils import timezone
from apps.employees.models import Employee
from django.http import JsonResponse
from django.utils import timezone

class AttendanceRecordView(LoginRequiredMixin, CreateView):
    form_class = AttendanceRecordForm
    model = AttendanceRecord
    template_name = 'hrperformance/my-dashboard.html'
    success_url = reverse_lazy('my_dashboard')
    
    def post(self, request, *args, **kwargs):
        current_user = self.request.user
        employee_instance = get_object_or_404(Employee, user_id=current_user)
        post_datetime_stamp = timezone.now()
        post_date = timezone.now().date()
        employee_attendance = AttendanceRecord()

        
        attendance_record_checker = AttendanceRecord.objects.filter(
            employee=employee_instance,
            timein__date=post_date
        ).first()
        
        if attendance_record_checker:
            if attendance_record_checker.timeout is None:
                attendance_record_checker.timeout = post_datetime_stamp
                attendance_record_checker.save()
                return HttpResponse("DONE LOGOUT")
            else:
                return HttpResponse("NKA LOGIN and LOGOUT NAKA")
            
        else:
            employee_attendance.employee = employee_instance
            employee_attendance.timein = post_datetime_stamp
            employee_attendance.save()
            return HttpResponse("DONE LOGIN")  

        
        
        ### LOGIC IS NOW CORRECT, NEXT MOVE IS TO INCLUDE TYPE IN THE CONDITION AND IMPLEMENT PROPER REDIRECT, 
        

class HRSettingView(FormView):
    model = HRSetting
    template_name = "hrperformance/hr-settings.html"
    form_class = HRSettingForm
    
