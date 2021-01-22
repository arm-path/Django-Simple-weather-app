from django import forms

from .models import City


class CityForm(forms.ModelForm):
    """ Форма для представления, поле ввода города """

    class Meta:
        model = City
        fields = ['title']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control'})}
