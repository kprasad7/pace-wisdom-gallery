from django import forms
from .models import Imagee

class ImageFormm(forms.ModelForm):
    class Meta:
        model=Imagee
        fields=("caption","image", "category")