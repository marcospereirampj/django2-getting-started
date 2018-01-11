from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(verbose_name='Description')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "genres"
