from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import *


def registerPage(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account wasd created for ' + user)
            return redirect('login')

    context = {
        'form' : form,
    }

    return render(request, 'accounts/register.html', context)

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@allowed_users(allowed_roles=['admin'])
def home(request):
    if request.user.is_authenticated:

        orders = Order.objects.all()
        customers = Customer.objects.all()
        total_customers = customers.count()
        total_orders = orders.count()
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()

        context = {
            'orders' : orders,
            'customers' : customers,
            'total_customers' : total_customers,
            'total_orders' : total_orders,
            'delivered' : delivered,
            'pending' : pending,
            
        }

        return render(request, 'accounts/dashboard.html', context)
    
    else:

        return redirect('login')

def products(request):
    if request.user.is_authenticated:

        products = Product.objects.all()

        return render(request, 'accounts/products.html', {'products':products})
    else:
        return redirect('login')
    
def customer(request, id):

    if request.user.is_authenticated:

        customer = Customer.objects.get(id=id)
        orders = customer.order_set.all()
        orders_count = orders.count()
        
        myFilter = OrderFilter(request.GET, queryset=orders)
        orders = myFilter.qs

        context = {
            'customer' : customer,
            'orders' : orders,
            'orders_count' : orders_count,
            'myFilter' : myFilter,
        }

        return render(request, 'accounts/customer.html', context)
    else:
        return redirect('login')
    
def createOrder(request):
    #call the form from form.py
    form = OrderForm()

    if request.method == 'POST':
        #add the request Data to the form
        form = OrderForm(request.POST)
        #check that the form is valid useing Django's built in validation
        if form.is_valid():
            #save the form to the database
            form.save()
            #send the user back to the home page
            return redirect('home')
        
    context = {
        'form' : form
    }

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, id):
    #retrive the order from the database by the id
    order = Order.objects.get(id=id)
    #call the form from forms.py and autofill it with the order we called from the database
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form' : form
    }
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, id):

    order = Order.objects.get(id=id)

    if request.method == 'POST':
        order.delete()
        return redirect('home')


    context = {
        'order' : order
    }

    return render(request, 'accounts/delete.html', context)