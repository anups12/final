from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages
from .forms import Orderform, UserRegister, UpdateCustomer
from .filters import OrderFilter
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def SigninUser(request):
    form=UserRegister()
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulations your account has been created ')
            return redirect('login')
    context={'form':form}
    return render(request, 'learn/signin.html', context)
    
def LoginUser(request): 
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully '+ username)
            return redirect('profile')
    return render(request, 'learn/login.html')

def LogoutUser(request):
    logout(request)
    return redirect('/login/')

def UserProfile(request):
    orders = request.user.customer.order_set.all()
    total_order=orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='pending').count()
    context={'orders':orders, 'total_order':total_order, 'delivered':delivered,'pending':pending}
    return render(request, 'learn/profile.html', context)

def Update_profile(request):
    cust = request.user.customer
    form = UpdateCustomer(instance=cust)
    if request.method=='POST':
        form = UpdateCustomer(request.POST, request.FILES, instance=cust)
        if form.is_valid():
            form.save()
            return redirect('/')            
    return render(request, 'learn/update_cust.html',{'form':form})

@login_required(login_url='login')
def Home(request):
    order = Order.objects.all() 
    customer =Customer.objects.all()
    total_customer=customer.count()
    total_order=order.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='pending').count()
    context = {'customer':customer, 'order':order, 'total_customer':total_customer,'total_order':total_order, 'delivered':delivered,'pending':pending}
  
    return render(request, 'learn/dashboard.html', context)

@login_required(login_url='login')
def Products(request):
    product = Product.objects.all()
    context = {'product':product}
    return render(request, 'learn/products.html', context)

@login_required(login_url='login')
def Customerpage(request, pk):
    customer = Customer.objects.get(id=pk)
    myfilter = OrderFilter()
    context = {'customer':customer, 'myfilter':myfilter}
    return render(request, 'learn/customer.html', context)

@login_required(login_url='login')
def Create_Order(request, pk):
    customer = Customer.objects.get(id=pk)
    form = Orderform(initial={'customer':customer})
    if request.method=='POST':
        form = Orderform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        form = Orderform()
    context={'form':form}
    return render(request, 'learn/create_order.html', context)

@login_required(login_url='login')
def Update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = Orderform(instance=order)
    if request.method=='POST':
        form = Orderform(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'learn/create_order.html', context)

@login_required(login_url='login')
def Delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context = {'order':order}
    return render(request, 'learn/delete.html', context)