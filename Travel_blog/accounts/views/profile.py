from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from Travel_blog.accounts.forms.profile import ProfileForm
from Travel_blog.app.models import Destination


def profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    profile = user.profile
    destinations = Destination.objects.filter(user_id=user.id)
    if request.method == 'GET':
        context = {
            'user': user,
            'profile': profile,
            'form': ProfileForm(),
            'destinations': destinations,
        }
        return render(request, 'profile.html', context)
    else:
        form = ProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')
        return redirect('current user profile')
