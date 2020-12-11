from django.shortcuts import render
from accounts.forms.profile_edit import EditProfileForm, EditUserCreationForm


def view_profile(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'user': user,
            'user_form': EditUserCreationForm(instance=user),
            'profile_form': EditProfileForm(instance=user),
        }
        return render(request, 'view_profile.html', context)

    else:
        pass