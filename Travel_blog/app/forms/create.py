from django import forms
from Travel_blog.app.models import Destination


class DestinationFrom(forms.ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'

