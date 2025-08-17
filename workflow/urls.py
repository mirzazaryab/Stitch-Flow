from django.urls import path
from . import views

urlpatterns = [
    path('', views.workflow_dashboard, name='workflow_dashboard'),
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),
    path('assign/<int:order_pk>/', views.assign_employee, name='assign_employee'),
]

