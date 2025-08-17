from django import forms
from django.forms import inlineformset_factory
from .models import Order, Product, OrderItem
from customers.models import Customer


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'rate_per_inch', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Product name'}),
            'rate_per_inch': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Rate per inch'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Product description'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'advance_payment', 'notes']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'advance_payment': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Advance payment amount'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Order notes'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].queryset = Customer.objects.all()


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'size', 'quantity']  # Removed DELETE field
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'size': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Size in cm'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'placeholder': 'Quantity'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()


# Formset for handling multiple order items
OrderItemFormSet = inlineformset_factory(
    Order, OrderItem,
    form=OrderItemForm,
    extra=1,
    can_delete=True,
    min_num=1,
    validate_min=True
)


class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }