
from django.db.models import fields
# import serializer from rest_framework
from rest_framework import serializers
# import model from models.py
from .models import Employee
 
# Create a model serializer
class EmployeeSerializer(serializers.ModelSerializer):
   # specify model and fields
   class Meta:
       model = Employee
       fields = ('first_name', 'last_name', 'industry', 'date_of_birth', 'years_of_experience')
       
       
        