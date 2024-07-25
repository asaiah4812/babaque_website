from django.shortcuts import render, get_object_or_404
from .models import Product
from payment.models import Payment
from cart.cart import Cart
from .forms import AddToCartForm

# Create your views here.

def product(request, product__slug):
   cart = Cart(request)
   product = get_object_or_404(Product, slug=product__slug)
   
   form = AddToCartForm()

   if request.method == 'POST':
      form = AddToCartForm(request.POST)
      if form.is_valid():
           quantity = form.cleaned_data['quantity']
           cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
           messages.success(request, 'The product has been added to cart')

      return redirect('product:product', slug=slug)
   
   context = {
      'product': product,
      'form':form,
   }
   return render(request, 'product/product.html', context)