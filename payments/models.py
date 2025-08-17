from django.db import models
from orders.models import Order


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank_transfer', 'Bank Transfer'),
        ('check', 'Check'),
    ]

    PAYMENT_TYPE_CHOICES = [
        ('advance', 'Advance Payment'),
        ('final', 'Final Payment'),
        ('partial', 'Partial Payment'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES, default='advance')
    payment_date = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment of ${self.amount} for Order #{self.order.order_number}"

    class Meta:
        ordering = ['-payment_date']

