from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib.auth import authenticate, login, logout

from .models import Customer


# User login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'error_message': 'Unable to login! Please check username and password then try again.',
            }
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


# User logout
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


# List all customers
@login_required(login_url='login/')
def index(request):
    customers = Customer.objects.all()
    context = {
        'title': 'Customer List',
        'customers': customers,
    }
    return render(request, 'index.html', context)


# Show specific customer details
@login_required(login_url='login/')
def customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    # invoices = Invoice.objects.filter(customer = customer)
    context = {
        'title': "Customer info - %s" % customer.name,
        'customer': customer,
        # 'invoices' : invoices,
    }
    return render(request, 'customer.html', context)


# Add new customer
@login_required(login_url='login/')
def new_customer(request):
    if request.method == 'POST':
        # Stuff from form
        c = Customer(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'],
                     address=request.POST['address'], invoices=request.POST['invoices'],
                     total_collectibles=request.POST['total_collectibles'], notes=request.POST['notes'])
        c.save()

        if 'saveandnew' in request.POST:
            return HttpResponseRedirect(reverse('new_customer'))
        else:
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'new_customer.html')


# Update customer
@login_required(login_url='login/')
def update_customer(request, customer_id):
    # Stuff from form
    c = get_object_or_404(Customer, pk=customer_id)

    c.name = request.POST['name']
    c.email = request.POST['email']
    c.phone = request.POST['phone']
    c.address = request.POST['address']
    c.invoices = request.POST['invoices']
    c.total_collectibles = request.POST['total_collectibles']
    c.notes = request.POST['notes']

    c.save()

    return HttpResponseRedirect(reverse('index'))


# Delete customer
@login_required(login_url='login/')
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return HttpResponseRedirect(reverse('index'))


# Search for invoice
@login_required(login_url='login/')
def search_customer(request):
    name = request.POST['name']
    return HttpResponseRedirect(reverse('customer', args=(name,)))
