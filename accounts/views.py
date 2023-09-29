from django.shortcuts import render, redirect
from .models import *
from .forms import OrderForm

def home(request):
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

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html', {'products':products})

def customer(request, id):
    customer = Customer.objects.get(id=id)
    orders = customer.order_set.all()
    orders_count = orders.count()
   
    context = {
        'customer' : customer,
        'orders' : orders,
        'orders_count' : orders_count,
    }

    return render(request, 'accounts/customer.html', context)

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