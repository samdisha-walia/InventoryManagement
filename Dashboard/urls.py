from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    #path('', views.Home, name = 'Home'),
    path('Home/', views.Home, name = 'Home'),
    path('Inventory/', views.Inventory, name = 'Inventory'),
    path('Orders/', views.Orders, name = 'Orders'),
    path('profile/', views.profile, name = 'profile'),
    
]
