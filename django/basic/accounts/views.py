from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
#authenticaion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *

from .forms import OrderForm, UserCreationForm, CustomerForm
from .filters import OrderFilter
from .decorators import unauthenticated_user, allowed_user, only_admin

# Create your views here.


@unauthenticated_user
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #form.save()
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            #register to create 'user' for 'customer'
            Customer.objects.create(
                user = user,
                name = user.username,
            )
            username = form.cleaned_data.get('username')
            messages.success(request,'Tạo thành công tài khoản: '+ username)

            return redirect('login')

    context = {'form':form}
    return render(request, 'accounts/register.html',context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        #get data from input
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    return render(request, 'accounts/login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_user(allowed_grp=['customer'])
def userPage(request):
    #get user => link OneToOne with 'customer' => customer link oneToMany with 'orders'
    orders = request.user.customer.order_set.all()
    total_order = orders.count()
    total_delivered = orders.filter(status="Deliveried").count()
    total_pending = orders.filter(status="Pending").count()
    #print(orders)
    context ={'orders':orders, 'total_order':total_order, 'total_delivered':total_delivered, 'total_pending':total_pending}
    return render(request, 'accounts/userpage.html',context)


@login_required(login_url='login')
@allowed_user(allowed_grp=['customer'])
def accountSetting(request):
    customer = request.user.customer
    #print(customer)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('setting')
    context = {'form':form}
    return render(request, 'accounts/accountSetting.html', context)


@login_required(login_url='login')
@only_admin
def home(request):
    customers = Customer.objects.all()
    #print(customers[0])
    orders = Order.objects.all()

    total_order = orders.count()
    total_delivered = orders.filter(status="Deliveried").count()
    total_pending = orders.filter(status="Pending").count()

    context = {'customers':customers, 'orders':orders,'total_order':total_order, 'total_delivered':total_delivered, 'total_pending':total_pending}
    return render(request, 'accounts/dashboard.html',context)


@login_required(login_url='login')
@allowed_user(allowed_grp=['admin'])
def product(request):
    products = Product.objects.all()
    return render(request, 'accounts/product.html', {'products':products})


@login_required(login_url='login')
@allowed_user(allowed_grp=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    total_order = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    #load list orders again after searching
    orders = myFilter.qs

    context = {'customer':customer, 'orders':orders, 'total_order':total_order, 'myFilter':myFilter}
    return render(request, 'accounts/cusomer.html',context)


@login_required(login_url='login')
@allowed_user(allowed_grp=['admin'])
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product','status'),extra=5)

    customer = Customer.objects.get(id=pk)
    #hide already Objects
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(initial={'customer':customer})
    
    if request.method == 'POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
        return redirect('/')

    context = {'formset':formset}
    return render(request, 'accounts/orderform.html',context)


@login_required(login_url='login')
@allowed_user(allowed_grp=['admin'])
def updateOrder(request,pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/updateOrder.html', context)


@login_required(login_url='login')
@allowed_user(allowed_grp=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context = {'order':order}
    return render(request, 'accounts/deleteOrder.html', context)
