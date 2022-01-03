from datetime import date

from django.db import models

from . import Actor, Category, Genre


class Movie(models.Model):
    title = models.CharField('Title', max_length=100)
    tagline = models.CharField('Tagline', max_length=100)
    description = models.TextField('Description')
    poster = models.ImageField('Poster', upload_to='movies/')
    year = models.PositiveSmallIntegerField('Release year', default=0)
    country = models.CharField('Country', max_length=30)
    directors = models.ManyToManyField(
        Actor, verbose_name='director', related_name='movie_director')
    actors = models.ManyToManyField(
        Actor, verbose_name='actor', related_name='movie_actor')
    genres = models.ManyToManyField(Genre, verbose_name='genres')
    world_premiere = models.DateField('World premiere', default=date.today)
    budget = models.PositiveIntegerField(
        'Budget', default=0, help_text='amount in USD')
    fees_usa = models.PositiveIntegerField(
        'Fees in USA', default=0, help_text='amount in USD')
    fees_world = models.PositiveIntegerField(
        'Fees in USA', default=0, help_text='amount in USD')
    category = models.ForeignKey(
        Category, verbose_name='category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Draft', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
