from django.contrib import admin
from .models import Department, Company, Position, Employee, EmploymentHistory, ContactInformation

# Register your models here.


admin.site.register(Department)
admin.site.register(Company)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(EmploymentHistory)
admin.site.register(ContactInformation)
