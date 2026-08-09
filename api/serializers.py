from rest_framework import serializers

from api.models import Student
from employee.models import employee


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= employee
        fields = "__all__"
        