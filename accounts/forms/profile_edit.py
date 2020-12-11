from django import forms
from django.contrib.auth.models import User
from app.models import UserProfile


class EditUserCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = User
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = UserProfile
        fields = '__all__'
