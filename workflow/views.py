from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count, Q
from .models import Employee, OrderPhaseTracking
from .forms import EmployeeForm, OrderPhaseTrackingForm
from orders.models import Order


def workflow_dashboard(request):
    # Get order statistics by status
    order_stats = Order.objects.values('status').annotate(count=Count('id'))

    # Get recent phase tracking
    recent_tracking = OrderPhaseTracking.objects.select_related(
        'order', 'order__customer', 'employee'
    ).order_by('-start_time')[:10]

    # Get active employees
    employees = Employee.objects.filter(is_active=True)

    context = {
        'order_stats': order_stats,
        'recent_tracking': recent_tracking,
        'employees': employees,
    }
    return render(request, 'workflow/dashboard.html', context)


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'workflow/employee_list.html', {'employees': employees})


def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f'Employee "{employee.name}" created successfully!')
            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'workflow/employee_create.html', {'form': form})


def assign_employee(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)

    if request.method == 'POST':
        form = OrderPhaseTrackingForm(request.POST)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            phase = form.cleaned_data['phase']
            notes = form.cleaned_data['notes']
            is_completed = form.cleaned_data['is_completed']

            tracking, created = OrderPhaseTracking.objects.get_or_create(
                order=order,
                phase=phase,
                defaults={
                    'employee': employee,
                    'notes': notes,
                    'is_completed': is_completed
                }
            )

            if not created:
                tracking.employee = employee
                tracking.notes = notes
                tracking.is_completed = is_completed
                tracking.save()

            messages.success(request, f'Employee "{employee.name}" assigned to {phase} phase!')
            return redirect('order_detail', pk=order.pk)
    else:
        form = OrderPhaseTrackingForm()

    context = {
        'order': order,
        'form': form,
    }
    return render(request, 'workflow/assign_employee.html', context)