from rest_framework import serializers
from apps.employees.models import Employee, ContactInformation, EmploymentHistory, Company, Position, Department
from apps.accounts.models import User



class ContactInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInformation
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
        
class EmploymentHistorySerializer(serializers.ModelSerializer):
    company = CompanySerializer()
        
    class Meta:
        model = EmploymentHistory
        fields = '__all__'





class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

        

class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = '__all__'
        

class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()
    
    class Meta:
        model = User
        fields = '__all__'
        
        




