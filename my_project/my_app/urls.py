from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('services/', views.services, name="services"),
    path('help/', views.help, name="help"),
    path('profile/', views.profile, name="profile"),
]