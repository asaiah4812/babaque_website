from django.forms import ModelForm
from django import forms
from order.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'country', 'state', 'city', 'zipcode', 'phone']
        exclude = ['total_cost']
        widgets = {
        'country': forms.Select(),
        'state': forms.Select(),
        'city': forms.Select(),
    }