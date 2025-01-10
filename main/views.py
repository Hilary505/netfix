from django.shortcuts import render
from django.contrib.auth import logout as django_logout
from django.db.models import Count, F
from services.models import Service
from services.models import ServiceRequest


def home(request):
    # Get the top 5 most requested services along with their total prices
    most_requested_services = (
        Service.objects.annotate(
            request_count=Count('servicerequest'),
            total_price=F('servicerequest__total_price')  # Calculate total price from ServiceRequest
        )
        .order_by('-request_count')[:2]
    )
    return render(request, 'main/home.html', {'most_requested_services': most_requested_services})


def logout(request):
    django_logout(request)
    return render(request, "main/logout.html")
