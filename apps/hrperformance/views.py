from django.shortcuts import render
from apps.hrperformance.models import AttendanceRecord
from apps.hrperformance.forms import AttendanceRecordForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AttendanceRecordForm  
from .models import AttendanceRecord 
from django.shortcuts import get_object_or_404
from django.utils import timezone
from apps.employees.models import Employee

class AttendanceRecordView(LoginRequiredMixin, CreateView):
    form_class = AttendanceRecordForm
    model = AttendanceRecord
    template_name = 'hrperformance/my-dashboard.html'
    success_url = reverse_lazy('my_dashboard')
    
    

    # def get_success_url(self):
    #     return reverse_lazy('my_dashboard')

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     if self.request.method == 'GET':
    #         employee_instance = get_object_or_404(Employee, user_id=self.request.user)
    #         kwargs['initial']['employee'] = employee_instance
    #     return kwargs

    # def form_valid(self, form):
    #     # Check if an instance already exists for the current day, employee, and type
    #     existing_instance = AttendanceRecord.objects.filter(
    #         employee__user_id=self.request.user,
    #         type=form.cleaned_data['type'],
    #         timein__date=timezone.now().date(),
    #     ).first()

    #     if existing_instance:
    #         # If an instance exists, update the timeout value
    #         existing_instance.timeout = timezone.now()
    #         existing_instance.save()
    #         success_message = "Attendance record successfully updated!"
    #         return super().form_valid(form)  # Return early to avoid creating a new instance
    #     else:
    #         # If no instance exists, create a new instance with the timein value
    #         form.instance.employee = get_object_or_404(Employee, user_id=self.request.user)
    #         form.instance.timein = timezone.now()  # Set the timein only when creating a new instance
    #         form.instance.timeout = timezone.now()  # Set the timeout initially to avoid null constraint issues
    #         success_message = "Attendance record successfully created!"

    #     messages.success(self.request, success_message)
    #     return super().form_valid(form)