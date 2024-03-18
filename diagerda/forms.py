from users.forms import StyleFormMixin
from .models import *
from django import forms


class AppointmentForm(forms.ModelForm):
    # doctor = forms.ModelChoiceField(widget=forms.Select(attrs={'enabled': 'enabled'}), queryset=Doctor.objects.request.doctor)
    # date = forms.CharField(widget=forms.TextInput(attrs={'disabled': 'disabled'}))
    # user = forms.ModelChoiceField(widget=forms.Select(attrs={'disabled': 'disabled'}),
    #                                      queryset=User.objects.all())
    readonly_fields = ('doctor', 'diagnostic')

    class Meta:
        model = Appointment
        fields = ('user',)
