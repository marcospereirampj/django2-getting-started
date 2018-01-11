
from django.views import generic

from ..models.genre import Genre


class GenreDetailView(generic.DetailView):
    template_name = 'genre_detail.html'
    model = Genre
