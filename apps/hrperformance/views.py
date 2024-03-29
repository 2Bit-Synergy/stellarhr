from django.shortcuts import render
from apps.accounts.models import User
from apps.hrperformance.models import AttendanceRecord, HRSetting
from apps.hrperformance.forms import AttendanceRecordForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import SingleObjectMixin, DetailView
from django.views.generic.detail import SingleObjectMixin, DetailView
from .forms import AttendanceRecordForm, HRSettingForm, OffenseForm, RecognitionForm
from .models import AttendanceRecord, Offense, Recognition
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from apps.employees.models import Employee
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.models import Group


#ATTENDACE RECORD VIEWS
class AttendanceRecordView(LoginRequiredMixin, CreateView):
    form_class = AttendanceRecordForm
    model = AttendanceRecord
    template_name = 'hrperformance/my-dashboard.html'
    success_url = reverse_lazy('my_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        employee_instance = get_object_or_404(Employee, user_id=current_user)
        post_date = timezone.now().date()

        # Check if the user has logged in
        attendance_record_checker = AttendanceRecord.objects.filter(
            employee=employee_instance,
            timein__date=post_date
        ).first()

        # Check if the user has logged out
        is_done_for_day = False
        if attendance_record_checker and attendance_record_checker.timeout:
            is_done_for_day = True

        # Set context variables
        context['is_time_in'] = attendance_record_checker is None or attendance_record_checker.timeout is not None
        context['is_done_for_day'] = is_done_for_day

        return context

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
                return redirect('my_dashboard')
            else:
                return redirect('my_dashboard')
        else:
            employee_attendance.employee = employee_instance
            employee_attendance.timein = post_datetime_stamp
            employee_attendance.save()
            return redirect('my_dashboard')
        

class AttendanceSummaryView(ListView):
    model  = AttendanceRecord
    template_name = 'hrperformance/attendance-summary.html'
    
    def get_queryset(self):
        # Get the current user's groups
        user_groups = self.request.user.groups.all()
        
        # Check if the user belongs to the HR group
        if any(group.name == 'HR' for group in user_groups):
            # If yes, return all attendance records
            attendance_records = AttendanceRecord.objects.all()
            return attendance_records
        else:
            # If not, return only the attendance records of the requesting user
            attendance_records = AttendanceRecord.objects.filter(employee=self.request.user.employee)
            return attendance_records
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attendance_records'] = self.get_queryset()
        return context
        


class AttendanceRecordDetailView(DetailView):
    model = AttendanceRecord
    template_name = 'hrperformance/attendance-detail.html'
    

class AttendanceRecordEditView(UpdateView):
    model = AttendanceRecord
    template_name = 'hrperformance/edit-attendance-record.html'
    fields = '__all__'
    success_url = reverse_lazy('attendance_summary')
    
    
class AttendanceRecordDeleteView(DeleteView):
    model = AttendanceRecord
    template_name = 'hrperformance/delete-attendance-record.html'
    success_url = reverse_lazy('attendance_summary')


    
#HR SETTINGS VIEWS  
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
    
    
    
    
#OFFENSE VIEWS
class OffenseCreateView(CreateView):
        model = Offense
        template_name = 'hrperformance/log-offense.html'
        form_class = OffenseForm
        success_url = reverse_lazy('temporary_sucess_url')
        

        
        def get_initial(self):
            initial = super().get_initial()
            # Get the user object based on the ID passed in the URL
            user_id = self.kwargs.get('id')
            user = get_object_or_404(User, id=user_id)
            employee = user.employee
            # Set the 'employee' field in the initial data
            initial['employee'] = employee
            return initial
        
        def post(self, request, *args, **kwargs):
            form = self.get_form()
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
            
    
    

class OffenseSummaryView(ListView):
    model = Offense
    template_name = 'hrperformance/offense-summary.html'
    # form_class = OffenseForm



class OffenseDeleteView(DeleteView):
    model = Offense
    template_name = 'hrperformance/delete-offense.html'
    success_url = reverse_lazy('temporary_sucess_url')

    def delete(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.delete()
            messages.success(request, 'Offense deleted successfully.')
            return HttpResponseRedirect(success_url)
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
            return HttpResponseRedirect(reverse('temporary_failure_url'))  # Redirect to a failure URL

    
    
class OffenseUpdateView(UpdateView, SingleObjectMixin):
    model = Offense
    template_name = 'hrperformance/update-offense.html'
    form_class = OffenseForm
    success_url = reverse_lazy('temporary_sucess_url')



class OffenseDetailView(DetailView):
    model = Offense
    template_name = 'hrperformance/offense-detail.html'
    form_class = OffenseForm
    success_url = reverse_lazy('temporary_sucess_url')
    











#RECOGNITION VIEWS
class RecognitionCreateView(CreateView):
    model = Recognition
    form_class = RecognitionForm
    template_name = 'hrperformance/add-recognition.html'
    success_url = reverse_lazy('recognition_summary')

    
class RecognitionUdpateView(UpdateView):
    model = Recognition
    form_class = RecognitionForm
    template_name = 'hrperformance/update-recognition.html'
    success_url = reverse_lazy('recognition_summary')


class RecognitionDetailView(DetailView):
    model = Recognition
    template_name = 'hrperformance/recognition-detail.html'

class RecognitionSummaryView(ListView):
    model = Recognition
    template_name = 'hrperformance/recognition-summary.html'
    

class RecognitionDeleteView(DeleteView):
    model = Recognition
    template_name = 'hrperformance/delete-recognition.html'
    success_url = reverse_lazy('recognition_summary')








#TEMPORARY HANDLERS
def temporary_success_url(request):
    return HttpResponse("UPDATE SUCCESSFULL")


def temporary_failure_url(request):
    return HttpResponse("UNSUCCESSFULL")
