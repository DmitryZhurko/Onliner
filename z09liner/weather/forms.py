from django import forms

class CityForm(forms.Form):
    city = forms.CharField(widget=forms.TextInput(attrs={
         'placeholder': 'Введите название города'}))