from django import forms
from .models import Car

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = (
            'name',
            'model_type',
            'make',
            'ftype',
            'remarks'
            )