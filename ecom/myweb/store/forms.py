from dataclasses import fields
from django import forms
from .models import createmodel

class createform(forms.Form):
    title = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget= forms.CheckboxInput)
    views = forms.IntegerField(widget=forms.TextInput)
    date = forms.DateField(widget=forms.SelectDateWidget)

class myform(forms.ModelForm):
     class Meta:
        model = createmodel
        exclude = ['img']