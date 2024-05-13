from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    path('', views.Home, name = 'Home'),
    path('Home/', views.Home, name = 'Home'),
    path('Inventory/', views.Inventory, name = 'Inventory'),
    path('Orders/', views.Orders, name = 'Orders'),
    path('Analytics/', views.Analytics, name = 'Analytics'),
    path('Settings/', views.Settings, name = 'Settings'),
    path('Users/', views.Users, name = 'Users'),
    path('Help/', views.Help, name = 'Help'),
    path('Notifications/', views.Notifications, name = 'Notifications'),
    path('Logout/', views.Logout, name = 'Logout'),
]
