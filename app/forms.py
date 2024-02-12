from django import forms
from .models import Event

class RegistrationForm(forms.ModelForm):
    start_date_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'YYYY-MM-DDTHH:MM'}))
    end_date_time = forms.DateTimeField(widget=forms.widgets.DateTimeInput(attrs={'type': 'datetime-local', 'placeholder': 'YYYY-MM-DDTHH:MM'}))
    
    
    class Meta:
        model = Event
        fields = ("title","description","start_date_time","end_date_time","image","venue","organizer")
