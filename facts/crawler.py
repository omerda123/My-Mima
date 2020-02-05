from bs4 import BeautifulSoup
import requests
import re
from .models import Artist, Song, Fact

LETTERS = ['א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ', 'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת']


def delete_all_records():
    Artist.objects.all().delete()
    Song.objects.all().delete()
    Fact.objects.all().delete()


def get_all_artists():
    for letter in LETTERS:
        html_doc = requests.get(f'https://mima.co.il/artist_letter.php?let={letter}').text
        soup = BeautifulSoup(html_doc, 'html.parser')
        artists = soup.findAll("a", href=re.compile("artist_page"))
        for artist in artists:
            Artist.objects.create(name=artist.text, mima_id=artist.get('href').split("=")[1])
            print(artist)


def get_all_songs():
    all_artists = Artist.objects.all()
    for artist in all_artists:
        html_doc = requests.get(f'https://mima.co.il/artist_page.php?artist_id={artist.mima_id}').text
        soup = BeautifulSoup(html_doc, 'html.parser')
        songs_table = soup.findAll('table')[5]
        for a in songs_table.findAll('a'):
            if 'fact_page' in a['href']:
                Song.objects.create(artist=artist, name=a.text, mima_id=a.get('href').split("=")[1])
                print(a)


def get_all_facts():
    all_songs = Song.objects.all()
    for song in all_songs:
        html_doc = requests.get(f'https://mima.co.il/fact_page.php?song_id={song.mima_id}').text
        soup = BeautifulSoup(html_doc, 'html.parser')
        songs_table = soup.findAll('table')[5]
        for fact in songs_table.find_all("td")[:-1]:
            a = fact.text.split('נכתב ע"י')
            print(fact)
            Fact.objects.create(song=song, fact=a[0],
                                author=a[1] if len(a) == 2 else "")
