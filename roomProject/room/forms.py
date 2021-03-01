from django import forms 

class SearchForm(forms.Form):
    distance = forms.IntegerField()
    charge = forms.IntegerField()
    rating = forms.IntegerField()