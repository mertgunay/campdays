from django import forms
from booking.models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = {
            'check_in',
            'check_out',
            'guests',
            'tents',
        }
