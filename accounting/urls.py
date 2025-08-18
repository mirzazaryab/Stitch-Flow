from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),

    # Sales
    path("sales/add/", views.sale_create, name="sale_create"),
    path("sales/<int:pk>/edit/", views.sale_update, name="sale_update"),
    path("sales/<int:pk>/delete/", views.sale_delete, name="sale_delete"),

    # Expenses
    path("expenses/add/", views.expense_create, name="expense_create"),
    path("expenses/<int:pk>/edit/", views.expense_update, name="expense_update"),
    path("expenses/<int:pk>/delete/", views.expense_delete, name="expense_delete"),

    # Sale Categories
    path("sales/categories/", views.sale_category_list, name="sale_category_list"),
    path("sales/categories/add/", views.sale_category_create, name="sale_category_create"),
    path("sales/categories/<int:pk>/edit/", views.sale_category_update, name="sale_category_update"),
    path("sales/categories/<int:pk>/delete/", views.sale_category_delete, name="sale_category_delete"),

    # Expense Categories
    path("expenses/categories/", views.expense_category_list, name="expense_category_list"),
    path("expenses/categories/add/", views.expense_category_create, name="expense_category_create"),
    path("expenses/categories/<int:pk>/edit/", views.expense_category_update, name="expense_category_update"),
    path("expenses/categories/<int:pk>/delete/", views.expense_category_delete, name="expense_category_delete"),
]
