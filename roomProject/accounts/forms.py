from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'password1', 'password2',)