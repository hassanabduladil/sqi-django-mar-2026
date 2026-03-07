from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return render(request, "my_app/my_app.html")