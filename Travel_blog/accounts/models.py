from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(UserModel, editable=False, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True,)
    last_name = models.CharField(max_length=20, blank=True,)
    email = models.EmailField(blank=True,)
    about_me = models.TextField(default='', blank=True,)
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
