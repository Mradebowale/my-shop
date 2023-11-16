from django import forms
from .models import contactform, Booking


SERVICE_TYPE = (
    ("1", "Service 1"),
    ("2", "Service 2"),
    ("3", "Service 3")
)


class contactform1(forms.ModelForm):
    class Meta:
        model = contactform
        fields = "__all__"




class bookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
    