# tourism/models.py
from django.db import models
from user.models import CustomUser

class TouristPlace(models.Model):
    typical_food = models.TextField(blank=True, null=True)
    languages = models.CharField(max_length=255, blank=True, null=True)
    traditional_music = models.TextField(blank=True, null=True)
    city_tourist_map = models.TextField(blank=True, null=True)
    map_of_tourist_places_in_ecuador = models.TextField(blank=True, null=True)
    hotels = models.TextField(blank=True, null=True)
    regions = models.CharField(max_length=255, blank=True, null=True)

    users = models.ManyToManyField(CustomUser, related_name='places', blank=True)

    class Meta:
        db_table = 'tourist_places'
