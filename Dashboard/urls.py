from django.contrib import admin
from django.urls import path,include 
from . import views

urlpatterns = [
    #path('', views.Home, name = 'Home'),
    path('Home/', views.Home, name = 'Home'),
    path('Inventory/', views.Inventory, name = 'Inventory'),
    path('Orders/', views.Orders, name = 'Orders'),
    path('profile/', views.profile, name = 'profile'),
    path('Inventory/delete/<int:pk>/', views.product_delete, name = 'product-delete'),
    path('Inventory/update/<int:pk>/', views.product_update, name = 'product-update'),
    path('Staff/', views.Staff, name = 'Staff'),
    path('Staff/details/<int:pk>/', views.Staff_details, name = 'Staff-details')

]
