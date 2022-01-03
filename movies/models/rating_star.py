from django.db import models


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Value', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating star'
        verbose_name_plural = 'Rating stars'
