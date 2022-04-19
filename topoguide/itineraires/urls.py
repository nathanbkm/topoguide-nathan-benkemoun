from django.urls import path

from . import views

app_name = 'iteneraires'
urlpatterns = [
    # ex: /itineraires/
    path('', views.get_itineraries, name='itineraires'),
]