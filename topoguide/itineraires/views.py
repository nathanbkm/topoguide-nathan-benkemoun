from django.shortcuts import get_list_or_404, render

from .models import Itineraire, Sortie

def itineraires(request):
    """
    Get all itineraries from database
    
    :param request: The incoming request
    """
    itineraries = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraries':itineraries})

def sorties(request, itineraire_id):
    """
    Get all trips from database for a specified itinerary 
    
    :param request: The incoming request
    :param itineraire_id: The itinerary's ID
    
    """
    sorties = get_list_or_404(Sortie, itineraire_id=itineraire_id )
    return render(request, 'itineraires/sorties.html', {'sorties': sorties})
