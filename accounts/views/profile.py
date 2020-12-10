from django.contrib.auth.models import User
from django.shortcuts import render

from accounts.forms.profile import ProfileForm


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    context = {
        'user': user,
        'profile': user.userprofile,
        'form': ProfileForm(),
    }
    return render(request, 'profile.html', context)
