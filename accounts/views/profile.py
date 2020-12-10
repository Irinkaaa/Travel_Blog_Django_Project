from django.contrib.auth.models import User
from django.shortcuts import render
from accounts.forms.profile import ProfileForm
from app.models import Destination


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    destinations = Destination.objects.filter(user_id=user.id)
    context = {
        'user': user,
        'profile': user.userprofile,
        'form': ProfileForm(),
        'destinations': destinations,
    }
    return render(request, 'profile.html', context)


