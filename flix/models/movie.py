import datetime

from django.db import models

from .genre import Genre


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    synopsis = models.TextField(verbose_name='Synopsis')
    pub_date = models.DateField(verbose_name='Date Published')
    genre = models.ForeignKey(Genre, verbose_name='Genre', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= datetime.date.today() - datetime.timedelta(days=30)

    class Meta:
        verbose_name_plural = "movies"
        ordering = ['-pub_date']
