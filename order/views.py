from django.shortcuts import render, redirect, get_object_or_404
from . models import Order, OrderItem
from cart.cart import Cart
from django.contrib import messages
from django.conf import settings
from order.forms import OrderForm
from payment.models import Payment
import json
import stripe
from django.http import JsonResponse
from product.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def start_order(request):
    form = OrderForm()
    cart = Cart(request)
    orderItem = []
    if request.method == 'POST':

        form = OrderForm(request.POST)
        if form.is_valid():
            user = request.user
            total_cost = 0

            for item in cart:
                product_in_cart = item['product']
                quantity_in_cart = int(item['quantity'])
                product_instance = get_object_or_404(Product, pk=product_in_cart.id)
                order = form.save(commit=False)
                order.user = user
                order.total_cost = product_instance.price * quantity_in_cart

                total_cost += order.total_cost
                order.total_cost = total_cost
                order.save()
                orderItem = OrderItem.objects.create(order=order, product=product_instance, price=product_instance.price * quantity_in_cart, quantity=quantity_in_cart)

            payment = Payment.objects.create(amount=total_cost, email=user.email, user=user)
            payment.save()
            pub_key = settings.PAYSTACK_PUBLISABLE

            cart.clear()

        # Redirect to a success page or process payment
            context = {
                # 'order': order,
                'total_cost':total_cost,
                'orderitem': orderItem,
                'payment': payment,
                'paystack_pub_key': pub_key,
                'amount': payment.amount_value()
            }
    
            return render(request, 'cart/make_payment.html', context)
        else:
            form_erros = form.errors.as_text()
            messages.warning(request, f"Error: Invalid Data. Details: {form_erros}")
            return redirect('order:start_order')

    form =  OrderForm()
    context = {'form':form}
    return render(request, 'cart/checkout.html', context)

@login_required
def invoice(request):
    return render(request, 'cart/invoice.html')


@login_required
def all_orders(request):
    orderitems = OrderItem.objects.all()
    count = orderitems.count()
    context = {'count':count, 'orderitems':orderitems}
    return render(request, 'order/all_orders.html', context)


@login_required
def order_invoice(request, pk):
    order = OrderItem.objects.get(id=pk)
    payment = Payment.objects.filter().first()
    # orderitems = OrderItem.objects.all()
    context = {'order':order, 'payment':payment}
    return render(request, 'order/invoice.html', context)




# def start_order(request):
#     form = OrderForm()
#     cart = Cart(request)
    
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
        
#         if form.is_valid():
#             total_price = 0
#             items = []
#             for item in cart:
#                 product = item['product']
#                 total_price += product.price * int(item['quantity'])
#                 obj = {
#                     'price_data': {
#                         'currency': 'usd',
#                         'product_data': {
#                             'name': product.name,
#                         },
#                         'unit_amount': product.price,
#                     },
#                     'quantity': item['quantity']
#                 }
#                 items.append(obj)

#             stripe.api_key = settings.STRIPE_API_KEY_HIDDEN
#             session = stripe.checkout.Session.create(
#                 payment_method_types=['card'],
#                 line_items=items,
#                 mode='payment',
#                 success_url='http://127.0.0.1:8000/cart/success/',
#                 cancel_url='http://127.0.0.1:8000/cart/cancel/',
#             )
#             payment_intent = session.payment_intent

#             order = form.save(commit=False)
#             order.user = request.user
#             order.payment_intent = payment_intent
#             order.paid_amount = total_price
#             order.paid = True
#             order.save()

#             for item in cart:
#                 product = item['product']
#                 quantity = int(item['quantity'])
#                 price = product.price * quantity
#                 OrderItem.objects.create(order=order, product=product, price=price, quantity=quantity)

#             cart.clear()

#             return JsonResponse({'session': session, 'order': payment_intent})

#     else:
#         form = OrderForm()

#     return render(request, 'cart/checkout.html', {'form': form, 'cart': cart})
