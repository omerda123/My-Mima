from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    mima_id = models.IntegerField(unique=True)


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    mima_id = models.IntegerField(unique=True)


class Fact(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    fact = models.TextField(default="")
    date_created = models.DateField(null=True)
    author = models.CharField(max_length=200, null= True)
