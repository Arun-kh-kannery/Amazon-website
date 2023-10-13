"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
    path('addtocart/<p>',views.addtocart,name="add_to_cart"),
    path('cartview',views.cart_view,name="cart_view"),
    path('cartremove/<p>',views.cart_remove,name="cart_remove"),
    path('cartfullremove/<p>',views.cart_full_remove,name="cart_full_remove"),
    path('order',views.order,name="orders"),
    path('orderview/',views.orderview,name="orderview")
]

