from django.db import models


class Destinations(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    country = models.CharField(max_length=50, blank=False)
    image = models.ImageField(upload_to='destinations')

    def __str__(self):
        return f'{self.title}'
