from django.db import models


class Artists(models.Model):
    name = models.CharField(max_length=200)


class Songs(models.Model):
    artist_id = models.ForeignKey(Artists, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

class facts(models.Model):
    song_id = models.ForeignKey(Songs, on_delete=models.CASCADE)
    fact = models.TextField()
