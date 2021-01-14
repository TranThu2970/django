from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .utils import cookieCart, cookieData, guestOrder

import json
import datetime

# Create your views here.
def store(request):
    Data = cookieData(request)
    cartItems = Data['cartItems']

    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html',context)


def cart(request):

    Data = cookieData(request)
    cartItems = Data['cartItems']
    items = Data['items']
    order = Data['order']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/cart.html',context)


def checkout(request):
    Data = cookieData(request)
    cartItems = Data['cartItems']
    items = Data['items']
    order = Data['order']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'store/checkout.html',context)

def main(request):
    context = {}
    return render(request, 'store/main.html',context)

def updateItem(request):
    # lấy dữ liệu file JSON phần body trong file cart.js: producId vs action
    # listen button=> dataset => json =>...views
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('action:',action)
    print('productId:',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    #Tạo customer nếu không có trong 'Order' model
    order, created = Order.objects.get_or_create(customer=customer,complete=False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    if action=='add':
        orderItem.quanity = (orderItem.quanity + 1)
    elif action == 'remove':
        orderItem.quanity = (orderItem.quanity - 1)

    orderItem.save()
    if orderItem.quanity <=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
            
    else:
        customer, order = guestOrder(request,data)
            

    #For authenticate user and not_auth user
    total = float(data['form']['total'])
    order.transaction_id = transaction_id
    # Kiểm tra nếu kết quả từ frontEnd gửi về đúng thì ok
    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping== True:
        ShippingAddress.objects.create(
            customer = customer,
            order = order,
            address = data['shipping']['address'],
            city = data['shipping']['city'],
            state = data['shipping']['state'],
            zipcode = data['shipping']['zipcode'],
        )

    return JsonResponse('Order completed!', safe=False)
