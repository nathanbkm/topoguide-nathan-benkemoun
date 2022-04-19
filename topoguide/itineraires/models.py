from django.db import models

class Itineraire(models.Model):
    """
    A single itinerary available
    """
    name = models.CharField('titre',max_length=200)
    start_point = models.CharField('point de départ',max_length=200)
    description = models.CharField(max_length=400)
    start_alt = models.FloatField('altitude de départ (m)') 
    alt_min = models.FloatField('altitude min (m)') 
    alt_max = models.FloatField('altitude max (m)') 
    elevation_gain = models.FloatField('dénivelé positif cumulé (m)')
    elevation_loss = models.FloatField('dénivelé négatif cumulé (m)')
    duration = models.FloatField('durée estimée (h)')
    DIF_CHOICE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    difficulty = models.IntegerField('difficulté', default=1, choices=DIF_CHOICE)
    
    
    def __str__(self):
        return self.name

