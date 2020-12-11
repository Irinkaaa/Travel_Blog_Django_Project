from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True,)
    last_name = models.CharField(max_length=20, blank=True,)
    about_me = models.TextField(default='', blank=True,)
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )

    def __str__(self):
        return self.user.username
