import email
import datetime

from django.db import models
from django.db.models import Model
 
 
# Create your models here.
 
class Employee(models.Model):
   # id = models.IntegerField("id", primary_key=True)
   first_name = models.CharField(max_length=30, blank=True)
   last_name = models.CharField(max_length=30, blank=True)
   email = models.EmailField(max_length=255, blank=True, null=True)
   gender = models.CharField(("gender"), max_length=30, blank=True, null=True) 
   date_of_birth = models.DateField(default=datetime.datetime.now)
   industry = models.CharField(max_length=20, blank=True, null=True)
   salary = models.FloatField(("salary"), blank=True, default=0.0, null=True)
   years_of_experience = models.IntegerField(("years_of_experience"), blank=True, null=True)
    
   
 
  
   def __str__(self):
       return self.first_name + " " + self.last_name
