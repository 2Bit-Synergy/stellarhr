from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer, UserSerializer, EmploymentHistorySerializer, ContactInformationSerializer
from apps.employees.models import Employee, EmploymentHistory, ContactInformation
from apps.accounts.models import User
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    data = serializer.data
    
    return Response(data)

@api_view(['GET'])
def employee_detail(request, id):
    try:
        user = User.objects.select_related('employee').get(id=id) # Use select_related to fetch related employee in one query
        employee_id = user.employee.id
        employment_history = EmploymentHistory.objects.get(employee_id=employee_id) 
        contact_information = ContactInformation.objects.get(employee_id=employee_id)
        
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    user_serializer = UserSerializer(user)
    employment_history_serializer = EmploymentHistorySerializer(employment_history)
    contact_information_serializer = ContactInformationSerializer(contact_information)
    response_data = {
        "user": user_serializer.data,
        "employment_history": employment_history_serializer.data,
        "contact_information": contact_information_serializer.data
    }
    
    return Response(response_data)



def update_employee_details(request, id):
    pass



def delete_employee(request, id):
    pass