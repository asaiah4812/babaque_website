from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
    
class Order(models.Model):
    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    DELIVERED = 'delivered'

    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered')
    )
    
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False, )
    total_cost = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)

    class Meta:
        ordering = ['-create_at']
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name

