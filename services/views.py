from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from users.models import Company, Customer, User

from .models import Service
from .forms import CreateNewService, RequestServiceForm


def service_list(request):
    services = Service.objects.all().order_by("-date")
    return render(request, 'services/list.html', {'services': services})


def index(request, id):
    service = Service.objects.get(id=id)
    return render(request, 'services/single_service.html', {'service': service})


def create(request):
    return render(request, 'services/create.html', {})


def service_field(request, field):
    # search for the service present in the url
    field = field.replace('-', ' ').title()
    services = Service.objects.filter(
        field=field)
    return render(request, 'services/field.html', {'services': services, 'field': field})


def request_service(request, id):
    service = get_object_or_404(Service, id=id)
    customer = get_object_or_404(Customer, user=request.user)  # Get the logged-in customer
    
    if request.method == 'POST':
        form = RequestServiceForm(request.POST)
        if form.is_valid():
            service_hours = form.cleaned_data['service_hours']
            address = form.cleaned_data['address']
            total_price = service.price_hour * service_hours  # Calculate total price

            # Save the service request
            ServiceRequest.objects.create(
                customer=customer,
                service=service,
                service_hours=service_hours,
                address=address,
                total_price=total_price
            )
            return redirect('customer_profile', username=request.user.username)  # Redirect after success
    else:
        form = RequestServiceForm()

    return render(request, 'services/request_service.html', {'form': form, 'service': service})
