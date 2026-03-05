from django.urls import path

from . import views

urlpatterns = [
    path('you/', views.you, name="you"),
    path('hiss/', views.hiss, name="hiss"),
]