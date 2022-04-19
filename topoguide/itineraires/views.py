from django.shortcuts import get_list_or_404, render

from .models import Itineraire

def get_itineraries(request):
    """
    Get all itineraries from database
    :param request: The incoming request
    """
    itineraries = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraries':itineraries})
