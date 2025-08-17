from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db import transaction
from decimal import Decimal
from .models import Payment
from orders.models import Order


def payment_list(request):
    payments = Payment.objects.select_related('order', 'order__customer').all()
    return render(request, 'payments/payment_list.html', {'payments': payments})


def payment_create(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)

    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        payment_type = request.POST.get('payment_type')
        notes = request.POST.get('notes')

        try:
            amount = Decimal(amount.replace(',', ''))  # Convert string to Decimal
        except (ValueError, TypeError):
            messages.error(request, 'Invalid amount format. Please enter a valid number.')
            return render(request, 'payments/create.html', {
                'order': order,
                'payment_methods': Payment.PAYMENT_METHOD_CHOICES,
                'payment_types': Payment.PAYMENT_TYPE_CHOICES,
                'form_data': request.POST,  # Preserve form data on error
            })

        with transaction.atomic():
            payment = Payment.objects.create(
                order=order,
                amount=amount,
                payment_method=payment_method,
                payment_type=payment_type,
                notes=notes
            )

            # Update order advance payment
            if payment_type == 'advance':
                order.advance_payment += payment.amount

            order.save()

            messages.success(request, f'Payment of Rs {payment.amount:.2f} recorded successfully!')
            return redirect('order_detail', pk=order.pk)

    context = {
        'order': order,
        'payment_methods': Payment.PAYMENT_METHOD_CHOICES,
        'payment_types': Payment.PAYMENT_TYPE_CHOICES,
    }
    return render(request, 'payments/create.html', context)