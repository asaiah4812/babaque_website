from django.urls import path
from . import views

app_name='core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('login/', views.login_user, name='login'),
    # path('validate/', views.validateuser, name='validate_login'),
    path('signup/', views.register_user, name='signup'),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('logout/', views.logout_user, name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('mail/', views.simple_mail, name='mail'),
    path('myaccount/edit/', views.edit_myaccount, name='edit_myaccount')
]
