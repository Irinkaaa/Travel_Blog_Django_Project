from django import forms
from accounts.models import UserProfile
from app.models import Destination


class DestinationFrom(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'

    def clean_user(self):
        if not self.cleaned_data['user']:
            return UserProfile()
        return self.cleaned_data['user']
