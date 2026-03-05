from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to my django page.")

def get_out(request):
    return HttpResponse("Get out of my django page.")