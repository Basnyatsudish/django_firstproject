from django import forms
from . import models
from django.forms import ModelForm


class userform(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your password', max_length=100)


class itemform(forms.ModelForm):
    class Meta:
        model = models.Items
        fields = ['name', 'item_type', 'expiry_date']


