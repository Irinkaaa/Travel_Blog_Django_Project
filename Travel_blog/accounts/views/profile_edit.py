from django.shortcuts import render, redirect
from Travel_blog.accounts.forms.profile_edit import EditProfileForm, EditUserCreationForm
from Travel_blog.accounts.models import Profile


def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(pk=user.id)
    if request.method == 'GET':
        context = {
            'user': user,
            'user_form': EditUserCreationForm(instance=user),
            'profile_form': EditProfileForm(instance=profile),
        }
        return render(request, 'profile_edit.html', context)
    else:
        profile_form = EditProfileForm(request.POST, request.FILES, instance=profile)
        profile_form.user = request.user
        if profile_form.is_valid():
            profile_form.save()
            return redirect('current user profile')

        else:
            context = {
                'user': user,
                'profile_form': profile_form,
            }
            return render(request, 'profile_edit.html', context)
