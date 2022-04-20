from django import forms

from .models import Sortie

class TripForm(forms.ModelForm):
    class Meta:
        model = Sortie
        fields = ['trip_date', 'duration', 'nb_participant', 
                  'group_exp', 'weather', 'difficulty']