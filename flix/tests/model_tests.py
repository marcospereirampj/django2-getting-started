import datetime

from django.test import TestCase

from flix.models.movie import Movie


class MovieModelTests(TestCase):

    def test_was_published_recently_with_recent_movie(self):
        """
        was_published_recently() returns True whose pub_date is
        recent (pub_date between now() and datetime.timedelta(-30).
        """
        pub_date = datetime.date.today() - datetime.timedelta(days=10)
        recent_movie = Movie(title='Simple Movie', synopsis='Simple Synopsis', pub_date=pub_date)
        self.assertIs(recent_movie.was_published_recently(), True)

    def test_was_published_recently_with_old_movie(self):
        """
        was_published_recently() returns True whose pub_date is
        recent (pub_date between now() and datetime.timedelta(-30).
        """
        pub_date = datetime.date.today() - datetime.timedelta(days=60)
        old_movie = Movie(title='Simple Movie', synopsis='Simple Synopsis', pub_date=pub_date)
        self.assertIs(old_movie.was_published_recently(), False)

    def test_was_published_recently_with_future_movie(self):
        """
        was_published_recently() returns False for movie whose pub_date
        is in the future.
        """
        pub_date = datetime.date.today() + datetime.timedelta(days=60)
        future_movie = Movie(title='Simple Movie', synopsis='Simple Synopsis', pub_date=pub_date)
        self.assertIs(future_movie.was_published_recently(), False)

    def test_str_movie(self):
        title = 'Simple Movie'
        movie = Movie(title=title, synopsis='Simple Movie')
        self.assertEqual(title, str(movie))


class GenreModelTests(TestCase):

    def test_str_movie(self):
        title = 'Simple Genre'
        genre = Movie(title=title, synopsis='Simple Synopsis')
        self.assertEqual(title, str(genre))
