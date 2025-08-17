from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_list, name='payment_list'),
    path('create/<int:order_pk>/', views.payment_create, name='payment_create'),
]

