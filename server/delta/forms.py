from django import forms
from .models import status
class nodemcu(forms.ModelForm):
    class Meta:
        model=status
        fields=[
        'title',
        'moisture'
        ]
