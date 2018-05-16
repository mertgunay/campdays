from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import campLocation
from datetime import datetime 

class createAreaForm(forms.ModelForm):
    lat  = forms.DecimalField(label=(u'lat'), max_digits=9, decimal_places=6)
    lng = forms.DecimalField(label=(u'lng'),  max_digits=9, decimal_places=6)
    name = forms.CharField(label=(u'name'))
    title=forms.CharField(label=(u'Title'))
    description=forms.CharField(label=(u'Description'))
    createDate = forms.DateTimeField(initial=datetime.now(), required=False)
    

    class Meta:
        model=campLocation
        fields = (
            'lat',
            'lng',
            'name',
            'title',
            'description',
            'max_guests',
            'max_tents',
            )