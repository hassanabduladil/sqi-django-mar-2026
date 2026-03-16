from django.shortcuts import render
from .models import Artist, Album


def home(request):
    return render(request, 'home.html')


def artists(request):
    artist_list = Artist.objects.all().order_by('debut_year')
    return render(request, 'artists.html', {'artists': artist_list})


def albums(request):
    album_list = Album.objects.all().order_by('release_date')
    return render(request, 'albums.html', {'albums': album_list})