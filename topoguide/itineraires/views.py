from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Itineraire, Sortie
from .forms import TripForm

@login_required
def itineraires(request):
    """
    Get all itineraries from database
    
    :param request: The incoming request
    """
    itineraries = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraries':itineraries})

@login_required
def sorties(request, itineraire_id):
    """
    Get all trips from database for a specified itinerary 
    
    :param request: The incoming request
    :param itineraire_id: The itinerary's ID
    
    """
    sorties = get_list_or_404(Sortie, itineraire_id=itineraire_id )
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request, 'itineraires/sorties.html',
                  {'sorties': sorties, 'itineraire': itineraire})

@login_required()
def sortie(request, sortie_id):
    """
    Get the specified trip details
    :param request: The incoming request
    :param sortie_id: The trip's ID
    """
    sortie = get_object_or_404(Sortie, pk=sortie_id )
    return render(request, 'itineraires/sortie.html', {'sortie': sortie})

@login_required()
def nouvelle_sortie(request, itineraire_id):
    """
    Create a new trip related to a specified itinerary bases on user input in form
    Args:
        request: the incoming request, GET or POST
        itineraire_id: The itinerary's ID 
    Returns:
        - a page with an empty form if it was a GET request,
        - a page with an empty form if it was a POST request
          with invalid data,
        - or the page of the input trip if it was a POST with valid data
    """
    if request.method == 'GET':
        form = TripForm()
    elif request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            sortie = form.save(commit=False)
            sortie.utilisateur = request.user
            sortie.itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
            sortie.save()
            return redirect('itineraires:sortie', sortie.id)
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id )
    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form, 'itineraire': itineraire})
