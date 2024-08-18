# tourism/models.py
from django.db import models
from user.models import CustomUser

class TouristPlace(models.Model):
    especific_destination = models.TextField(blank=True, null=True)
    description_place = models.TextField(blank=True, null=True)
    typical_food = models.TextField(blank=True, null=True)
    languages = models.TextField( blank=True, null=True)
    traditional_music = models.TextField(blank=True, null=True)
    city_tourist_map = models.TextField(blank=True, null=True)
    map_of_tourist_places_in_ecuador = models.TextField(blank=True, null=True)
    hotels = models.TextField(blank=True, null=True)
    regions = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    users = models.ManyToManyField(CustomUser, related_name='places', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tourist_places'
