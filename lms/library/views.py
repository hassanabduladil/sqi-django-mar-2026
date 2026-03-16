from django.shortcuts import render
from django.http import HttpResponse

from .models import Book
from authors.models import Author
# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    context = {
        "all_books": Book.objects.all(),
        "books_in_desc": Book.objects.order_by('title')
    }
    return render(request, "library/book-list.html", context)

