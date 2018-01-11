from django.contrib import admin

from .models.movie import Movie
from .models.genre import Genre

admin.site.register(Genre)
admin.site.register(Movie)
