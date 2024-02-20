from django.urls import path
from . import views

urlpatterns = [
    path('api/employee-list', views.employee_list),
    path('api/employee-details/<int:id>/', views.employee_detail),
]