from django.http import HttpResponse
from . import models
from django.shortcuts import render
from .models import Artist, Song, Fact

LETTERS = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת']


# from . import crawler


# Create your views here.
def index(request):
    context = {
        'letters': LETTERS
    }
    return render(request, 'facts/index.html', context)


def crawler_view(request):
    all_artists = models.Artist.objects.all()
    all_songs = models.Song.objects.all()
    all_facts = models.Fact.objects.all()
    context = {
        'buttons': ['Get Artists', 'Get Songs', 'Get Facts'],
        'artists': all_artists,
        'songs': all_songs,
        'facts': all_facts,
    }
    return render(request, 'facts/note_form.html', context)


def artist_letter(request, letter):
    letter_artists = Artist.objects.filter(name__startswith=letter)

    context = {
        'artists': letter_artists,
        'letters': LETTERS

    }
    return render(request, 'facts/artist_letter.html', context)


def artist_page(request, artist_id):
    artist = Artist.objects.filter(id=artist_id)
    songs = Song.objects.filter(artist=artist_id)
    print(songs)
    context = {
        'artist': artist[0],
        'songs': songs
    }
    return render(request, 'facts/artist_page.html', context)
