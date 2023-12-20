from django.urls import path
from . import views
# from .views import CreateEmployeeView




app_name = 'apps.employees'

urlpatterns = [
    path('create-employee', views.create_employee, name="create_employee"),
    path('update-employee', views.update_employee, name="update_employee"),
    path('delete-employee', views.delete_employee, name="delete_employee"),
    path('employee-list', views.employee_list, name="employee_list"),

]