from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product

# Create your views here.

@login_required(login_url = 'user-login')
def Home(request):
    return render(request, 'dash/Home.html')

@login_required(login_url = 'user-login')
def Inventory(request):
    return render(request, 'dash/Inventory.html')

@login_required(login_url = 'user-login')
def Orders(request):
    return render(request, 'dash/Orders.html')

@login_required(login_url = 'user-login')
def Analytics(request):
    return render(request, 'dash/Analytics.html')

@login_required(login_url = 'user-login')
def Settings(request):
    return render(request, 'dash/Settings.html')