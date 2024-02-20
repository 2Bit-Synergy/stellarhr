from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer, UserSerializer
from apps.employees.models import Employee
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
        user = User.objects.select_related('employee').get(id=id)  # Use select_related to fetch related employee in one query
    except User.DoesNotExist:
        return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

# @api_view(['GET'])
# def employee_detail(request, id):
#     employee = User.objects.get(id=id)
#     serializer = UserSerializer(employee)
    
#     data = serializer.data
    
#     return Response(data)


# class EmployeeDetailView(APIView):
#     def get(self, request, id):
#         try:
#             employee = User.objects.get(id=id)
#         except User.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
        
#         serializer = UserSerializer(employee)
#         return Response(serializer.data)