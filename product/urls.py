from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('<slug:product__slug>/', views.product, name='product'),
]
