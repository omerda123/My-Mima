from django.db import models


class Artists(models.Model):
    name = models.CharField(max_length=200)


class Songs(models.Model):
    artist_id = models.ForeignKey(Artists)
    name = models.CharField(max_length=200)
