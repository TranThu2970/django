from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order, Customer

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        exclude =['user','date_created']

class UserCreationForm(UserCreationForm):
    class Meta:
        #import from library to get already User model
        model = User
        fields = ['username', 'email', 'password1', 'password2']
