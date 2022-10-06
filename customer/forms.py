from django import forms
from .models import  Order, OrderFood


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('date_time', 'state', 'total_price', 'user', )


class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        fields = '__all__'