from users.forms import StyleFormMixin
from .models import Appointment
from django import forms

class AppointmentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('user',)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['password'].widget = forms.HiddenInput()
