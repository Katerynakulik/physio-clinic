from django import forms
from .models import BookingSlot
from django.core.exceptions import ValidationError

class BookingSlotForm(forms.ModelForm):
    class Meta:
        model = BookingSlot
        fields = ['date', 'start_time', 'end_time', 'status']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        # Отримуємо фізіотерапевта з аргументів при створенні форми
        self.physiotherapist = kwargs.pop('physiotherapist', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        start = cleaned_data.get('start_time')
        
        # Використовуємо переданого фізіотерапевта для перевірки дублікатів
        physio = self.physiotherapist or (self.instance.physiotherapist if self.instance.pk else None)
        
        if physio and date and start:
            duplicate = BookingSlot.objects.filter(
                physiotherapist=physio, 
                date=date, 
                start_time=start
            )
            if self.instance.pk:
                duplicate = duplicate.exclude(pk=self.instance.pk)
            
            if duplicate.exists():
                raise ValidationError("A slot for this time and date already exists.")
        
        return cleaned_data