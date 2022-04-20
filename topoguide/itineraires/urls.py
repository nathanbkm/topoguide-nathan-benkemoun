from django.urls import path

from . import views

app_name = 'itineraires'
urlpatterns = [
    # ex: /itineraires/
    path('itineraires/', views.itineraires, name='itineraires'),
    # ex: /sorties/2/
    path('sorties/<int:itineraire_id>/', views.sorties, name='sorties'),
    # ex: /sortie/2/
    path('sortie/<int:sortie_id>/', views.sortie, name='sortie'),
    
]