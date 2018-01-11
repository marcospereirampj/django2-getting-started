
from django.views import generic

from ..models.movie import Movie


class MovieDetailView(generic.DetailView):
    template_name = 'movie_detail.html'
    model = Movie
