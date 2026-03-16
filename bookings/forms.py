from django import forms
from .models import BookingSlot
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError


class BookingSlotForm(forms.ModelForm):
    class Meta:
        model = BookingSlot
        fields = ['date', 'start_time', 'end_time',
                  'status', 'client', 'client_note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
            'client_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):

        self.physiotherapist = kwargs.pop('physiotherapist', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        physio = self.physiotherapist

        if date and start_time and physio:
            exists = BookingSlot.objects.filter(
                physiotherapist=physio,
                date=date,
                start_time=start_time
            ).exists()

            if exists:
                raise forms.ValidationError(
                    "A slot for this date and time already exists in your schedule."
                )

        return cleaned_data
