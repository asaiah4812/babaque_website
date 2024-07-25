from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls', namespace='core')),
    path('product/', include('product.urls', namespace='product')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    # path('qr/', include('qrauth.urls')),
    path('accounts/', include('allauth.urls')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace='social'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
