from django import forms

class Form_reviews(forms.Form):
    name = forms.CharField(max_length=40)
    Rating = forms.FloatField()
    review = forms.CharField(max_length=500)
   