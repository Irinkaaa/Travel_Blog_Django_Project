from django import forms
from accounts.models import Profile
from app.models import Destination


class DestinationFrom(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'

