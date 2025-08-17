from django import forms
from .models import Customer, Measurement


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'company']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter company name (optional)'}),
        }


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = [
            'shirt_length', 'arm', 'shoulder', 'neck', 'chest', 'waist',
            'gheera', 'moda', 'collar', 'front_pocket', 'side_pocket',
            'gool', 'choras',
            'trouser_length', 'trouser_waist', 'trouser_hip',
            'thigh', 'knee', 'paincha',
            'notes'
        ]
        widgets = {
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
