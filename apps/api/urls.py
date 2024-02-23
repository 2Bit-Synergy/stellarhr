from django.urls import path
from . import views

urlpatterns = [
    path('api/employee-list', views.employee_list),
    path('api/employee-details/<int:id>/', views.employee_detail),
    path('api/update_employee_details/<int:id>/', views.update_employee_details)
    
]