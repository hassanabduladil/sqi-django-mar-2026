from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "index.html")
def profile(request):
    return render(request, "profile.html")
def help(request):
    return render(request, "help.html")
def services(request):
    return render(request, "services.html")