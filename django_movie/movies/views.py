from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Movie


class MoviesView(ListView):
    """
    Список фильмов
    """

    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetailView(DetailView):
    """
    Описание фильма
    """
    model = Movie
    slug_field = "url"

