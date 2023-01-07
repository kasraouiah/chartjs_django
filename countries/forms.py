from django import forms
from . models import Country
from . models import Club

class CountryDataForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class ClubDataForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = '__all__'