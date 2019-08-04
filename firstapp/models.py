from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm

class Users(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Items(models.Model):
    name =models.TextField()
    item_type =models.CharField(max_length=100)
    expiry_date =models.DateField()

    def __str__(self):
        return self.name



