from django import forms
from .models import *


class searchForm(forms.Form):
    q = forms.CharField(required=False, label="Search", widget=forms.TextInput(attrs={'type':'search'}))
