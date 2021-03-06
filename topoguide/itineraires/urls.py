from django.urls import path

from . import views

app_name = 'itineraires'
urlpatterns = [
    # ex: /itineraires/
    path('itineraires/', views.itineraires, name='itineraires'),
    # ex: /sorties/2/
    path('sorties/<int:itineraire_id>/', views.sorties, name='sorties'),
    # ex: /sortie/4/
    path('sortie/<int:sortie_id>/', views.sortie, name='sortie'),
    # ex: /nouvelle_sortie/2/
    path('nouvelle_sortie/<int:itineraire_id>/', views.nouvelle_sortie, name='nouvelle_sortie'),
    # ex: /modif_sortie/4/
    path('modif_sortie/<int:sortie_id>/', views.modif_sortie, name='modif_sortie'),
    
]