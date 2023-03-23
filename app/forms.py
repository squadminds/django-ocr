from django import forms
from app.models import Images

class ImageForm(forms.ModelForm):
    class Meta:
        model=Images
        fields=('image',)