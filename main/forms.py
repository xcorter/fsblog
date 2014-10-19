__author__ = 'Stepan'
from django import forms
from main.models import Tour, Claim

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim