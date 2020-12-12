from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

# @login_required
# def signout_user(request):
#     logout(request)
#     return redirect('index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')
