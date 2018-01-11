from django.urls import path

from .views.home_page import HomePageView
from .views.genre_detail import GenreDetailView
from .views.movie_detail import MovieDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='genre_detail'),
    path('movie/<int:pk>/', MovieDetailView.as_view(), name='movie_detail'),
]