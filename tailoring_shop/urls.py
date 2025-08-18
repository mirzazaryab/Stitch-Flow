from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('customers/', include('customers.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('workflow/', include('workflow.urls')),
    path("accounting/", include("accounting.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

