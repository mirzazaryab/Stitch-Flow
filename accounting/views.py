from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now
from .models import Sale, Expense, SaleCategory, ExpenseCategory
from .forms import (
    SaleForm,
    ExpenseForm,
    SaleCategoryForm,
    ExpenseCategoryForm,
)

# ---------------- Dashboard ----------------
def dashboard(request):
    today = now().date()
    sales_today = Sale.objects.filter(date=today)
    expenses_today = Expense.objects.filter(date=today)

    total_sales = sum(s.amount for s in sales_today)
    total_expenses = sum(e.amount for e in expenses_today)
    profit = total_sales - total_expenses

    return render(request, "accounting/dashboard.html", {
        "sales_today": sales_today,
        "expenses_today": expenses_today,
        "total_sales": total_sales,
        "total_expenses": total_expenses,
        "profit": profit,
    })


# ---------------- Sales ----------------
def sale_create(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = SaleForm()
    return render(request, "accounting/form.html", {"form": form, "title": "Add Sale"})


# ---------------- Expenses ----------------
def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ExpenseForm()
    return render(request, "accounting/form.html", {"form": form, "title": "Add Expense"})


# ---------------- Sale Categories ----------------
def sale_category_list(request):
    categories = SaleCategory.objects.all()
    return render(request, "accounting/category_list.html", {
        "categories": categories,
        "title": "Sale Categories",
        "type": "sale",
    })


def sale_category_create(request):
    if request.method == "POST":
        form = SaleCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("sale_category_list")
    else:
        form = SaleCategoryForm()
    return render(request, "accounting/form.html", {"form": form, "title": "Add Sale Category"})


def sale_category_update(request, pk):
    category = get_object_or_404(SaleCategory, pk=pk)
    if request.method == "POST":
        form = SaleCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("sale_category_list")
    else:
        form = SaleCategoryForm(instance=category)
    return render(request, "accounting/form.html", {"form": form, "title": "Edit Sale Category"})


def sale_category_delete(request, pk):
    category = get_object_or_404(SaleCategory, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("sale_category_list")
    return render(request, "accounting/confirm_delete.html", {"object": category, "type": "Sale Category"})


# ---------------- Expense Categories ----------------
def expense_category_list(request):
    categories = ExpenseCategory.objects.all()
    return render(request, "accounting/category_list.html", {
        "categories": categories,
        "title": "Expense Categories",
        "type": "expense",
    })


def expense_category_create(request):
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("expense_category_list")
    else:
        form = ExpenseCategoryForm()
    return render(request, "accounting/form.html", {"form": form, "title": "Add Expense Category"})


def expense_category_update(request, pk):
    category = get_object_or_404(ExpenseCategory, pk=pk)
    if request.method == "POST":
        form = ExpenseCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("expense_category_list")
    else:
        form = ExpenseCategoryForm(instance=category)
    return render(request, "accounting/form.html", {"form": form, "title": "Edit Expense Category"})


def expense_category_delete(request, pk):
    category = get_object_or_404(ExpenseCategory, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("expense_category_list")
    return render(request, "accounting/confirm_delete.html", {"object": category, "type": "Expense Category"})

def sale_create(request):
    if request.method == "POST":
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = SaleForm()
    return render(request, "accounting/form.html", {"form": form, "title": "Add Sale"})


def sale_update(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        form = SaleForm(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = SaleForm(instance=sale)
    return render(request, "accounting/form.html", {"form": form, "title": "Edit Sale"})


def sale_delete(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == "POST":
        sale.delete()
        return redirect("dashboard")
    return render(request, "accounting/confirm_delete.html", {"object": sale, "type": "Sale"})

def expense_create(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ExpenseForm()
    return render(request, "accounting/form.html", {"form": form, "title": "Add Expense"})


def expense_update(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    else:
        form = ExpenseForm(instance=expense)
    return render(request, "accounting/form.html", {"form": form, "title": "Edit Expense"})


def expense_delete(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        expense.delete()
        return redirect("dashboard")
    return render(request, "accounting/confirm_delete.html", {"object": expense, "type": "Expense"})
