from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from accounts.forms import SigninForm, SignupForm, ProfileForm


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    context = {
        'user': user,
        'profile': user.userprofile,
        'form': ProfileForm(),
    }
    return render(request, 'profile.html', context)


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


def signin_user(request):
    if request.method == 'GET':
        context = {
            'signin_form': SigninForm(),
        }
        return render(request, 'auth/signin.html', context)

    else:
        signin_form = SigninForm(request.POST)
        if signin_form.is_valid():
            username = signin_form.cleaned_data['username']
            password = signin_form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                return redirect('current user profile')

            context = {
                'signup_form': SignupForm(),
            }
            return render(request, 'auth/signin.html', context)


@login_required
def signout_user(request):
    logout(request)
    return redirect('index')
