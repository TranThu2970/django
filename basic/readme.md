# boostrap
- class: card: card-header,card-body, card-footer; card-title
- class: table
- class: text-center
- outline: row & col
# Database
- oneToMany: follow the table:
+ order01 = customer01 & product01
+ order02 = customer01 & product02
+ order03 = customer02 & product01
=> 1 customer có thể ở trong nhiều Order
=> 1 product cũng có thể ở trong nhiều Order
- oneToOneField: user <=> customer
# django-filter
- pip3 install django-filter
- INSTALLED_APPS = ['django_filter',]
- use as form!
- filters.py:
    + import django_filters
    + from django_filters import DateFilter, CharFilter

# register
-C1: create a view form to render:
    from django.contrib.auth.forms import UserCreationForm
    => form = UserCreationForm()
-C2: create a form class:
    from django.contrib.auth.forms import UserCreationForm  => style of form
    from django.contrib.auth.models import User             => model for form
    from django import forms
- messages:
    from django.contrib import messages
    =>views: messages.success(request,'Tạo thành công tài khoản: ')
    =>templates:

# login
    views: from django.contrib.auth import authenticate, login, logout
    => user = authenticate(request, username=username, password=password)
    => login(request,user)
    => logout(request)

# decorators
    [from django.contrib.auth.decorators import login_required]
    => @login_required(login_url='login')

# User role based on permissions
    -create decorators.py
    - create user group in admin panel
    - from django.contrib.auth.models import Group => model group

# image
    pip3 install pillow
    MEDIA_ROOT = os.path.join(BASE_DIR,'static/accounts/images')
    MEDIA_URL = '/images/'
    - add link for image in urls.py
    - <form method="POST" action="" enctype="multipart/form-data">
    - form = CustomerForm(request.POST, request.FILES, instance=customer)

# signal

# reset password
    from django.contrib.auth import views as auth_views
    => auth_views.PasswordResetView.as_view()
    => auth_views.PasswordResetDoneView.as_view()
    => auth_views.PasswordResetConfirmView.as_view()
    => auth_views.PasswordResetCompleteView.as_view()
    - SETTINGS:
    #SMTP configuration
EMAIL_BACKEND =''
EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_USE_TLS = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
    https://myaccount.google.com/lesssecureapps  => ON