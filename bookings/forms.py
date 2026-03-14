from django import forms
from .models import BookingSlot
from django.core.exceptions import ValidationError

class BookingSlotForm(forms.ModelForm):
    """
    Form for creating and updating booking slots manually.
    Includes validation to prevent duplicate time slots.
    """
    class Meta:
        model = BookingSlot
        fields = ['date', 'start_time', 'end_time', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        """
        Custom validation to ensure no overlapping or duplicate slots 
        exist for the same physiotherapist at the same time.
        """
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start = cleaned_data.get('start_time')
        
        # 'instance.physiotherapist' is available if we pass the instance to the form
        if self.instance and self.instance.physiotherapist:
            physio = self.instance.physiotherapist
            duplicate = BookingSlot.objects.filter(
                physiotherapist=physio, 
                date=date, 
                start_time=start
            ).exclude(pk=self.instance.pk)
            
            if duplicate.exists():
                raise ValidationError("A slot for this time and date already exists.")
        
        return cleaned_data