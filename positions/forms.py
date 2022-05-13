from django import forms
from .models import Position

class PositionForm(forms.ModelForm):
    
    class Meta:
        model = Position
        fields = ("title",'description','amount')
