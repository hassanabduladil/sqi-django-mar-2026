from django.urls import path
from . import views

app_name = 'freelanceapp'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blog', views.blog_view, name='blog'),
    path('our-reviews', views.testimonials_view, name='testimonials'),
    path('services', views.services_view, name='services'),
]