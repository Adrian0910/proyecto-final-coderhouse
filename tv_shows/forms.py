from django import forms

class Form_tv_shows(forms.Form):
    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    year = forms.FloatField()
    director = forms.CharField(max_length=40)
    actors = forms.CharField(max_length=80)
    description = forms.CharField(max_length=300)
   