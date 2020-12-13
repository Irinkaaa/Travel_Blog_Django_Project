from django import forms
from Travel_blog.app.models import Destination


class EditDestinationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Destination
        fields = '__all__'
