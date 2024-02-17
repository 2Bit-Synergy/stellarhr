from django.urls import path
from . import views
# from .views import CreateEmployeeView




app_name = 'apps.employees'

urlpatterns = [
    path('register-employee', views.register_employee, name="register_employee"),
    path('manage-employee-data', views.manage_employee_data, name="manage_employee_data"),
    path('employee-data/<int:id>', views.employee_data, name="employee_data"),
    path('employee-data-update/<int:id>/', views.EmployeeData.as_view(), name="employee_data_update"),
    path('delete-employee/', views.DeleteEmployee.as_view(), name="delete_employee"),
    path('employee-list', views.employee_list, name="employee_list"),
    
]