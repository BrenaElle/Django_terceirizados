from django import forms
from app.services.models import Services
from bootstrap_datepicker_plus import DateTimePickerInput


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(RequestForm, self).__init__(*args, **kwargs)

    def save(self):
        print(self.request)
        request = super(RequestForm, self).save(commit=False)
        request.requester = self.request.user
        request.save()
        return request

    class Meta:
        model = Services
        fields = ('date','place','department','justification')
        widgets = {
            'date': DateTimePickerInput(),
        }
