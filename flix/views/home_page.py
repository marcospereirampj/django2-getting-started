
from django.views import generic

from ..models.genre import Genre


class HomePageView(generic.ListView):
    template_name = 'home_page.html'
    context_object_name = 'genres'

    def get_queryset(self):
        return Genre.objects.all()
