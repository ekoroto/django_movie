from django.db import models


class Actor(models.Model):
    """Actors and directors"""

    name = models.CharField('Name', max_length=100)
    age = models.PositiveSmallIntegerField('Age', default=0)
    description = models.TextField('Description')
    image = models.ImageField('Image', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actors and directors'
        verbose_name_plural = 'Actors and directors'
