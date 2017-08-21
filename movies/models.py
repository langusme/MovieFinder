from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    channel = models.CharField(max_length=30)
    air_date = models.DateField(blank=True)
    air_time = models.TimeField(blank=True)

    def __str__(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'pk': self.pk}, )

