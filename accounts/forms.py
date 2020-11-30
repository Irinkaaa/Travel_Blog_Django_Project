from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import UserProfile


class SigninForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(),
    )


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def email_required(self):
        email = self.cleaned_data.get('email', False)
        if not email:
            raise forms.ValidationError('Email is required')
        return email


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )
