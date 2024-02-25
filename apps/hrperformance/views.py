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
from .forms import AttendanceRecordForm, HRSettingForm, OffenseForm, RecognitionForm
from .models import AttendanceRecord, Offense
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
        

class HRSettingUpdateView(UpdateView):
    model = HRSetting
    form_class = HRSettingForm
    template_name = 'hrperformance/hr-settings.html'  # Your template name
    success_url = '/success-url/'  # URL to redirect after successful form submission
    
    
    
    
class HRSettingUpdateView(UpdateView):
    model = HRSetting
    form_class = HRSettingForm
    template_name = 'hrperformance/hr-settings.html'
    success_url = reverse_lazy('temporary_sucess_url')

    def get_object(self, queryset=None):
        return HRSetting.objects.get(pk=1)

    def get_initial(self):
        initial = super().get_initial()
        instance = self.get_object()
        initial['timein_setpoint'] = instance.timein_setpoint  # Prepopulate with instance data
        initial['timeout_setpoint'] = instance.timeout_setpoint
        initial['break_time_start'] = instance.break_time_start
        initial['break_time_end'] = instance.break_time_end
        initial['awol_setpoint'] = instance.awol_setpoint
        initial['late_offense_verbalwarning'] = instance.late_offense_verbalwarning
        initial['late_offense_writtenwarning'] = instance.late_offense_writtenwarning
        initial['late_offense_suspension'] = instance.late_offense_suspension
        initial['awol_offense_verbalwarning'] = instance.awol_offense_verbalwarning
        initial['awol_offense_writtenwarning'] = instance.awol_offense_writtenwarning
        initial['awol_offense_suspension'] = instance.awol_offense_suspension
        return initial

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.save()
        return super().form_valid(form)
    
    
    
    

class OffenseCreateView(CreateView):
    model = Offense
    template_name = 'hrperformance/log-offense.html'
    form_class = OffenseForm
    success_url = reverse_lazy('offense_create')
    
    def get_object():
        employee_with_offense = User.objects.get(id=id)
        print(employee_with_offense)
        return employee_with_offense
    
    
    
    
    
class OffenseUpdateView(UpdateView):
    model = Offense
    template_name = 'hrperformance/update-offense.html'
    form_class = OffenseForm




def temporary_success_url(request):
    return HttpResponse("UPDATE SUCCESSFULL")