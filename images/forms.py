from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "title-input", "placeholder": "Title"}))
    description = forms.CharField(max_length=250, widget=forms.TextInput(attrs={"class": "description-input", "placeholder": "Description"}))

    class Meta:
        model = Image
        fields = ['title', 'description', 'file']


