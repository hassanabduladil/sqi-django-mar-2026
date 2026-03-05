from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def hiss(request):
    return HttpResponse("Mtcheew.")

def you(request):
    return HttpResponse("If i can do it then why can't you.")