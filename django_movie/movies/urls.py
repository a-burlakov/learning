from django.urls import path

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path("<str:slug>/", views.MovieDetailView.as_view(), name="movie_detail")
]