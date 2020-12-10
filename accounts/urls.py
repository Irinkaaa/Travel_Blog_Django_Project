from django.urls import path, include
from accounts.views.profile import user_profile
from accounts.views.profile_edit import edit_profile
from accounts.views.signin import signin_user
from accounts.views.signout import signout_user
from accounts.views.signup import signup_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('signout/', signout_user, name='signout user'),
]
