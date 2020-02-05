from django.http import HttpResponse
from . import models
from django.shortcuts import render
# from . import crawler


# Create your views here.
def index(request):
    # get_all_artists()
    return HttpResponse("Hello World!")


def crawler_view(request):
    all_artists = models.Artist.objects.all()
    all_songs = models.Song.objects.all()
    all_facts = models.Fact.objects.all()
    # crawler.delete_all_records()
    context = {
        'buttons': [('Get Artists', crawler.get_all_artists), ('Get Songs', crawler.get_all_songs),
                    ('Get Facts', crawler.get_all_facts)],
        'artists': all_artists,
        'songs': all_songs,
        'facts': all_facts,
    }
    return render(request, 'facts/note_form.html', context)
