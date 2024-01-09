from django.urls import path
from . import views
# from .views import CreateEmployeeView




app_name = 'apps.employees'

urlpatterns = [
    path('register-employee', views.register_employee, name="register_employee"),
    path('manage-employee-data/<int:id>', views.manage_employee_data, name="manage_employee_data"),
    path('employee-data/<int:id>', views.employee_data, name="employee_data"),
    path('delete-employee', views.delete_employee, name="delete_employee"),
    path('employee-list', views.employee_list, name="employee_list"),
    
]