from django.contrib.auth.models import User
from django.db import models


class Destination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    country = models.CharField(max_length=50, blank=False)
    year = models.IntegerField(blank=False)
    image = models.ImageField(
        upload_to='destinations',
    )

    def __str__(self):
        return f'{self.title}'
