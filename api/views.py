
from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

from .models import Employee 
from .serializers import EmployeeSerializer
  
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_employees': '/',
        'Average age per industry': '/?industry=industry_name',
        'Average salaries per industry': '/?industry=c=industry_name',
        'Average salries per years of experience': '/?industry=s=industry_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/employee/pk/delete'
    }
  
    return Response(api_urls)


  
@api_view(['POST'])
def add_employee(request):
    employee = EmployeeSerializer(data=request.data)
  
    # validating for already existing data
#    if employee.objects.filter(**request.data).exists():
#       raise serializers.ValidationError('This data already exists')
  
    if employee.is_valid():
        employee.save()
        return Response(employee.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


def view_employees(request):
   #get all employees
   #serialize all employees
   #return json response
   employees = Employee.objects.all()
   serializer= EmployeeSerializer(employees, many=True)
   return JsonResponse(serializer.data, safe=False)


