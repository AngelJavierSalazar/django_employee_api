
from django.urls import path
from api import views
  
urlpatterns = [
    path('', views.ApiOverview, name='home'),
     path('create/', views.add_employee, name='add-employee'),
     path('all/', views.view_employees, name='view_employees'),
]