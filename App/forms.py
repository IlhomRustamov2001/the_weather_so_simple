from django import forms
from .models import *
from django.forms import TextInput

class CityForm(forms.ModelForm):
    class Meta:
        model=CityModel
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input', 'placeholder':'Add city'})}