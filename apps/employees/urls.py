from django.urls import path
from . import views

app_name = 'apps.employees'

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('<int:pk>/', views.employee_detail, name='employee_detail'),
    path('create/', views.employee_create, name='employee_create'),
    path('<int:pk>/update/', views.employee_update, name='employee_update'),
    # Add more paths as needed
]