from django import forms
from .models import Booking

class bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'type', 'message', 'date']