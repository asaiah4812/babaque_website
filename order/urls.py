from django.urls import path
from . import views

app_name='order'

urlpatterns = [
    path('start-order/', views.start_order, name='start_order'),
    path('make-payment/', views.start_order, name='make_payment'),
    path('all-orders/', views.all_orders, name='orders'),
    path('invoice/<int:pk>/', views.order_invoice, name='invoice'),
]
