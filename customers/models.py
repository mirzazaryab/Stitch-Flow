from django.db import models
import json


class Customer(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    company = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

class Measurement(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='measurements')

    # Shirt Measurements
    shirt_length = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    arm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    shoulder = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    neck = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    chest = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gheera = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    moda = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    collar = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    front_pocket = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    side_pocket = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gool = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    choras = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    # Shalwar / Trouser Measurements
    trouser_length = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    trouser_waist = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    trouser_hip = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    thigh = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    knee = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    paincha = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Measurement for {self.customer.name}"

    class Meta:
        ordering = ['-created_at']


