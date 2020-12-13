from Travel_blog.app.forms.create import DestinationFrom
from Travel_blog.app.forms.mixin import DisabledFormMixin


class DeleteDestinationForm(DestinationFrom, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
