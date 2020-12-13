from django import forms
from django.contrib.auth import get_user_model
from Travel_blog.accounts.models import Profile

UserModel = get_user_model()


class EditUserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = UserModel
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Profile
        fields = '__all__'
