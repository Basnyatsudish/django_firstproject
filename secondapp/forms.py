from .models import Photo
from django import forms
from django.forms import ModelForm


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('file', )
