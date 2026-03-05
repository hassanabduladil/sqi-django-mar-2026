from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def events(request):
    return HttpResponse("<section>My birthday</section>"
                        "<section>Another birthday</section>"
                        "<section>And Another birthday</section>"
                        )