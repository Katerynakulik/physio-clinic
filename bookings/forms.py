from django import forms
from .models import BookingSlot
from django.utils import timezone
from datetime import datetime
from django.core.exceptions import ValidationError


class BookingSlotForm(forms.ModelForm):
    class Meta:
        """
    Form for manual creation/editing of booking slots by physiotherapists.
    Includes custom widgets for Bootstrap styling and date/time pickers.
    """
        model = BookingSlot
        fields = ['date', 'start_time', 'end_time',
                  'status', 'client', 'client_note']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'start_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'end_time': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'client': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'client_note': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 2}
            ),
        }

    def __init__(self, *args, **kwargs):
        """
        Initializes the form with a specific physiotherapist instance
        to facilitate overlap validation.
        """

        self.physiotherapist = kwargs.pop('physiotherapist', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        """
        Custom validation to ensure no duplicate slots are created
        for the same physiotherapist at the same time.
        """
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start_time = cleaned_data.get('start_time')
        physio = self.physiotherapist

        if date and start_time:
            now = timezone.localtime()

            slot_datetime = timezone.make_aware(
                datetime.combine(date, start_time)
            )

            if slot_datetime < now:
                raise forms.ValidationError(
                    "You cannot create a slot in the past. "
                    "Please select a future time."
                )

            if physio:
                exists = BookingSlot.objects.filter(
                    physiotherapist=physio,
                    date=date,
                    start_time=start_time
                ).exists()

                if exists:
                    raise forms.ValidationError(
                        "A slot for this date and time "
                        "already exists in your schedule."
                    )

        return cleaned_data
