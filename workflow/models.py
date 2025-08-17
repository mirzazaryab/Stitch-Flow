from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class OrderPhaseTracking(models.Model):
    PHASE_CHOICES = [
        ('MEASUREMENT', 'Measurement'),
        ('CUTTING', 'Cutting'),
        ('STITCHING', 'Stitching'),
        ('FINISHING', 'Finishing'),
        ('DELIVERY', 'Delivery'),
    ]

    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    phase = models.CharField(max_length=20, choices=PHASE_CHOICES)
    notes = models.TextField(blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.order.order_number} - {self.phase} - {self.employee.name if self.employee else 'Unassigned'}"