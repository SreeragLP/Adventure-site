"""
URL configuration for myproject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cart import views

app_name="cart"

urlpatterns = [
    path('add/<p>', views.add_to_cart, name="add_to_cart"),
    path('cart_view', views.cart_view, name="cart_view"),

    path('edit/<int:pk>/', views.edit_cart_item, name='edit_cart_item'),

    path('delete/<int:pk>/', views.delete_cart_item, name='delete_cart_item'),


    path('booking/', views.show_booking_form, name='booking_form'),

    path('orderview',views.order_view,name="orderview"),


    path('cancel/<int:pk>/', views.delete_order_view, name='delete_order_view'),

    path('refund', views.refund, name='refund'),


    #path('receipt/', views.send_receipt_email, name='receipt'),









    # path('cart_remove/<p>', views.cart_remove, name="cart_remove"),
    # path('full_remove/<p>', views.full_remove, name="full_remove"),





]
