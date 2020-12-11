from django.urls import path, include
from accounts.views.view_profile import view_profile
from accounts.views.profile import user_profile
from accounts.views.signin import signin_user
from accounts.views.signout import signout_user
from accounts.views.signup import signup_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),

    path('profile/view/', view_profile, name='view profile'),

    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('signout/', signout_user, name='signout user'),
]
