from django.db import models

from . import rating_star
from . import Movie


class Rating(models.Model):
    ip = models.CharField('IP address', max_length=15)
    star = models.ForeignKey(
        rating_star.RatingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, verbose_name='movie')

    def __str__(self):
        return f'{self.movie} - {self.star}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
