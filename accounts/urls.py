from django.urls import path, include
from accounts.views import user_profile, signin_user, signup_user, signout_user

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signup/', signup_user, name='signup user'),
    path('signin/', signin_user, name='signin user'),
    path('signout/', signout_user, name='signout user'),
]