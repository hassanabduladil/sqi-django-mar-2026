from django.shortcuts import render

from django.http  import HttpResponse
# Create your views here.

def books(request):
    return HttpResponse("<ul>"
                        "<li>To Kill a Mockingbird</li>" 
                        "<li>1984</li>"
                        "<li>The Busby Babes</li>"
                        "<li>Pele</li>"
                        "<li>Money Heist</li>"
                        "</ul>")

def special(request):
    return HttpResponse("<div>"
                        "<ul>"
                        "<li>To Kill a Mockingbird</li>" 
                        "<li>1984</li>"
                        "</ul>"
                        "</div>")