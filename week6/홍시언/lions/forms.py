from django import forms
from .models import Lion

class LionForm(forms.ModelForm):
    class Meta:
        model = Lion
        fields = ['name', 'track']