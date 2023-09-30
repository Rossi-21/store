from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Order

class OrderForm(ModelForm):
    class Meta:
        #which class are we sending data to
        model = Order
        #use fields = ['customer', 'product'] to select only certian feilds for the form
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
