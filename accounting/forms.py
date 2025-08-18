from django import forms
from .models import Sale, Expense, SaleCategory, ExpenseCategory


class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["category", "amount", "description"]
        widgets = {
            "category": forms.Select(attrs={
                "class": "form-select rounded-3 shadow-sm",
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "placeholder": "Enter amount",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "rows": 4,
                "placeholder": "Enter description",
            }),
        }


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ["category", "amount", "description"]
        widgets = {
            "category": forms.Select(attrs={
                "class": "form-select rounded-3 shadow-sm",
            }),
            "amount": forms.NumberInput(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "placeholder": "Enter amount",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "rows": 4,
                "placeholder": "Enter description",
            }),
        }


class SaleCategoryForm(forms.ModelForm):
    class Meta:
        model = SaleCategory
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "placeholder": "Enter sale category name",
            }),
        }


class ExpenseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExpenseCategory
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "placeholder": "Enter expense category name",
            }),
        }
