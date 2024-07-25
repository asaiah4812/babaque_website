from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'country', 'state', 'city', 'phone', 'create_at']
    list_filter = ['status', 'create_at']
    search_fields = ['first_name', 'address']
    list_display_links = ['first_name', 'create_at']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['price', 'quantity']
