from django import forms
from .models import Employee, OrderPhaseTracking

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'phone_number', 'specialization']
        labels = {
            'name': 'Employee Name',
            'phone_number': 'Phone Number',
            'specialization': 'Specialization',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phone_number'].required = False
        self.fields['specialization'].required = False

class OrderPhaseTrackingForm(forms.Form):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.filter(is_active=True),
        label='Employee',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    phase = forms.ChoiceField(
        choices=OrderPhaseTracking.PHASE_CHOICES,
        label='Phase',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True
    )
    notes = forms.CharField(
        label='Notes',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        required=False
    )
    is_completed = forms.BooleanField(
        label='Mark as Completed',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        required=False
    )