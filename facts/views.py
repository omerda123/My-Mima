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
        'letters': LETTERS,
        'url_prefix': '../../artist/'

    }
    return render(request, 'facts/artist_letter.html', context)


def artist_page(request, artist_id):
    artist = Artist.objects.filter(id=artist_id)
    songs = Song.objects.filter(artist=artist_id)
    print(songs)
    context = {
        'artist': artist[0],
        'songs': songs,
        'letters': LETTERS,

    }
    return render(request, 'facts/artist_page.html', context)


def facts_page(request, song_id):
    facts = Fact.objects.filter(song_id=song_id)
    song = Song.objects.get(id=song_id)
    context = {
        'facts': facts,
        'song': song.name,
        'artist': song.artist.name,
        'letters': LETTERS,

    }
    return render(request, 'facts/fact_page.html', context)


def songs_letter(request, letter):
    letter_songs = Song.objects.filter(name__startswith=letter)

    context = {
        'artists': letter_songs,
        'letters': LETTERS,
        'url_prefix': ''

    }
    return render(request, 'facts/artist_letter.html', context)


def search_result(request):
    if request.method == 'POST':
        q = request.POST['search']
        print(q)
        Artists_result = Artist.objects.filter(name__contains=q)
        songs_result = Song.objects.filter(name__contains=q)
        facts_result = Fact.objects.filter(fact__contains=q)
        context = {
            'artists': Artists_result,
            'songs': songs_result,
            'facts': facts_result,
            'letters': LETTERS,
        }
    return render(request, 'facts/search_result.html', context)
