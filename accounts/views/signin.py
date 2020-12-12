from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.forms.signup import SignupForm
from django.contrib.auth.views import LoginView
from accounts.forms.signin import SignInForm


# def signin_user(request):
#     if request.method == 'GET':
#         context = {
#             'signin_form': SigninForm(),
#         }
#         return render(request, 'auth/signin.html', context)
#
#     else:
#         signin_form = SigninForm(request.POST)
#         if signin_form.is_valid():
#             username = signin_form.cleaned_data['username']
#             password = signin_form.cleaned_data['password']
#             user = authenticate(username=username, password=password)
#
#             if user:
#                 login(request, user)
#                 return redirect('current user profile')
#
#             context = {
#                 'signup_form': SignupForm(),
#             }
#             return render(request, 'auth/signin.html', context)


class SignInView(LoginView):
    template_name = "auth/signin.html"
    form_class = SignInForm
