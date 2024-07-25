from django import forms
from order.models import Order

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()