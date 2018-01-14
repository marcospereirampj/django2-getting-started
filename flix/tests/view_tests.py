
from django.urls import reverse
from django.test import TestCase

from freezegun.api import freeze_time

from flix.models.genre import Genre
from flix.models.movie import Movie


class HomePageTests(TestCase):
    """ HomePage Tests"""

    fixtures = ['flix.json']

    def test_all_genres(self):
        """
        Returns all genres
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


class GenreDetailTests(TestCase):
    fixtures = ['flix.json']

    def test_genre_detail_success(self):
        """
        Returns genre detail
        """
        response = self.client.get(reverse('genre_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Action')

    def test_genre_detail_not_found(self):
        """
        Retuns not found - genre detail
        """
        response = self.client.get(reverse('genre_detail', args=(100,)))
        self.assertEqual(response.status_code, 404)

    def test_genre_detail_list_movies(self):
        """
        Returns all genre's movies
        """
        response = self.client.get(reverse('genre_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Avenger')
        self.assertContains(response, 'Star Wars')
        self.assertQuerysetEqual(response.context['genre'].movie_set.all(),
                                 ['<Movie: Star Wars: Episode VIII - The Last Jedi>',
                                  '<Movie: The Avenger>'])

    def test_genre_detail_list_movies_empty(self):
        """
        Returns empty movies list
        """
        response = self.client.get(reverse('genre_detail', args=(3,)))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['genre'].movie_set.all(), [])

    @freeze_time("2017-12-20 00:00:00")
    def test_movie_detail_with_recente_movie(self):
        """
        Returns recent movie
        """
        response = self.client.get(reverse('genre_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Star Wars')
        self.assertContains(response, 'New')


class MovieDetailTests(TestCase):
    fixtures = ['flix.json']

    def test_movie_detail_success(self):
        """
        Returns movie detail
        """
        response = self.client.get(reverse('movie_detail', args=(1,)))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'The Avenger')

    def test_movie_detail_not_found(self):
        """
        Retuns not found - movie detail
        """
        response = self.client.get(reverse('movie_detail', args=(100,)))
        self.assertEqual(response.status_code, 404)
