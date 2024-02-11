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
