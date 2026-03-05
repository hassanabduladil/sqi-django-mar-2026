from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def hobbies(request):
    return render(request, "hobbies.html")

def goals(request):
    return render(request, "goals.html")