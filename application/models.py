from django.db import models


class City(models.Model):
    """ Модель города, для определения погоды """
    title = models.CharField(max_length=69, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['-id']
