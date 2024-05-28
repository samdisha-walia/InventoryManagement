from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'dash/Home.html')

def Inventory(request):
    return render(request, 'dash/Inventory.html')

def Orders(request):
    return render(request, 'dash/Orders.html')

def Analytics(request):
    return render(request, 'dash/Analytics.html')

def Settings(request):
    return render(request, 'dash/Settings.html')

def Users(request):
    return render(request, 'dash/Users.html')

def Help(request):
    return render(request, 'dash/Help.html')



