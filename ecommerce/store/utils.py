import json
from .models import *

def cookieCart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])   
    except:
        cart = {}

    print('cart:',cart)
    items = []
    #Khong dang nhap tai khoan nao
    order = {'get_cart_total':0,'get_cart_items':0,'shipping':False}
    cartItems = order['get_cart_items']
    # Get cookie data
    for i in cart:
        try:
            cartItems += cart[i]['quanity']
            
            product = Product.objects.get(id=i)
            total = (product.price*cart[i]['quanity'])
            # Sumary of the price
            order['get_cart_total']+=total
            # Sumary of the items
            order['get_cart_items']+=cart[i]['quanity']
            # create items
            item = {
                'product':{
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quanity': cart[i]['quanity'],
                'get_total': total
            }
            items.append(item)
            if product.digital == False:
                order['shipping'] = True
        except:
            pass
    return {'items':items, 'order':order, 'cartItems':cartItems}

def cookieData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        #Tạo customer nếu không có trong 'Order' model
        order, created = Order.objects.get_or_create(customer=customer,complete=False)
        #Lấy các item trong 'OrderItem' model
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        items = cookieData['items']
        order = cookieData['order']
    return {'items':items, 'order':order, 'cartItems':cartItems}

def guestOrder(request,data):
    print('User is not logged in..')
    print('COOKIES:',request.COOKIES)
    # User is not logged in..
    # COOKIES: {'cart': '{"1":{"quanity":1}}', 'csrftoken': '87U6CGF9wHbiKd37Fq4Q8GsWOlLK6NsRK44rIy5Yq4pm1ILBNVDFVlDBkvy5zs78'}
    name = data['form']['name']
    email = data['form']['email']
    
    cookieData = cookieCart(request)
    items = cookieData['items']


    #Nếu email này đã mua thì sài luôn, không thì tạo mới
    customer, created = Customer.objects.get_or_create(
        email = email,
        )
    customer.name = name
    customer.save()
    print('name:',name)

    order = Order.objects.create(
        customer=customer,
        complete=False,
        )
    # Thêm vô database
    for item in items:
        product= Product.objects.get(id=item['product']['id'])
        orderItem = OrderItem.objects.create(
            product=product,
            order = order,
            quanity = item['quanity'],
        )
    return customer, order