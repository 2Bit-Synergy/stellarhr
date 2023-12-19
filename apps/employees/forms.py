from django import forms
from .models import Employee, ContactInformation

class EmployeeAndContactForm(forms.ModelForm):
    address = forms.CharField(max_length=255, label='Address')
    phone_number = forms.CharField(max_length=255, label='phone_number')
    emergency_contact_name = forms.CharField(max_length=255, label='emergency_contact_name')
    emergency_contact_number = forms.CharField(max_length=255, label='emergency_contact_number')

    def __init__(self, *args, **kwargs):
        super(EmployeeAndContactForm, self).__init__(*args, **kwargs)

        # Include ContactInformation fields in the form
        if 'instance' in kwargs and kwargs['instance']:
            employee_instance = kwargs['instance']

            contact_info = ContactInformation.objects.get(employee=employee_instance)
            self.fields['address'].initial = contact_info.address
            self.fields['phone_number'].initial = contact_info.phone_number
            self.fields['emergency_contact_name'].initial = contact_info.emergency_contact_name
            self.fields['emergency_contact_number'].initial = contact_info.emergency_contact_number
    
    def save(self, commit=True):
        print("SAVE")
        employee = super(EmployeeAndContactForm, self).save(commit)
        print(employee)
        # Save or update ContactInformation
        contact_info, created = ContactInformation.objects.get_or_create(employee=employee)
        print("xxx")
        contact_info.address = self.cleaned_data['address']
        contact_info.phone_number = self.cleaned_data['phone_number']
        contact_info.emergency_contact_name = self.cleaned_data['emergency_contact_name']
        contact_info.emergency_contact_number = self.cleaned_data['emergency_contact_number']
        contact_info.save()

        print(employee)
        return employee
    
    class Meta:
        model = Employee
        fields = '__all__'
        # Add more fields from ContactInformation model as needed
        exclude = ('user',)  # Exclude the 'user' field from the form