from django import forms
from django.contrib.auth.models import User

class ClientRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30, 
        required=True, 
        help_text='Required. Please enter your real name.'
    )
    last_name = forms.CharField(
        max_length=30, 
        required=True
    )
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding Bootstrap classes to fields for consistent UI
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user