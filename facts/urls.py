from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "facts"

urlpatterns = [
    path('', views.index, name="index"),
    path('crawler/', views.crawler_view, name="crawler")
]
