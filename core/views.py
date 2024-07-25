from django.shortcuts import render, redirect
from django.contrib import messages, auth
from product.models import Product, Category
from .forms import UserForm
from django.db.models import Q
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from qrauth.models import Website
import qrcode
import random
from django.conf import settings
import os
from qrauth.models import Website
from .models import Testimony
from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.core.mail import send_mail, EmailMessage
from .tokens import account_activation_token


# Create your views here.
otp = 0
def home(request):
    testimonies = Testimony.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories':categories,
        'products': products,
        'active_category':active_category,
        'testimonies': testimonies
    }
    return render(request, 'core/home.html', context)

def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    active_category = request.GET.get('category', '')

    if active_category:
        products = products.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'categories':categories,
        'products': products,
        'active_category':active_category
    }
    return render(request, 'core/shop.html', context)


# activate email

# jus
def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            email= form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'This email is already registered, Plaese use a different email.')
            else:
                # user = 
                # user.is_active = False
                # user.save()
                # activateEmail(request, user, email)
                form.save()
                messages.success(request, f"Account created Successfully Please Login to Continue")
                return redirect('core:login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'Login successfully')
                return redirect('core:home')
            else:
                messages.warning(request, 'This account is inactive')
                return redirect('core:login')
        else:
            messages.error(request, 'Invalid Login detail')
            return redirect('core:login')
    else:
        return render(request, 'accounts/login.html')
    
def logout_user(request):
    logout(request)
    messages.info(request, 'logged out successfully')
    return redirect('core:login')

@login_required
def myaccount(request):
    # website = Website.objects.filter(user=request.user).first()
    return render(request, 'accounts/myaccount.html')

@login_required
def edit_myaccount(request):
    if request.method == "POST":
        user = request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()
        messages.success(request, 'Your account has been updated')
        return redirect('core:myaccount')
    return render(request, 'accounts/edit_account.html')


def about(request):
    obj = Website.objects.get(id=1)
    return render(request, 'core/about.html', {'obj':obj})



# email sending view acions

def simple_mail(request):
    send_mail(subject='That`s you subject', message='That`s you message body', from_email='Hensonasaiah25@gmail.com', recipient_list=['Hensonasaiah21@gmail.com'])

    return HttpResponse('Message sent')