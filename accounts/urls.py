from django.urls import path, include
from accounts.views.profile_edit import view_profile
from accounts.views.profile import profile
# from accounts.views.signin import signin_user
# from accounts.views.signout import signout_user
from accounts.views.signout import SignOutView
from accounts.views.signup import signup_user
from accounts.views.signin import SignInView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/', profile, name='current user profile'),
    path('profile/<int:pk>/', profile, name='user profile'),
    path('profile/view/', view_profile, name='view profile'),

    # function views urls

    path('signup/', signup_user, name='signup user'),
    # path('signin/', signin_user, name='signin user'),
    # path('signout/', signout_user, name='signout user'),

    # CBV urls

    # path('signup/', signup_user, name='signup user'),
    path('signin/', SignInView.as_view(), name='signin user'),
    path('signout/', SignOutView.as_view(), name='signout user'),
]
