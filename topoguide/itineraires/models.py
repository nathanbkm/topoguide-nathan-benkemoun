from django.db import models

from django.contrib.auth.models import User

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
    
class Sortie(models.Model):
    """
    A single trip realized by on or many hikers
    """
    utilisateur = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    itineraire = models.ForeignKey(
        Itineraire,
        on_delete=models.CASCADE
    )
    trip_date = models.DateTimeField('date de la sortie')
    duration = models.FloatField('durée réelle (h)')
    nb_participant = models.IntegerField('nombre de participant')
    EXP_CHOICE = (
        ('Tous débutants','Tous débutants'),
        ('Tous expérimentés','Tous expérimentés'),
        ('Mixte','Mixte'),
    )
    group_exp = models.CharField('expérience du groupe', max_length=30, choices=EXP_CHOICE)
    WEATHER_CHOICE = (
        ('Mauvaise','Mauvaise'),
        ('Moyenne','Moyenne'),
        ('Bonne','Bonne'),
    )
    weather = models.CharField('météo', max_length=30, choices=WEATHER_CHOICE)
    DIF_CHOICE = (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    )
    difficulty = models.IntegerField('difficulté ressentie', default=1, choices=DIF_CHOICE)
    
    def __str__(self):
        return '%s %s'% (self.itineraire, self.trip_date)

