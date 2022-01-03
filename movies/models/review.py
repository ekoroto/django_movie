from django.db import models

from . import Movie


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField('Name', max_length=150)
    text = models.TextField('Text', max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name='Parent', on_delete=models.SET_NULL, null=True, blank=True)
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='movie')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
