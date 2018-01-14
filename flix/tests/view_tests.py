
from django.urls import reverse
from django.test import TestCase

from flix.models.genre import Genre
from flix.models.movie import Movie


class HomePageTests(TestCase):
    fixtures = ['flix.json']

    def test_all_genres(self):
        """
        Retuns all genres
        """
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Action")
        self.assertContains(response, "Adventure")
        self.assertContains(response, "Comedy")
        self.assertQuerysetEqual(response.context['genres'],
                                 {'<Genre: Action>': 1, '<Genre: Adventure>': 1, '<Genre: Comedy>': 1},
                                 ordered=False)

    def test_no_genres(self):
        """
        No genres exists
        """

        # Remove all movies and genres
        Movie.objects.all().delete()
        Genre.objects.all().delete()
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['genres'], [])
