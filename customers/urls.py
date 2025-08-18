from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
    path('<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('<int:customer_pk>/measurements/create/', views.measurement_create, name='measurement_create'),
    path('measurements/<int:pk>/', views.measurement_detail, name='measurement_detail'),
]

