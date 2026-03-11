from django.urls import path

from . import views

urlpatterns = [
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),
    path('dashboard/', views.dashboard, name='dashboard'),
] 