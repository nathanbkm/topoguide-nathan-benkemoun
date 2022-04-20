from django.urls import path

from . import views

app_name = 'iteneraires'
urlpatterns = [
    # ex: /itineraires/
    path('itineraires/', views.itineraires, name='itineraires'),
    # ex: /sorties/2/
    path('sorties/<int:itineraire_id>/', views.sorties, name='sorties'),
    
]