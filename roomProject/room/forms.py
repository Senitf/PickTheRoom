from django import forms 

class SearchForm(forms.Form):
    distance = forms.IntegerField()
    price = forms.IntegerField()
    traffic = forms.IntegerField()
    facility = forms.IntegerField()
    usability = forms.IntegerField()