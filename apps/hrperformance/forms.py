from django import forms
from apps.hrperformance.models import AttendanceRecord, TimeLogType, HRSetting




class AttendanceRecordForm(forms.ModelForm):
    
    class Meta:
        model = AttendanceRecord
        fields = ['employee', 'timein', 'timeout']
        widgets = {
            'timein': forms.DateTimeInput(attrs={'required': False}),
            'timeout': forms.DateTimeInput(attrs={'required': False}),
        }
        
        
class HRSettingForm(forms.ModelForm):
    class Meta:
        model = HRSetting
        fields = '__all__'