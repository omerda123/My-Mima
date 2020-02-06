from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "facts"

urlpatterns = [
    path('', views.index, name="index"),
    path('artist/<int:artist_id>/', views.artist_page, name="artist-page"),
    path('artist/<str:letter>/', views.artist_letter, name="artist-page"),
    path('song/<int:song_id>', views.facts_page, name="artist-page"),
    path('song/<str:letter>', views.songs_letter, name="artist"),
    path('crawler/', views.crawler_view, name="crawler")
]
