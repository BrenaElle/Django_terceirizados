from django import forms
from app.services.models import Services

class RequestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RequestForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Services
        fields = ('__all__')

