from django import forms
from .models import Gallery

class ImgForm(forms.ModelForm):
    class Meta:
        model=Gallery
        fields='__all__'

