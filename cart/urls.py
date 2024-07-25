from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('', views.cart, name='cart'),
    # path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('hx_menu_cart/', views.hx_menu_cart, name='hx_menu_cart'),
    path('hx_cart_total/', views.hx_cart_total, name='hx_cart_total'),
    path('update_cart/<int:product_id>/<str:action>/', views.update_cart, name='update_cart'),
]
