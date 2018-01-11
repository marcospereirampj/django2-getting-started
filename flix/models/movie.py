from django.db import models

from flix.models.category import Category


class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    synopsis = models.TextField(verbose_name='Synopsis')
    pub_date = models.DateTimeField(verbose_name='Date Published')
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title
