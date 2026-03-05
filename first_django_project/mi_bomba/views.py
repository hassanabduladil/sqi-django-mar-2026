from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def why_not(request):
    return HttpResponse("<h1 style=font-size: 10px>If someone asks you why, respond with 'why not'.</h1>")