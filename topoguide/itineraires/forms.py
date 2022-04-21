from django import forms

from .models import Sortie

class TripForm(forms.ModelForm):
    """
    A form based on models.Sortie with all fields execpt itineraire and utilisateur
    """
    class Meta:
        model = Sortie
        fields = ['trip_date', 'duration', 'nb_participant', 
                  'group_exp', 'weather', 'difficulty']