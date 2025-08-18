from django.db import models
from customers.models import Customer
from decimal import Decimal


class Product(models.Model):
    name = models.CharField(max_length=100)
    rate_per_inch = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (${self.rate_per_inch}/inch)"

    class Meta:
        ordering = ['name']


class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('cutting', 'Cutting'),
        ('stitching', 'Stitching'),
        ('quality', 'Quality Check'),
        ('kaj_overlock', 'Kaj Overlock'),
        ('pressing', 'Pressing'),
        ('packing', 'Packing'),
        ('ready', 'Ready for Pickup'),
        ('delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    advance_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    remaining_payment = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.order_number} - {self.customer.name}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Generate order number
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                self.order_number = str(int(last_order.order_number) + 1)
            else:
                self.order_number = "1"
        
        # Calculate remaining payment
        self.remaining_payment = self.total_amount - self.advance_payment
        
        super().save(*args, **kwargs)

    def get_payment_status(self):
        if self.advance_payment == 0:
            return "Pending"
        elif self.advance_payment >= self.total_amount:
            return "Paid"
        else:
            return "Partial"

    class Meta:
        ordering = ['-created_at']


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Calculate unit price: size * rate_per_inch
        self.unit_price = self.size * self.product.rate_per_inch
        # Calculate total price: unit_price * quantity
        self.total_price = self.unit_price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} - {self.size}\" x {self.quantity}"

    class Meta:
        ordering = ['id']

