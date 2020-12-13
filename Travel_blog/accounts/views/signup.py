from django.contrib.auth import login
from django.db import transaction
from django.shortcuts import render, redirect
from Travel_blog.accounts.forms.profile import ProfileForm
from Travel_blog.accounts.forms.signup import SignupForm


@transaction.atomic()
def signup_user(request):
    if request.method == 'GET':
        context = {
            'signup_form': SignupForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/signup.html', context)

    else:
        signup_form = SignupForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if signup_form.is_valid() and profile_form.is_valid():
            user = signup_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('current user profile')

        context = {
            'signup_form': SignupForm(),
            'profile_form': ProfileForm(),
        }
        return render(request, 'auth/signup.html', context)
