from django import forms
from apps.hrperformance.models import AttendanceRecord, TimeLogType




class AttendanceRecordForm(forms.ModelForm):
    
    class Meta:
        model = AttendanceRecord
        fields = '__all__'
