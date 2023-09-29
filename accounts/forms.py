from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        #which class are we sending data to
        model = Order
        #use fields = ['customer', 'product'] to select only certian feilds for the form
        fields = '__all__'