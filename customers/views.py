from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Customer, Measurement
from .forms import CustomerForm, MeasurementForm


def customer_list(request):
    search_query = request.GET.get('search', '')
    customers = Customer.objects.all()
    
    if search_query:
        customers = customers.filter(
            Q(name__icontains=search_query) |
            Q(phone_number__icontains=search_query) |
            Q(company__icontains=search_query)
        )
    
    context = {
        'customers': customers,
        'search_query': search_query,
    }
    return render(request, 'customers/customer_list.html', context)


def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            messages.success(request, f'Customer "{customer.name}" created successfully!')
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm()
    
    return render(request, 'customers/create.html', {'form': form})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    measurements = customer.measurements.all()
    orders = customer.orders.all()
    
    context = {
        'customer': customer,
        'measurements': measurements,
        'orders': orders,
    }
    return render(request, 'customers/detail.html', context)


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, f'Customer "{customer.name}" updated successfully!')
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    
    return render(request, 'customers/edit.html', {'form': form, 'customer': customer})


def measurement_create(request, customer_pk):
    customer = get_object_or_404(Customer, pk=customer_pk)
    
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.customer = customer
            measurement.save()
            messages.success(request, 'Measurements saved successfully!')
            return redirect('measurement_detail', pk=measurement.pk)
    else:
        form = MeasurementForm()
    
    return render(request, 'customers/measurement_create.html', {
        'form': form,
        'customer': customer
    })


def measurement_detail(request, pk):
    measurement = get_object_or_404(Measurement, pk=pk)
    return render(request, 'customers/measurement_detail.html', {'measurement': measurement})

