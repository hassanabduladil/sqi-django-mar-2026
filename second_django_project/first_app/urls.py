from django.urls import path

from . import views

urlpatterns = [
    path('welcome/', views.welcome, name="welcome"),
    path('get-out/', views.get_out, name="get_out"),
]