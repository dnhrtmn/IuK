from django import forms
from . import models
from bootstrap_datepicker_plus import DatePickerInput


class reservationForm(forms.ModelForm):
    class Meta:
        model = models.reservation
        fields = [
            "start_time",
        ]


class roomForm(forms.ModelForm):
    class Meta:
        model = models.room
        fields = [
            "description",
            "location",
            "size",
        ]
