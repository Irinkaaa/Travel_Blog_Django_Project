from django.contrib.auth import logout
from django.shortcuts import render, redirect


def user_profile(request):
    pass


def signup_user(request):
    pass


def signout_user(request):
    logout(request)
    return redirect('index')
