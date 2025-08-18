from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Sum
from django.db import transaction
from decimal import Decimal
from .models import Order, Product, OrderItem
from .forms import OrderForm, OrderItemFormSet, ProductForm, OrderStatusForm


def order_list(request):
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    orders = Order.objects.select_related('customer').all()

    if search_query:
        orders = orders.filter(
            Q(order_number__icontains=search_query) |
            Q(customer__name__icontains=search_query) |
            Q(customer__phone_number__icontains=search_query)
        )

    if status_filter:
        orders = orders.filter(status=status_filter)

    context = {
        'orders': orders,
        'search_query': search_query,
        'status_filter': status_filter,
        'status_choices': Order.STATUS_CHOICES,
    }
    return render(request, 'orders/order_list.html', context)


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST, instance=Order())

        if form.is_valid() and formset.is_valid():
            with transaction.atomic():
                order = form.save()
                formset.instance = order
                order_items = formset.save()  # Handles saving and deleting

                # Calculate total amount
                total = Decimal('0.00')
                for item in order_items:
                    total += item.total_price

                order.total_amount = total
                order.save()

                messages.success(request, f'Order #{order.order_number} created successfully!')
                return redirect('order_detail', pk=order.pk)
    else:
        form = OrderForm()
        formset = OrderItemFormSet(instance=Order())

    return render(request, 'orders/create.html', {
        'form': form,
        'formset': formset
    })


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    items = order.items.all()
    # Remove phase_tracking; keep payments if valid, otherwise remove
    try:
        payments = order.payments.all()
    except AttributeError:
        payments = []

    context = {
        'order': order,
        'items': items,
        'payments': payments,
    }
    return render(request, 'orders/detail.html', context)


def order_update_status(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        form = OrderStatusForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, f'Order #{order.order_number} status updated to {order.get_status_display()}!')
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderStatusForm(instance=order)

    return render(request, 'orders/update_status.html', {
        'form': form,
        'order': order
    })


def product_list(request):
    products = Product.objects.all()
    return render(request, 'orders/product_list.html', {'products': products})


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(request, f'Product "{product.name}" created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'orders/product_create.html', {'form': form})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        messages.success(request, f"Order #{order.order_number} deleted successfully.")
        return redirect('order_list')
    return redirect('order_list')
