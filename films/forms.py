from django import forms

class Form_films(forms.Form):
    poster = forms.ImageField()
    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    year = forms.FloatField()
    director = forms.CharField(max_length=40)
    actors = forms.CharField(max_length=80)
    description = forms.CharField(max_length=300)
   