from django.contrib import admin
from . import models
# Register your models here.

admin.site.registart(models.Artist)
admin.site.registart(models.Song)
admin.site.registart(models.Fact)